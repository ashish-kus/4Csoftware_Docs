---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 19
title: "sys.cbc_end"
---
## sys.cbc_end()
### Purpose
sys.cbc_end() finalizes the clipboard copy.

### Usage
```c
sys.cbc_end();
```

### Arguments
None

### Returns
None

### Where Used
sys.cbc_end() can only be called if a clipboard copy operation has been started by the 4csrvr application calling `sys.cbc_init()`. The `sys.cbc_init()` and `sys.cbc_end()` calls will normally nest a series of `sys.cbc_open()`, `sys.cbc_senddata()`, and `sys.cbc_close()` calls.

### Example
None

### Description
sys.cbc_end() finalizes the clipboard copy and makes the data available for pasting by the 4C Client and by other client applications.

### Bugs / Features / Comments
None

### See Also
- Cut/Copy/Paste Overview
- sys.cbc_init()
