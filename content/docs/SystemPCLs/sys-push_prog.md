---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 247
title: "sys.push_prog"
---
## sys.push_prog()
### Purpose
None
### Usage
```c
sys.push_prog(<progname>[,Arg1-Arg15]);
ret = sys.push_prog(<progname> [,arg1 [..., [arg15]] ...]);
```
### Arguments
- progname - alpha
- arg1,arg2,...,arg15 0-15 optional alpha args that have meaning to the called program.
### Returns
- OK - program ran - exit code now in `$wexit_code`
- -1 - Err - Could not run program
### Where Used
sys.push_prog() can be called from anywhere.
### Example
```c
sys.push_prog("program");
```
### Description
sys.push_prog() runs a 4C program at the next higher level from the current program. This means, that the current program will not regain control until the pushed program and all programs that it starts exit. When the push program exits, the current program can check `$wexit_code` for the exit code.
### Bugs / Features / Comments
None
### See Also
- sys.link_prog()
- sys.exec_prog()
