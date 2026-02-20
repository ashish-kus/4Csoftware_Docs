---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 155
title: "sys.get_help"
---
## sys.get_help()
### Purpose
sys.get_help() returns the value of the 4C environment variable XLHELPMSG.

### Usage
```c
helpmsg = sys.get_help();
```

### Arguments
None

### Returns
alpha <helpmsg>

"ON" - Field Help is on.

"OFF" - Field Help is off.

### Where Used
sys.get_help() can be called from anywhere. It is most likely used in system programs that may allow the user to change the value.

### Example
In the system program sys.help.set, the Init PCL calls `sys.get_help()` in order to display the current value before allowing the user to change it. The entire Init PCL follows:
```c
helpmsg = sys.get_help();
fkhelp = sys.get_fkhelp();
msgl1 = sys.get_msgline1();
msgl2 = sys.get_msgline2();
retsel = sys.get_return();
```

### Description
sys.get_help() returns the value of the 4C environment variable XLHELPMSG. This env variable is used to control whether 4C automatically displays help messages on all input fields. If `sys.get_help()` returns "ON", then 4C will display input field help messages. If the return is "OFF", then 4C does not display any input field help messages without the user explicitly requesting it.

### Bugs / Features / Comments
The values stored in the 4C Environment variables may be different than those at the shell. Calls to `sys.set_help()` etc do not modify the shell's environment, only 4C's internal copy. Even shells started from 4C will not share the same environment if the 4C environment has changed during running. Of Course this is subject to change.

### See Also
- sys.get_fkhelp()
- sys.get_msgline1()
- sys.get_msgline2()
- sys.get_return()
- sys.set_fkhelp()
- sys.set_help()
- sys.set_msgline1()
- sys.set_msgline2()
- sys.set_return()
