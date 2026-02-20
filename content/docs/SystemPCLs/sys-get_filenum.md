---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 145
title: "sys.get_filenum"
---
## sys.get_filenum()
### Purpose
sys.get_filenum() returns the internal file identifier that 4C uses internally instead of the asfile name.

### Usage
```c
<filenum> = sys.get_filenum([ <asprog>, ] <filename>);
```

### Arguments
alpha `<asprog>` - Optional asprog name of the program to find `<filename>` in. The default is the current program.

alpha `<filename>`

### Returns
integer `<filenum>`

`>= 0` - The filenum of the file with asfile name `<filename>`.

`< 0` - No asfile with name `<filename>` in current program.

### Where Used
sys.get_filenum() can be called from anywhere. Its main use is probably in programs used as screen and report writers that do not know which files they are reading until run time.

### Example
None

### Description
sys.get_filenum() returns the internal file identifier that 4C uses internally instead of the asfile name. 4C refers to all files internally by an integer. This integer can be used in any PCL that expects a file parameter. Programs that are used as report or screen writers may use sys.get_filenum() to read a file that is determined only at run time.

### Bugs / Features / Comments
None

### See Also
- sys.get_cdef()
