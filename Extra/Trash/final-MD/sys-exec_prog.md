---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 88
title: "sys.exec_prog"
---
## sys.exec_prog()
### Purpose
sys.exec_prog() starts a new program in place of the current program.

### Usage
```c
sys.exec_prog(<progname>[,<arg1>-<arg15>]);
ret = sys.exec_prog(<progname> [,<arg1> [,..., [<arg15>]]]);
```

### Arguments
alpha `<progname>` - The name of the program to run.

alpha `<arg1>`, `<arg2>`, ..., `<arg15>` - 0-15 optional alpha args that have meaning to the called program.

### Returns
If successful, control never returns to calling program.

-1 - Err - Could not run program.

### Where Used
sys.exec_prog() can be called from anywhere.

### Example
None

### Description
sys.exec_prog() starts a program that runs in place of the currently running program. sys.exec_prog() is similar to sys.link_prog() because the execed program runs on the same level as the current program. The differences are that with sys.exec_prog(), control never returns to the current program. sys.exec_prog() can be used to restart the current program.

### Bugs / Features / Comments
None

### See Also
- sys.push_prog()
- sys.link_prog()
