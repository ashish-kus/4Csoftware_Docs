---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 70
title: "sys.dr_range"
---
## sys.dr_range()
### Purpose
`sys.dr_range()` allows you to set the start and end range of rcds to be read for a driver.

### Usage
```c
sys.dr_range(<asfile>,<fldcdef>,<sval>,<eval>,<matchtype>);
```

### Arguments
asfile `<asfile>` - The asfile name of the driver being run.

integer `<fldcdef>` - The fld num in asfile to use for setting the range. This should be passed as a CDEFINE.

alpha `<sval>` - Starting val in range. This must be passed as an alpha. 4C will convert it to the proper type.

alpha `<eval>` - Ending val in range. This must be passed as an alpha. 4C will convert it to the proper type.

integer `<matchtype>` - This can be MATCH_FULL or MATCH_PARTIAL only.

### Returns
None

### Where Used
`sys.dr_range()` can ONLY be called from the DrInit PCL of any driver.

### Example
None

### Description
`sys.dr_range()` allows you to specify a range rcds in the driver file by specifying a range of values for ONE field in the driver file. You pass in the start and end values that the field will have and a flag specifying either MATCH_FULL, or MATCH_PARTIAL. MATCH_FULL specifies that trailing blanks for an alpha key must match also. All key fields before the specified field must be set before calling `sys.dr_range()`.

### Bugs / Features / Comments
None

### See Also
- sys.set_skey()
- sys.set_ekey()
- sys.seek_key()
- sys.dr_init()
