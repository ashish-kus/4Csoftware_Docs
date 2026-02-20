---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 274
title: "sys.set_busy"
---
## sys.set_busy()
### Purpose
sys.set_busy() allows you to modify either the title or the label of a running progress bar.

### Usage
```c
sys.set_busy(<name>, <type>, <newtext>);
```

### Arguments
\<name\> - The alpha that was used to start this progress bar in `sys.start_busy()`

\<type\> - One of SB_TITLE or SB_LABEL indicating what you are changing.

\<newtext\> - The new text for the progress bar title or label.

### Returns
-1 - means no progress bar with name \<name\> was found. Otherwise 0 is returned.

### Where Used
sys.set_busy() can be called from anywhere.

### Example
None

### Description
This system pcl allows you to change either the label or the title of a currently running progress bar.

### Bugs / Features / Comments
None

### See Also
- sys.start_busy()
- sys.stop_busy()
