---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 245
title: "sys.pr_restart"
---
## sys.pr_restart()
### Purpose
`sys.pr_restart()` restarts the current program at the Start/Restart state.

### Usage
```c
ret = sys.pr_restart();
```

### Arguments
None

### Returns
-1 - Program is not currently open.

If `sys.pr_restart()` succeeds then there is no return to the calling PCL.

### Where Used
`sys.pr_restart()` can be called from anytime that the program is open. A program that has not finished executing the Open PCL or a program that has already started executing the Exit PCL is not considered open.

### Example
None

### Description
`sys.pr_restart()` can be used by the application to restart the current program. If the program is a screen program, the window will not disappear. Program and file variables are not cleared. If you need to reset file variables to some other initial state, you will want to use one or more of `sys.fl_save()`, `sys.fl_restore()`, and `sys.restore_share()`. 

If the program is a scrolling program, the driver is closed and any screen list will be cleared. If the program is a panel program and it has an initial option panel, then that initial option panel will get control after the Start/Restart PCL is executed.

### Bugs / Features / Comments
None

### See Also
- sys.fl_save()
- sys.restore_share()
- sys.fl_restore()
