---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 244
title: "sys.prog_isopen"
---
## sys.prog_isopen()
### Purpose
sys.prog_isopen() returns 1 if the current program is open.

### Usage
```c
ret = sys.prog_isopen();
```

### Arguments
None

### Returns
0 - Program is not open

1 - Program is open

### Where Used
sys.prog_isopen() can be called from anywhere.

### Example
None

### Description
sys.prog_isopen() is an easy way to determine if a screen program has a client window currently display or if a report program has a device open. This can be useful because some system PCLs only work when a program is open. i.e. sys.dflist_clear(), sys.dflist_add(), and others.

### Bugs / Features / Comments
Bugs

### See Also
- Sys PCLs List
