---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 340
title: "sys.unshare_field"
---
## sys.unshare_field()
### Purpose
sys.unshare_field() stops sharing of one field with other fields

### Usage
```c
ret = sys.unshare_field(<field>);
```

### Arguments
\<field\> - Any valid file variable in the program

### Returns
integer \<ret\> - 0 if \<field\> is unshared successfully, -1 if \<field\> was not shared to start with.

### Where Used
sys.unshare_field() can be called from anywhere. It is most likely to be used in programs where `sys.share_field()` was used to dynamically shared fields at run time.

### Example
None

### Description
sys.unshare_field() stops sharing of one field with other fields This is most likely used when dynamic sharing was used in a program by calling `sys.set_share()`

### Bugs / Features / Comments
Bugs

### See Also
- sys.share_field()
