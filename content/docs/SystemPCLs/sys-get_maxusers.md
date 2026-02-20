---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 165
title: "sys.get_maxusers"
---
## sys.get_maxusers()
### Purpose
`sys.get_maxusers()` returns the max number of users that 4C is configured for.

### Usage
```c
maxusers = sys.get_maxusers();
```

### Arguments
None

### Returns
integer <maxusers> - The max number of users that 4C is configured for.

### Where Used
`sys.get_maxusers()` can be called from anywhere. It is used by some of the system configuration/display programs.

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
`sys.get_maxusers()` returns the max number of users that 4C is configured for. This corresponds to the Users parameter in the XLCONFIG file.

### Bugs / Features / Comments
None

### See Also
- sys.get_idx()
- sys.get_nusers()
- sys.get_ttyname()
- sys.get_username()
