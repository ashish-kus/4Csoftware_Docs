---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 56
title: "sys.decode_file"
---
## sys.decode_file()
### Purpose
sys.decode_file() decodes the \<fromfile\> using the specified \<encodingmethod\> to \<tofile\>

### Usage
```c
ret = sys.decode_file(\<fromfilename\>,\<tofilename\>,\<encodingtype\>);
```

### Arguments
alpha \<fromfilename\> - the full pathname of the file you are reading encoded data from.

alpha \<tofilename\> - the full pathname of the file you are writing the decoded data to.

integer - \<encodingtype\> - This must be one of ENCODE_NONE, ENCODE_BASE16, or ENCODE_BASE64

### Returns
0 - File was decoded successfully.

\< 0 - Some Error

### Where Used
sys.decode_file() can be called from anywhere.

### Example
None

### Description
sys.decode_file() decodes the \<fromfile\> using the specified \<encodingmethod\> to \<tofile\> The \<fromfile\> is not modified by `sys.encode_file`.

### Bugs / Features / Comments
None

### See Also
- sys.encode_file()
- sys.decode_file()
- sys.encode_text()
- sys.decode_text()
