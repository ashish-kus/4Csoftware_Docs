#!/bin/bash

# Check if pandoc is installed
if ! command -v pandoc &>/dev/null; then
  echo "Error: pandoc is not installed."
  exit 1
fi

# Convert all HTML files in current directory
for file in *.html; do
  # Skip if no HTML files found
  [ -e "$file" ] || continue

  output="${file%.html}.md"
  pandoc "$file" -f html -t gfm -o "$output"
  echo "Converted: $file -> $output"
done

echo "All conversions completed."
