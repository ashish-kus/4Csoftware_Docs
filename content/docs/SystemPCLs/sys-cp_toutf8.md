---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 53
title: "sys.cp_toutf8"
---
## sys.cp_toutf8()
### Purpose
sys.cp_toutf8() converts 1 to 30 32 bit integer Unicode Codepoints to one UTF8 string.

### Usage
```c
utf8str = sys.cp_toutf8(<cp01> [,<cp02> ... ,<cp30> ]);
```

### Arguments
integer `<cpNN>` - Any valid Unicode 32bit codepoint.

### Returns
utf8 `<utf8str>` - A valid UTF8 string

### Where Used
sys.cp_toutf8() can be called from anywhere.

### Example
The demo.utf8.1 program, though silly and pointless, has several examples of using `sys.cp_toutf8()` to create UTF8 strings.

### Description
sys.cp_toutf8() converts 1 to 30 32 bit integer Unicode Codepoints to one UTF8 string. The total number of bytes in the returned utf8 string is stored in `sys_ret`.

### Bugs / Features / Comments
None

### See Also
- sys.utf8_charat()
- sys.utf8_count()
- sys.utf8_fix()
- sys.utf8_join()
- sys.utf8_split()
- sys.utf8_tocp()
- sys.utf8_verify()
