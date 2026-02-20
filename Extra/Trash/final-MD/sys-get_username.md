---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 193
title: "sys.get_username"
---
## sys.get_username()
### Purpose
`sys.get_username()` returns the user name of the user identified by `<useridx>`.

### Usage
```c
username = sys.get_username(<useridx>);
```

### Arguments
integer `<useridx>` - The index into the 4C user info table. This must be `>= 0` and `< sys.get_maxusers()`.

### Returns
alpha `<username>` - The username associated with `<useridx>`

"" - No user associated with `<useridx>`

### Where Used
`sys.get_username()` can be called from anywhere. It is used by some of the system configuration and display programs.

### Example
The following code is the Init PCL for `sys.ui.display`.
```c
maxusers = sys.get_maxusers();
nusers = sys.get_nusers();
sys.create_tfile(sys.usr_info);
for (i = 0; i < maxusers; i += 1) {
    if ((sys.ui_usrname = sys.get_username(i)) == "")
        continue;
    sys.ui_idx = i;
    sys.read_file(sys.usr_info,F_ADD|F_NODEBLOCK);
    sys.ui_ttyname = sys.get_ttyname(i);
    totusrsize += sys.ui_maxumem = sys.get_maxumem(i);
    sys.upd_file(sys.usr_info,F_DEFAULT);
}
sys.ui_usrname = ""; /* clear for drinit */
```

### Description
`sys.get_username()` returns the user name of the user identified by `<useridx>`. The user info table is an internal table maintained by 4C. Some entries may be blank due to users logging on and off. The main purpose of this routine is to aid in system programs that display configuration and usage information.

### Bugs / Features / Comments
None

### See Also
- sys.get_idx()
- sys.get_maxusers()
- sys.get_nusers()
- sys.get_ttyname()
