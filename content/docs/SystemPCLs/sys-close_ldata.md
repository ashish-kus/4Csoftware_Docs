---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 39
title: "sys.close_ldata"
---
## sys.close_ldata()
### Purpose
sys.close_ldata() closes an open LData connection.

### Usage
```c
ret = sys.close_ldata(<ldname>);
```

### Arguments
<ldname> - an alpha var that was used in a previous call to `sys.open_ldata()`

### Returns
-1 = Failure and `sys.errno` will be set. Probably no open LData connection with name <ldname>.

0 - Success

### Where Used
sys.close_ldata() can be called from anywhere.

### Example
None

### Description
Use `sys.close_ldata()` to close non onetime LData connections with external processes.

### Bugs / Features / Comments
None

### See Also
- sys.open_ldata()
- sys.get_ldata()
- sys.set_ldata()
