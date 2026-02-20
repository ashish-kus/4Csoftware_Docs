---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 144
title: "sys.get_filename"
---
## sys.get_filename()
### Purpose
None
### Usage
```c
<filename> = sys.get_filename([ <asprog>, ] <asfile>);
```
### Arguments
alpha `<asprog>` - Optional asprog name of the program to find `<asfile>` in. The default is the current program.

asfile `<asfile>`
### Returns
alpha `<filename>`
### Where Used
`sys.get_filename()` can be called from anywhere.
### Example
None
### Description
`sys.get_filename()` returns the 4C filename for `<asfile>`. It can be useful in PCLs that use an asfile as input parameters. Internally, 4C saves an asfile as an integer, so this is a way for an application to determine at runtime what 4C filename is associated with a PCL parameter.
### Bugs / Features / Comments
None
### See Also
- sys.get_asfile()
