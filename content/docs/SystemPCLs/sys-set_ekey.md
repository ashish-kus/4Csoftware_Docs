---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 291
title: "sys.set_ekey"
---
## sys.set_ekey()
### Purpose
sys.set_ekey() sets the end position for sequential reads.

### Usage
```c
ret = sys.set_ekey(<asfile>,<fldcdef>,<matchtype>);
```

### Arguments
asfile - <asfile> - The asfile name of the file you are setting the end key pos for.

integer <fldcdef> - The cdef of the fld you want to seek to.

integer <matchflag> - Either MATCH_FULL or MATCH_PARTIAL

### Returns
0 - End Pos Set OK

-1 - Some Error

### Where Used
sys.set_ekey() will typically be called before reading a file sequentially.

### Example
See the demo.seekkey.1 demo program for an example.

### Description
sys.set_ekey() sets the end position for sequential reading of a file. It is typically used along with `sys.set_skey()`, and `sys.seek_key()` before calling `sys.read_file(...,F_SEQNEXT)`. Before calling sys.set_ekey() set values into the fields that need them.

### Bugs / Features / Comments
None

### See Also
- sys.set_skey()
- sys.seek_key()
- sys.read_file()
