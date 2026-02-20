---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 191
title: "sys.get_tty"
---
## sys.get_tty()
### Purpose
sys.get_tty() returns the terminal name of \<username\>.

### Usage
```c
ttyname = sys.get_tty(\<username\>);
```

### Arguments
alpha \<username\> - the name of the user that you want the tty name of.

### Returns
"" - No such user \<username\> currently logged on.

alpha \<ttyname\> - The terminal name of user \<username\>.

### Where Used
sys.get_tty() can be called from anywhere. It could be used before a call to `sys.send_msg()` to determine the ttyname parameter.

### Example
None

### Description
sys.get_tty() returns the tty name of \<username\>. The "/dev/" is stripped off of the name returned.

### Bugs / Features / Comments
If more than one user with same name are running 4C, sys.get_tty() will only ever return the ttyname of one of them.  
Be careful not to confuse this routine with `sys.get_ttyname()` which uses a \<useridx\> instead of \<username\>.

### See Also
- sys.get_ttyname()
- sys.send_msg()
