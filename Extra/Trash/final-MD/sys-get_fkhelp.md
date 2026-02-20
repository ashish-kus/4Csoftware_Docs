---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 146
title: "sys.get_fkhelp"
---
## sys.get_fkhelp()
### Purpose
`sys.get_fkhelp()` returns the value of the 4C environment variable XLFKHELPMSG.

### Usage
```c
fkhelp = sys.get_fkhelp();
```

### Arguments
None

### Returns
alpha `<fkhelp>`

"ON" - Function Key Help is on.

"OFF" - Function Key Help is off.

"STATUS" - Only the message "f2=FKHELP" will display if function keys are available.

### Where Used
`sys.get_fkhelp()` can be called from anywhere. It is most likely used in system programs that may allow the user to change the value.

### Example
In the system program `sys.help.set`, the Init PCL calls `sys.get_fkhelp()` in order to display the current value before allowing the user to change it. The entire Init PCL follows:
```c
helpmsg = sys.get_help();
fkhelp = sys.get_fkhelp();
msgl1 = sys.get_msgline1();
msgl2 = sys.get_msgline2();
retsel = sys.get_return();
```

### Description
`sys.get_fkhelp()` returns the value of the 4C environment variable XLFKHELPMSG. This env variable is used to control how function key help messages display automatically. If `sys.get_fkhelp()` returns "ON", then 4C will display as much function key help messages as will fit on XLMSGLINE2. If the return is "OFF", then 4C does not display any function key help messages without the user explicitly requesting it. If the return is "STATUS", then 4C will display an appropriate message indicating how to get the function key help. This message will display for any input field that has any function keys enabled.

### Bugs / Features / Comments
The values stored in the 4C Environment variables may be different than those at the shell. Calls to `sys.set_help()` etc do not modify the shell's environment, only 4C's internal copy. Even shells started from 4C will not share the same environment if the 4C environment has changed during running. Of course this is subject to change.

### See Also
- sys.get_help()
- sys.get_msgline1()
- sys.get_msgline2()
- sys.get_return()
- sys.set_fkhelp()
- sys.set_help()
- sys.set_msgline1()
- sys.set_msgline2()
- sys.set_return()
