---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 94
title: "sys.exit_layout"
---
## sys.exit_layout()
### Purpose
sys.exit_layout() exits all programs in the current layout.

### Usage
```c
sys.exit_layout();
```

### Arguments
This PCL takes no arguments.

### Returns
0 - OK

-1 - Current program is not a screen program.

### Where Used
sys.exit_layout() can be called from a ScreenProg only.

### Example
None

### Description
sys.exit_layout() exits all programs in the same layout as the current ScreenProg. If the current program is not a ScreenProg, then sys.exit_layout() returns -1.

### Bugs / Features / Comments
Programs exited using sys.exit_layout() will have an exit code of -3.

### See Also
- sys.exit_prog()
- sys.end_prog()
