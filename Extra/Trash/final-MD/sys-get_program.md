---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 175
title: "sys.get_program"
---
## sys.get_program()
### Purpose
sys.get_program() returns the real program name of the current program.

### Usage
```c
progname = sys.get_program();
```

### Arguments
None

### Returns
alpha <progname>

The real program name of the current program

### Where Used
sys.get_program() can be called from anywhere.

### Example
The system program sys.mem.summary uses `sys.get_program()` to re exec itself. The advantage of doing this is that sys.mem.summary could be renamed, and it would still work. The code that does this is in the EndFldLp PCL getans(). Here it is:
```c
if (sys.get_answer("Again?",'y',1,INP_QUICK) == 'y')
    sys.exec_prog(sys.get_program());
```

### Description
sys.get_program() returns the real program name of the current program.

### Bugs / Features / Comments
Don't confuse this PCL with `sys.get_progname()`.

### See Also
- sys.get_progname()
- sys.get_category()
- sys.get_field()
