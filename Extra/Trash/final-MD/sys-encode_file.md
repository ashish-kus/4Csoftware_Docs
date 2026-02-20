---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 79
title: "sys.encode_file"
---
## sys.encode_file()
### Purpose
sys.encode_file() encodes the \<fromfile\> using the specified \<encodingmethod\> to \<tofile\>

### Usage
```c
ret = sys.encode_file(\<fromfilename\>,\<tofilename\>,\<encodingtype\>);
```

### Arguments
alpha \<fromfilename\> - the full pathname of the file you are reading unencoded data from.

alpha \<tofilename\> - the full pathname of the file you are writing the encoded data to.

integer - \<encodingtype\> - This must be one of ENCODE_NONE, ENCODE_BASE16, or ENCODE_BASE64

### Returns
0 - File was encoded successfully.

\< 0 - Some Error

### Where Used
sys.encode_file() can be called from anywhere.

### Example
None

### Description
sys.encode_file() encodes the \<fromfile\> using the specified \<encodingmethod\> to \<tofile\> The \<fromfile\> is not modified by sys.encode_file.

### Bugs / Features / Comments
Requires version 5.0 or higher of 4csrvr.

### See Also
- sys.decode_file()
- sys.encode_text()
- sys.decode_text()
