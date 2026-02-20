---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 103
title: "sys.fl_getval"
---
## sys.fl_getval()
### Purpose
`sys.fl_getval()` returns an alpha representation of a single file variable.

### Usage
```c
<avar> = sys.fl_getval(<asfile>,<fldidx>);
```

### Arguments
- `asfile <asfile>` - The asfile associated with the filevar.
- `integer <fldidx>` - The index of the field in `<asfile>`. Normally, the CDefine of a field in `<asfile>` will be used.

### Returns
- `""` - If `sys_ret != SYSRET_OK`, then this is an error. Either invalid `<asfile>` or invalid `<fldidx>`.
  
If `sys_ret == SYSRET_OK`, then this is a valid return.

- Any other alpha - The formatted filevar

### Where Used
`sys.fl_getval()` can be called from anywhere.

### Example
None

### Description
When working with dynamic files, you cannot reference fields by name. In order to access fields in a dynamic file, you can use `sys.fl_getval()` and `sys.fl_setval()`. `sys.fl_getval()` formats the filevar using the format defined in the data dictionary and returns this formatted alpha.

### Bugs / Features / Comments
None

### See Also
- sys.fl_setval()
- sys.get_dfile()
