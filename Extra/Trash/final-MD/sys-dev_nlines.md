---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 59
title: "sys.dev_nlines"
---
## sys.dev_nlines()
### Purpose
`sys.dev_nlines()` returns the number of lines on the current output device.

### Usage
```c
nlines = sys.dev_nlines();
```

### Arguments
None

### Returns
integer nlines - The number of lines on the current output device.

### Where Used
`sys.dev_nlines()` can be called from anywhere, but you should be careful if it is called from the Init, End, or Exit PCLs.

### Example
None

### Description
`sys.dev_nlines()` returns the number of lines on the current output device. The current output device may not be the same device as that specified by the program. This is possible if `sys.dev_nlines()` is called from the Init PCL, and the calling program is not using the same device. In this case, `sys.dev_nlines()` would return the number of lines for the calling program's output device.

### Bugs / Features / Comments
None

### See Also
- sys.get_msgline1()
- sys.get_msgline2()
