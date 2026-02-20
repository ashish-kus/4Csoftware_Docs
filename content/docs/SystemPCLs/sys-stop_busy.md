---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 331
title: "sys.stop_busy"
---
## sys.stop_busy()
### Purpose
sys.stop_busy() stops a progress bar on the client.

### Usage
```c
sys.stop_busy(<name>);
```

### Arguments
\<name\> - The alpha that was used to start this progress bar in `sys.start_busy()`

### Returns
-1 - means no progress bar with name \<name\> was found. Otherwise 0 is returned.

### Where Used
sys.stop_busy() can be called from anywhere.

### Example
None

### Description
This system pcl causes a currently running progress bar to stop running on the client's display.

### Bugs / Features / Comments
None

### See Also
- sys.start_busy()
- sys.set_busy()
