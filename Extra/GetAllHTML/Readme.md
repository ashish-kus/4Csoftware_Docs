# Hugo Markdown Converter

Batch-converts legacy markdown/HTML documentation files into clean **Hugo-compatible markdown** using LangChain + OpenAI. It automatically extracts the correct function title, generates Hugo front-matter, restructures content into standard sections, and writes output files with Hugo-friendly filenames.

---

## Requirements

- Python 3.9+
- An OpenAI API key

---

## Installation

**1. Clone or download this project, then navigate into the folder:**

```bash
cd hugo-markdown-converter
```

**2. (Recommended) Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies:**

```bash
pip install -r requirements.txt
```

**4. Set your OpenAI API key:**

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-...your-key-here...
```

Or export it directly in your shell:

```bash
export OPENAI_API_KEY=sk-...your-key-here...   # macOS / Linux
set OPENAI_API_KEY=sk-...your-key-here...       # Windows CMD
```

---

## Usage

```bash
python convert_to_hugo.py --input ./input_docs --output ./output_docs
```

### All Options

| Flag             | Short | Default       | Description                                             |
| ---------------- | ----- | ------------- | ------------------------------------------------------- |
| `--input`        | `-i`  | _(required)_  | Directory containing `.md` files to convert             |
| `--output`       | `-o`  | _(required)_  | Directory where converted files will be saved           |
| `--start-weight` | `-w`  | `1`           | Starting Hugo `weight` value (increments by 1 per file) |
| `--model`        |       | `gpt-4o-mini` | OpenAI model to use (e.g. `gpt-4o`, `gpt-4-turbo`)      |
| `--api-key`      |       | _(env var)_   | OpenAI API key (overrides `OPENAI_API_KEY` env var)     |
| `--help`         | `-h`  |               | Show all options and exit                               |

### Examples

**Basic conversion:**

```bash
python convert_to_hugo.py -i ./docs -o ./hugo_docs
```

**Start weights at 10 (e.g. for a second batch):**

```bash
python convert_to_hugo.py -i ./docs -o ./hugo_docs --start-weight 10
```

**Use a more powerful model:**

```bash
python convert_to_hugo.py -i ./docs -o ./hugo_docs --model gpt-4o
```

**Pass API key inline (no .env needed):**

```bash
python convert_to_hugo.py -i ./docs -o ./hugo_docs --api-key sk-...
```

---

## What It Does

For each `.md` file in the input directory, the converter will:

1. Read the file contents
2. Send it to OpenAI with a formatting prompt
3. Extract the correct Hugo `title` from the document's actual usage (e.g. `sys.cbc_init` not the filename)
4. Wrap the output in Hugo front-matter:
   ```yaml
   ---
   date: "2026-02-19T14:07:01+05:30"
   draft: false
   type: docs
   weight: 1
   title: "sys.cbc_init"
   ---
   ```
5. Restructure the body into standard sections: `Purpose`, `Usage`, `Arguments`, `Returns`, `Where Used`, `Example`, `Description`, `Bugs / Features / Comments`, `See Also`
6. Write the output as a Hugo-friendly filename (e.g. `sys-cbc_init.md`)

---

## Output Structure

```
output_docs/
├── beep.md
├── sys-cbc_init.md
├── sys-cbp_exit.md
└── sys-char_val.md
```

Dots in titles are replaced with dashes in filenames for Hugo compatibility.

---

## Troubleshooting

| Problem                                        | Fix                                                                                    |
| ---------------------------------------------- | -------------------------------------------------------------------------------------- |
| `ValueError: OpenAI API key required`          | Set `OPENAI_API_KEY` in `.env` or use `--api-key`                                      |
| `FileNotFoundError: Input directory not found` | Check your `--input` path exists                                                       |
| `No .md files found`                           | Make sure input directory contains `.md` files                                         |
| Rate limit / timeout errors                    | Reduce batch size or switch to a slower, cheaper model                                 |
| Output title is wrong                          | The LLM reads the Usage/Example section — ensure source docs have clear usage examples |

---

## Notes

- Files are processed in **alphabetical order**; weights increment by 1 per file.
- If a file fails, it is skipped and reported in the summary — other files continue processing.
- `temperature=0` is used for deterministic, consistent output.
- The script prints a summary of converted vs failed files at the end.
