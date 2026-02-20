---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 251
title: "sys.put_fmtfield"
---
## sys.put_fmtfield()
### Purpose
sys.put_fmtfield() converts an alpha to the appropriate type and stores it in a field.

### Usage
```c
ret = sys.put_fmtfield([<asprog>], <asfilename>, <fieldname>, <fmtval>);
```

### Arguments
alpha `<asprog>` - The asprog name of the program to use to find `<asfilename>` and `<fieldname>`. This is an optional argument, and if not used, the current program is assumed.

alpha `<asfilename>` - The asfile name of the file containing `<fieldname>`. This must be passed in quotes, or in an alpha variable.

alpha `<fieldname>` - The name of the field you want to store the value. This must be passed in quotes, or in an alpha variable. Dimesioned variables can be used also using a format like "field[n]".

alpha `<fmtval>` - The formatted value to convert and store in `<field>`. This field is passed by name and should not be quoted.

### Returns
0 - OK - `<fmtval>` converted and stored in `<fieldname>`

-1 - Error - Either `<asprog>` or `<asfilename>` or `<fieldname>` or `<fmtval>` is invalid.

### Where Used
sys.put_fmtfield() can be called from anywhere. It is used in the 4C debugger programs to allow you to change the value of fields in running programs.

### Example
There are several examples in the 4C debugger program sys.dbg.fld.det.

### Description
sys.put_fmtfield() converts an alpha to the appropriate type and stores the converted value in `<field>`.

### Bugs / Features / Comments
None

### See Also
- sys.get_fmtfield()
- sys.get_afield()
- sys.get_ffield()
- sys.get_ifield()
- sys.put_afield()
- sys.put_ffield()
- sys.put_ifield()
