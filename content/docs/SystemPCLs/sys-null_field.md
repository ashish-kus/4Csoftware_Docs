---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 231
title: "sys.null_field"
---
## sys.null_field()
### Purpose
sys.null_field() sets the referenced file variable to a blank or 0.

### Usage
```c
ret = sys.null_field(<asfile>,<fldcdef>);
```

### Arguments
asfile `<asfile>` - The asfile name of the file

integer `<fldcdef>` - The CDefine of the variable in `<asfile>` to null.

### Returns
0 - OK

-1 - Invalid `<asfile>`

### Where Used
sys.null_field() can be called from anywhere.

### Example
None

### Description
sys.null_field() sets the referenced file variable to an empty string if it is an alpha file variable or to a 0 if it is a numeric file variable. `sys.null_field()` does not modify any permanent data. All modification is done on the file variable in memory.

### Bugs / Features / Comments
None

### See Also
- sys.null_file()
- sys.null_data()
