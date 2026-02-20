---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 259
title: "sys.reset_prog"
---
## sys.reset_prog()
### Purpose
sys.reset_prog() sets a program for recompile.

### Usage
```c
ret = sys.reset_prog(<progname>);
```

### Arguments
alpha `<progname>` - The name of the program to reset.

### Returns
0 - OK

-1 - Error - Probably no such program, a message has been displayed.

### Where Used
sys.reset_prog() can be called from anywhere. It most likely will be called from system development programs, and not from other application programs.

### Example
```c
sys.prog.reset is pushed from sys.fh.maint to reset programs using the current file. sys.prog.reset calls sys.reset_prog() from the SortSel PCL for the sys.pr_file driver. The PCL is named resetprog(). Its code follows:
sys.reset_prog(sys.pf_prname);
```

### Description
sys.reset_prog() reads the sys.program file, and resets the sys.pr_sftime field to 0. This causes the program to recompile the next time that it is run.

### Bugs / Features / Comments
None

### See Also
- sys.build_prog()
- sys.build_file()
