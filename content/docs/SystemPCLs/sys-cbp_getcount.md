---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 26
title: "sys.cbp_getcount"
---
## sys.cbp_getcount()
### Purpose
`sys.cbp_getcount()` returns the number of clipboard paste items available.

### Usage
```c
count = sys.cbp_getcount();
```

### Arguments
None

### Returns
- -1 - No Paste Available.
- >= 0 - count of items available.

### Where Used
`sys.cbp_getcount()` can be called from anywhere as long as at least one paste operation has been done by the user.

### Example
None

### Description
`sys.cbp_getcount()` returns the number of clipboard paste items available.

### Bugs / Features / Comments
None

### See Also
- Cut/Copy/Paste Overview
