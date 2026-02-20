---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 24
title: "sys.cbp_exit"
---
## sys.cbp_exit()
### Purpose
sys.cbp_exit() exits the paste loop.

### Usage
```c
sys.cbp_exit([<code>]);
```

### Arguments
integer `<code>` - Optional code. Currently unused.

### Returns
None

### Where Used
sys.cbp_exit() can be called anytime during the paste loop but when used is usually called during PasteInit.

### Example
None

### Description
sys.cbp_exit() exits the paste loop. The most likely reason to call `sys.cbp_exit()` is that the user has tried to paste an incompatible type of data to the 4C application. After calling `sys.cbp_exit()`, 4C will next process the PasteEnd state.

### Bugs / Features / Comments
None

### See Also
- Cut/Copy/Paste Overview
