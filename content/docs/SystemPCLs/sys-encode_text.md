---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 80
title: "sys.encode_text"
---
## sys.encode_text()
### Purpose
sys.encode_text() encodes the \<fromtext\> alpha field using the specified \<encodingmethod\> and returns the encoded text.

### Usage
etext = `sys.encode_text`(\<fromtext\>,\<encodingtype\>);

### Arguments
alpha \<fromtext\> - A 4C alpha field or literal.

integer - \<encodingtype\> - This must be one of ENCODE_NONE, ENCODE_BASE16, ENCODE_BASE64, or ENCODE_BASE64URL

### Returns
"" - Some Error

Any other alpha - \<fromtext\> was encoded successfully.

### Where Used
sys.encode_text() can be called from anywhere.

### Example
None

### Description
sys.encode_text() encodes the \<fromtext\> using the specified \<encodingmethod\> and returns the result as an alpha variable. The \<fromtext\> 4C field is not modified by `sys.encode_text`.

### Bugs / Features / Comments
Requires version 5.0 or higher of 4csrvr.

### See Also
- sys.encode_file()
- sys.decode_file()
- sys.encode_text()
- sys.decode_text()
