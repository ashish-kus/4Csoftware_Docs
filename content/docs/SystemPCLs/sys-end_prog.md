---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 85
title: "sys.end_prog"
---
## sys.end_prog()
### Purpose
sys.end_prog() ends the current 4C program

### Usage
```c
sys.end_prog();
```

### Arguments
None

### Returns
No Returns

### Where Used
sys.end_prog() can be called from anywhere.

### Example
None

### Description
sys.end_prog() exits all current processing in the current 4C program. This includes but is not limited to PCLs, drivers, dpy fields. The program will still run the ExitPCL.

### Bugs / Features / Comments
None

### See Also
- sys.exit_prog()
