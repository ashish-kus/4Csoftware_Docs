---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 10
title: "beep"
---
## beep()
### Purpose
beep() beeps the terminal.

### Usage
```c
beep();
```

### Arguments
None

### Returns
None

### Where Used
beep() can be called from anywhere.

### Example
```c
if (cm_read(cmcode < 0)) {
        beep();
        sys.exit_field(sys.cur_field);
}
```

### Description
Sends a beep to the terminal. Currently this is done by writing a ^G to the std err device. Possibly in the future a visible bell could be sent if it is defined for the terminal.

### Bugs / Features / Comments
None

### See Also
- sys.err_msg()
- sys.msg()
