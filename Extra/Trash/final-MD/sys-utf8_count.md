---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 343
title: "sys.utf8_count"
---
## sys.utf8_count()
### Purpose
`sys.utf8_count()` returns the number UTF8 characters in `<utf8str>`

### Usage
```c
count = sys.utf8_count(<utf8str>);
```

### Arguments
utf8 `<utf8str>` - A valid UTF8 string

### Returns
integer `<count>` - The number of UTF8 characters in `<utf8str>`, -1 for error

### Where Used
`sys.utf8_count()` can be called from anywhere.

### Example
None

### Description
`sys.utf8_count()` returns the number UTF8 characters in `<utf8str>`. If `<utf8str>` is not a valid UTF8 string, then -1 is returned.

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
