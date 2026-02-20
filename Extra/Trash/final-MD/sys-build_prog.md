---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 15
title: "sys.build_prog"
---
## sys.build_prog()
### Purpose
sys.build_prog() compiles a program.

### Usage
ret = sys.build_prog(<progname>);

### Arguments
alpha <progname> - The name of the program to build.

### Returns
integer <ret>

0 - OK

-1 - Error - Probably no such program or compile error, a message has been displayed.

### Where Used
sys.build_prog() can be called from anywhere. It most likely will be called from system development programs, and not from other application programs.

### Example
The system development programs use the <user15> key to compile a program. the statement executed when you press <user15> from one of the development programs is:

```c
sys.build_prog(sys.pr_name);
```

### Description
sys.build_prog() compiles the named program. Any errors during compilation cause an appropriate message to be displayed, and for sys.build_prog() to return -1.

4C does not compile programs in the sense that machine code is generated. 4C reads the spec files and converts them into easy to interpret tables and stores the result in the XLSEQFILE. It does the same with files. The terms build and compile will be used to both mean read the 4C specs and write the XLSEQFILE tables.

### Bugs / Features / Comments
None

### See Also
- sys.reset_prog()
- sys.build_file()
