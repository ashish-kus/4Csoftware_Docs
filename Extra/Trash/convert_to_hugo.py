"""
Hugo Markdown Converter
Converts a directory of markdown files to Hugo-compatible format using LangChain + OpenAI.

Usage:
    python convert_to_hugo.py --input ./input_docs --output ./output_docs --start-weight 1

Requirements:
    pip install langchain langchain-openai python-dotenv
"""

import os
import argparse
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# ── Hugo front-matter template ──────────────────────────────────────────────
FRONTMATTER_TEMPLATE = """---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: {weight}
title: "{title}"
---"""

# ── System prompt ────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are a technical documentation formatter.
Your job is to reformat legacy markdown/HTML documentation into clean Hugo-compatible markdown.

Rules:
1. Do NOT change any wording, meaning, or technical content.
2. Remove all HTML tags (span, anchor links like "Goto:", "Back to Top", etc.).
3. Structure sections using these exact headings (## for the function name, ### for sections):
   ## <function_name>()
   ### Purpose
   ### Usage
   ### Arguments
   ### Returns
   ### Where Used
   ### Example
   ### Description
   ### Bugs / Features / Comments
   ### See Also
4. Wrap all code/usage/example blocks in ```c ... ``` fences.
5. If a section has no content, write: None
6. In "See Also", list each item as a markdown bullet: - item_name() (strip HTML links, keep only the display text).
7. Inline function references in prose (like sys.cbc_init()) should be wrapped in backticks.
8. Don't add --- (horizontal rule) after each section.
9. Return ONLY the body markdown — no front-matter, no explanation, no extra commentary.
10. The first line of your output must be the ## heading for the function.

Determine the correct title (used for the Hugo front-matter) — it is exactly how the function
is called/used in the documentation itself, not the filename.
Look at the Usage section or how the function is invoked in examples to determine this.
For example:
  - If the doc says to call it as `beep()` → title is: beep
  - If the doc says to call it as `sys.cbp_exit()` → title is: sys.cbp_exit
  - If the doc says to call it as `sys.char_val()` → title is: sys.char_val
Strip the parentheses — the title is just the callable name without ().
Output the title on a special line at the very top in this exact format:
TITLE: <title_value>

Then a blank line, then the body markdown."""

# ── User prompt ──────────────────────────────────────────────────────────────
USER_PROMPT = """Convert the following documentation to Hugo markdown format.
The current weight for this file is: {weight}

--- DOCUMENT START ---
{content}
--- DOCUMENT END ---"""


def build_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("human", USER_PROMPT),
        ]
    )


def parse_response(
    response_text: str, weight: int, fallback_title: str
) -> tuple[str, str]:
    """
    Parse LLM response into (title, body_markdown).
    Expects first line: TITLE: <value>
    """
    lines = response_text.strip().splitlines()
    title = fallback_title
    body_start = 0

    if lines and lines[0].startswith("TITLE:"):
        title = lines[0].replace("TITLE:", "").strip()
        # Skip blank line after TITLE
        body_start = 2 if len(lines) > 1 and lines[1].strip() == "" else 1

    body = "\n".join(lines[body_start:])
    return title, body


def derive_output_filename(title: str) -> str:
    """
    Convert title like 'sys.cbc_end' → 'sys-cbc_end.md'
    Dots replaced with dashes for Hugo-friendly filenames.
    """
    safe = title.replace(".", "-")
    return f"{safe}.md"


def convert_file(
    input_path: Path,
    output_dir: Path,
    weight: int,
    chain,
) -> str:
    """Convert a single file. Returns the output filename written."""
    content = input_path.read_text(encoding="utf-8", errors="replace")
    fallback_title = input_path.stem  # use original filename as fallback

    print(f"  → Processing: {input_path.name} (weight={weight})")

    response = chain.invoke({"weight": weight, "content": content})
    response_text = response.content if hasattr(response, "content") else str(response)

    title, body = parse_response(response_text, weight, fallback_title)

    frontmatter = FRONTMATTER_TEMPLATE.format(weight=weight, title=title)
    full_output = f"{frontmatter}\n{body}\n"

    output_filename = derive_output_filename(title)
    output_path = output_dir / output_filename
    output_path.write_text(full_output, encoding="utf-8")

    print(f"     ✓ Written: {output_filename}  (title={title})")
    return output_filename


def main():
    parser = argparse.ArgumentParser(
        description="Convert markdown docs to Hugo format."
    )
    parser.add_argument(
        "--input", "-i", required=True, help="Input directory with .md files"
    )
    parser.add_argument(
        "--output", "-o", required=True, help="Output directory for converted files"
    )
    parser.add_argument(
        "--start-weight",
        "-w",
        type=int,
        default=1,
        help="Starting weight value (increments by 1)",
    )
    parser.add_argument(
        "--model",
        default="gpt-4o-mini",
        help="OpenAI model to use (default: gpt-4o-mini)",
    )
    parser.add_argument(
        "--api-key", help="OpenAI API key (or set OPENAI_API_KEY env var)"
    )
    args = parser.parse_args()

    # ── Setup ────────────────────────────────────────────────────────────────
    api_key = args.api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key required. Set OPENAI_API_KEY or use --api-key")

    input_dir = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")

    # ── Collect files ────────────────────────────────────────────────────────
    md_files = sorted(input_dir.glob("*.md"))
    if not md_files:
        print("No .md files found in input directory.")
        return

    print(f"\nFound {len(md_files)} markdown files.")
    print(f"Output directory: {output_dir.resolve()}")
    print(f"Starting weight: {args.start_weight}\n")

    # ── LangChain setup ──────────────────────────────────────────────────────
    llm = ChatOpenAI(
        model=args.model,
        temperature=0,
        api_key=api_key,
    )
    prompt = build_prompt()
    chain = prompt | llm

    # ── Process files ────────────────────────────────────────────────────────
    weight = args.start_weight
    converted = []
    failed = []

    for md_file in md_files:
        try:
            out_name = convert_file(md_file, output_dir, weight, chain)
            converted.append((md_file.name, out_name, weight))
            weight += 1
        except Exception as e:
            print(f"  ✗ FAILED: {md_file.name} — {e}")
            failed.append(md_file.name)

    # ── Summary ──────────────────────────────────────────────────────────────
    print(f"\n{'─'*50}")
    print(f"✓ Converted : {len(converted)} files")
    if failed:
        print(f"✗ Failed    : {len(failed)} files — {failed}")
    print(f"Output saved to: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
