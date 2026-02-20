---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 348
title: "sys.utf8_verify"
---
## sys.utf8_verify()
### Purpose
sys.utf8_verify() verifys that all bytes in `<utf8str>` are valid and returns 0 if they are and -1 if they are not.

### Usage
```c
ret = sys.utf8_verify(<utf8str>);
```

### Arguments
utf8 `<utf8str>` - A string of bytes that may or may not be a valid utf8 str.

### Returns
integer `<ret>` - 0 if `<utf8str>` is a valid UTF8 string, -1 if not

### Where Used
sys.utf8_verify() can be called from anywhere.

### Example
None

### Description
sys.utf8_verify() verifys that all bytes in `<utf8str>` are valid and returns 0 if they are and -1 if they are not. When -1 is returned, the byte index into `<utf8str>` of the start of the 1st invalid utf8 character is saved in sys_ret.

### Bugs / Features / Comments
Requirements: 4csrvr version 6.4.3 or later

### See Also
- sys.cp_toutf8()
- sys.utf8_charat()
- sys.utf8_count()
- sys.utf8_fix()
- sys.utf8_join()
- sys.utf8_split()
- sys.utf8_tocp()
- sys.utf8_verify()
