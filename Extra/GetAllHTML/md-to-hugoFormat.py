"""
Hugo Markdown Converter
Converts a directory of markdown files to Hugo-compatible format using LangChain + OpenAI.

Usage:
    python convert_to_hugo.py --input ./input_docs --output ./output_docs
    python convert_to_hugo.py -i ./docs -o ./out --start-weight 10 --model gpt-4o
    python convert_to_hugo.py -i ./docs -o ./out --api-key sk-...

Requirements:
    pip install -r requirements.txt
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
    """Convert a single markdown file to Hugo format.

    Reads the file, sends it to the LLM chain, parses the TITLE from the
    response, prepends Hugo front-matter, and writes the result to output_dir.

    Args:
        input_path: Path to the source .md file.
        output_dir: Directory where the converted file will be written.
        weight:     Hugo front-matter weight value for this file.
        chain:      LangChain runnable (prompt | llm).

    Returns:
        The filename (not full path) of the written output file.

    Raises:
        Any exception raised by the LLM call or file I/O is propagated
        to the caller so it can be caught and logged per-file.
    """
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


def build_arg_parser() -> argparse.ArgumentParser:
    """Build and return the CLI argument parser with full help text."""
    parser = argparse.ArgumentParser(
        prog="convert_to_hugo.py",
        description=(
            "Hugo Markdown Converter\n"
            "------------------------\n"
            "Batch-converts legacy markdown/HTML documentation files into\n"
            "clean Hugo-compatible markdown using LangChain + OpenAI.\n\n"
            "Each file gets Hugo front-matter (title, weight, draft, date),\n"
            "its content restructured into standard doc sections, and is\n"
            "saved with a Hugo-friendly filename (dots → dashes)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  Basic usage:\n"
            "    python convert_to_hugo.py -i ./input_docs -o ./output_docs\n\n"
            "  Start weights at 10 (for a second batch):\n"
            "    python convert_to_hugo.py -i ./docs -o ./out --start-weight 10\n\n"
            "  Use a more powerful model:\n"
            "    python convert_to_hugo.py -i ./docs -o ./out --model gpt-4o\n\n"
            "  Pass API key inline (no .env needed):\n"
            "    python convert_to_hugo.py -i ./docs -o ./out --api-key sk-...\n\n"
            "Environment:\n"
            "  OPENAI_API_KEY  Your OpenAI API key. Can also be set in a .env file\n"
            "                  in the current directory.\n\n"
            "Output filenames:\n"
            "  Titles are extracted from the document's Usage/Example section.\n"
            "  Dots in titles are replaced with dashes, e.g.:\n"
            "    sys.cbc_init  →  sys-cbc_init.md\n"
        ),
    )

    parser.add_argument(
        "--input",
        "-i",
        required=True,
        metavar="DIR",
        help=(
            "Path to the input directory containing .md files to convert. "
            "Files are processed in alphabetical order. "
            "Example: ./input_docs"
        ),
    )

    parser.add_argument(
        "--output",
        "-o",
        required=True,
        metavar="DIR",
        help=(
            "Path to the output directory where converted Hugo markdown files "
            "will be written. Created automatically if it does not exist. "
            "Example: ./hugo_output"
        ),
    )

    parser.add_argument(
        "--start-weight",
        "-w",
        type=int,
        default=1,
        metavar="N",
        help=(
            "Starting value for the Hugo front-matter 'weight' field. "
            "Weight increments by 1 for each file processed, controlling "
            "the order pages appear in Hugo's sidebar/menu. "
            "Useful when converting files in multiple batches. "
            "Default: 1"
        ),
    )

    parser.add_argument(
        "--model",
        default="gpt-4o-mini",
        metavar="MODEL",
        help=(
            "OpenAI model to use for conversion. "
            "Faster/cheaper: gpt-4o-mini (default). "
            "Higher quality: gpt-4o, gpt-4-turbo. "
            "Default: gpt-4o-mini"
        ),
    )

    parser.add_argument(
        "--api-key",
        metavar="KEY",
        help=(
            "OpenAI API key (e.g. sk-...). "
            "If not provided, the OPENAI_API_KEY environment variable or "
            ".env file will be used."
        ),
    )

    return parser


def main():
    parser = build_arg_parser()
    args = parser.parse_args()

    # ── Setup ────────────────────────────────────────────────────────────────
    api_key = args.api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        parser.error(
            "OpenAI API key is required.\n"
            "  Option 1: Set OPENAI_API_KEY in your environment or .env file.\n"
            "  Option 2: Pass it with --api-key sk-..."
        )

    input_dir = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    if not input_dir.exists():
        parser.error(f"Input directory not found: {input_dir}")

    # ── Collect files ────────────────────────────────────────────────────────
    md_files = sorted(input_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in: {input_dir.resolve()}")
        print("Make sure the directory contains files with a .md extension.")
        return

    print(f"\nHugo Markdown Converter")
    print(f"{'─' * 50}")
    print(f"Input  : {input_dir.resolve()}")
    print(f"Output : {output_dir.resolve()}")
    print(f"Model  : {args.model}")
    print(f"Files  : {len(md_files)} markdown files found")
    print(f"Weights: {args.start_weight} → {args.start_weight + len(md_files) - 1}")
    print(f"{'─' * 50}\n")

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
    print(f"\n{'─' * 50}")
    print(f"✓ Converted : {len(converted)} file(s)")
    if failed:
        print(f"✗ Failed    : {len(failed)} file(s) — {failed}")
    print(f"Output saved to: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
