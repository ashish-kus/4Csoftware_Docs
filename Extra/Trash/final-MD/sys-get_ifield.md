---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 158
title: "sys.get_ifield"
---
## sys.get_ifield()
### Purpose
`sys.get_ifield()` returns an integer value from an integer field by name.

### Usage
```c
ival = sys.get_ifield([<asprog>], <asfilename>, <fieldname>);
```

### Arguments
- `asprog <asprog>` - The asprog name of the program to use to find `<asfilename>` and `<fieldname>`. This is an optional argument, and if not used, the current program is assumed.
- `alpha <asfilename>` - The asfile name of the file containing `<fieldname>`. This must be passed in quotes, or in an alpha variable.
- `alpha <fieldname>` - The name of the field who's value you want. This must be passed in quotes, or in an alpha variable. Dimesioned variables can be used also using a format like "field[n]".

### Returns
- `integer` - `<ival>` - The value in field `<fieldname>`
- `-1` - Possible error, but could also mean that `<fieldname>` has the value -1.

### Where Used
`sys.get_ifield()` can be called from anywhere. It may be used in report/screen writers that do not know what fields they are using until runtime.

### Example
None

### Description
`sys.get_ifield()` locates the field identified by `<fieldname>` and returns the value in it. `sys.get_ifield()` is meant to be used when you don't know the field to get until runtime.

### Bugs / Features / Comments
If `<fieldname>` is not an integer type, no error is indicated, and -1 will be returned.

### See Also
- sys.get_fmtfield()
- sys.get_afield()
- sys.get_ffield()
- sys.put_fmtfield()
- sys.put_afield()
- sys.put_ffield()
