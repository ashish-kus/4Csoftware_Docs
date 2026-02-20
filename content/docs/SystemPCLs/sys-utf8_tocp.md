---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 347
title: "sys.utf8_tocp"
---
## sys.utf8_tocp()
### Purpose
`sys.utf8_tocp()` returns the 32bit integer codepoint for the utf8 character starting at byte 0 in `<utf8char>`.

### Usage
```c
cp = sys.utf8_tocp(<utf8char>);
```

### Arguments
utf8 `<utf8char>` - A single utf8 character byte string

### Returns
integer `<cp>` - The unicode code point for the utf8 char starting at byte 0 in `<utf8char>` or -1 if the first byte is the start of an invalid utf8 character.

### Where Used
`sys.utf8_tocp()` can be called from anywhere.

### Example
The demo.test.1 program has an example of using `sys.utf8_tocp()`.

### Description
`sys.utf8_tocp()` returns the 32bit integer codepoint for the utf8 character starting at byte 0 in `<utf8char>`. If the return is >= 0, then `<utf8char>` corresponded to the start of a valid UTF8 character and the number of bytes in that character is then stored in `sys_ret`. If the codepoint returned is less than 0, then the first byte in `<utf8char>` was not the beginning of a valid UTF8 character.

### Bugs / Features / Comments
None

### See Also
- sys.cp_toutf8()
- sys.utf8_charat()
- sys.utf8_count()
- sys.utf8_fix()
- sys.utf8_join()
- sys.utf8_split()
- sys.utf8_tocp()
- sys.utf8_verify()
