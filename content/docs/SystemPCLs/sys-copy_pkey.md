---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 52
title: "sys.copy_pkey"
---
## sys.copy_pkey()
### Purpose
`sys.copy_pkey()` copies the primary key fields of 1 file to the primary key fields of another file.

### Usage
```c
ret = sys.copy_pkey([ <fromasprog>, ] <fromasfile>, [ <toasprog>, ] <toasfile>);
```

### Arguments
alpha - `<fromasprog>` - Optional arg to specify the name of the 4C program to find `<fromasfile>`. If not specified, the current program is used.

asfile - `<fromasfile>` - The 4C asfile to copy from.

alpha - `<toasprog>` - Optional arg to specify the name of the 4C program to find `<toasfile>`. If not specified, the current program is used.

asfile - `<toasfile>` - The 4C asfile to copy to.

### Returns
< 0 - Some error

0 - OK

### Where Used
`sys.copy_pkey()` can be called from anywhere.

### Example
None

### Description
`sys.copy_pkey()` copies the values in the primary key field buffers in memory of 1 4C file to the primary key field buffer in memory of another 4C file. Fields with incompatible field types in the 2 files are skipped.

### Bugs / Features / Comments
None

### See Also
- sys.copy_file()
- sys.copy_fields()
- sys.null_file()
- sys.null_data()
