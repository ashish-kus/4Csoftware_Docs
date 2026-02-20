---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 308
title: "sys.set_return"
---
## sys.set_return()
### Purpose
sys.set_return() allows you to change the 4C environment variable XLRETURN.

### Usage
```c
sys.set_return(<retsel>);
```

### Arguments
alpha `<retsel>` - Should be "SELECT" or "NOSELECT"

### Returns
None

### Where Used
sys.set_return() can be called from anywhere. It is most likely used in system programs that may allow the user to change the environment.

### Example
In the system program sys.help.set, the EndFld PCL for ok calls `sethelp()` which in turn calls `sys.set_return()` to set the user specified value for XLRETURN. The entire `sethelp()` PCL follows:
```c
sys.set_help(helpmsg);
sys.set_fkhelp(fkhelp);
sys.set_msgline1(msgl1);
sys.set_msgline2(msgl2);
sys.set_return(retsel);
```

### Description
sys.set_return() sets the value of the 4C environment variable XLRETURN. This env variable is used to control how a select screen acts when a `<RETURN>` is typed. If set to "SELECT", then a select screen will treat the `<RETURN>` key like accept. Otherwise, it will not.

### Bugs / Features / Comments
No errors returned for illegal val. If not set to "SELECT", "NOSELECT" is assumed. The values stored in the 4C Environment variables may be different than those at the shell. Calls to `sys.set_help()` etc do not modify the shell's environment, only 4C's internal copy. Even shells started from 4C will not share the same environment if the 4C environment has changed during running. Of Course this is subject to change.

### See Also
- sys.get_fkhelp()
- sys.get_help()
- sys.get_msgline1()
- sys.get_msgline2()
- sys.get_return()
- sys.set_fkhelp()
- sys.set_help()
- sys.set_msgline1()
- sys.set_msgline2()
