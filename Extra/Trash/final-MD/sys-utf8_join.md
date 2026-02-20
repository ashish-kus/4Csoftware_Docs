---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 345
title: "sys.utf8_join"
---
## sys.utf8_join()
### Purpose
None
### Usage
```c
<utf8str> = sys.utf8_join(<array[idx]> [, <maxelements>]);
```
### Arguments
- utf8 OR integer `<array[idx]>` - The starting element of either a UTF8 character array or a Unicode codepoint array
- integer `<maxelements>` - Optional argument that specifies the maximum number of elements from the array to join. If not specified, then all elements starting at index `<idx>` until the end of the array are joined.
### Returns
- utf8 `<utf8str>` - The UTF8 string created by joining the elements of the array into a utf8 string
### Where Used
`sys.utf8_join()` can be called from anywhere.
### Example
None
### Description
`sys.utf8_join()` joins the elements in either a utf8 character array or a unicode codepoint array and returns a new utf8 string.
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
