---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 157
title: "sys.get_idx"
---
## sys.get_idx()
### Purpose
sys.get_idx() returns the index into the user table of the current process.

### Usage
```c
<useridx> = sys.get_idx();
```

### Arguments
None

### Returns
integer `<useridx>` - The index into the internal user info table.

### Where Used
sys.get_idx() can be called from anywhere.

### Example
None

### Description
sys.get_idx() returns the index into the internal user table for the current 4C process.

### Bugs / Features / Comments
None

### See Also
- sys.get_maxusers()
- sys.get_nusers()
- sys.get_ttyname()
- sys.get_username()
