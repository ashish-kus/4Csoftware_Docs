---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 120
title: "sys.get_asfile"
---
## sys.get_asfile()
### Purpose
None
### Usage
```c
<name> = sys.get_asfile([ <asprog>, ] <asfile>);
```
### Arguments
- alpha `<asprog>` - Optional asprog name of the program to find `<asfile>` in. The default is the current program.
- asfile `<asfile>`
### Returns
- alpha `<name>`
### Where Used
sys.get_asfile() can be called from anywhere.
### Example
None
### Description
sys.get_asfile() returns the 4C asfile name for `<asfile>`. It can be useful in PCLs that use an asfile as input parameters. Internally, 4C saves an asfile as an integer, so this is a way for an application to determine at runtime what 4C asfile name is associated with a PCL parameter.
### Bugs / Features / Comments
None
### See Also
- sys.get_filename()
