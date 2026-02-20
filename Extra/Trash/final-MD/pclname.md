---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 346
title: "pclname"
---
## pclname()
### Purpose
None
### Usage
```c
ret = sys.utf8_split(<utf8str> [, <utf8array[idx]> [, <cparray[idx]>]);
```
### Arguments
- utf8 `<utf8str>` - A valid utf8 string
- utf8 `<utf8array[idx]>` - The starting item in a utf8array to store the utf8 characters into
- integer `<cparray[idx]>` - The starting item in an integer array to store the codepoints into

Both `<utf8array[idx]>` and `<cparray[idx]>` are optional arguments but at least one of them must be specified.
### Returns
integer `<ret>` - -1 on error, or the total number of items stored in either of the two arrays passed in.
### Where Used
`sys.utf8_split()` can be called from anywhere.
### Example
None
### Description
`sys.utf8_split()` splits a UTF8 string into an array of UTF8 characters and/or an array of Unicode codepoints.
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
