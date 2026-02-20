---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 134
title: "sys.get_dfile"
---
## sys.get_dfile()
### Purpose
sys.get_dfile() allocates memory for and returns the filenum for a dynamic file.

### Usage
fileno = sys.get_dfile(<afilename>);

### Arguments
alpha <afilename> - The name of the dynamic file.

### Returns
>= 0 - The filenum that can be used in any calls that need an <asfile>.

-1 - Error - Invalid <afilename> for current application

### Where Used
sys.get_dfile() can be called from anywhere.

### Example
The global system PCL sys.rcd_exists() makes uses sys.get_dfile().

### Description
sys.get_dfile() can be used in situations where a 4C program does not know ahead of time the files it will need to access. The fileno returned by sys.get_dfile() can be used in any SysPCL needing an <asfile> argument. When you no longer need the fileno, memory is freed by calling `sys.rel_dfile(fileno)`. Any dynamic files that are not released using `sys.rel_dfile()` will be released when the 4C program that allocated them exits.

### Bugs / Features / Comments
None

### See Also
- sys.rel_dfile()
- sys.fl_getval()
- sys.fl_setval()
