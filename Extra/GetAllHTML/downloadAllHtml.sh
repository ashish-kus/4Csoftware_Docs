#!/bin/bash

# Create output directory if not exists
OUTPUT_DIR="./4cSysPCL_html"
mkdir -p "$OUTPUT_DIR"

# Base URL
URL="https://www.4csoftware.com/docs/SysPCLs/index.html"

# Download HTML files
wget --recursive \
  --no-parent \
  --no-clobber \
  --level=1 \
  --accept "*.html" \
  --no-directories \
  --wait=0.5 \
  -P "$OUTPUT_DIR" \
  "$URL"

echo "Download completed."
