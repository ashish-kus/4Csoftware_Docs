---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 32
title: "sys.cbp_gettype"
---
## sys.cbp_gettype()
### Purpose
sys.cbp_gettype() returns the type of clipboard paste available.

### Usage
```c
type = sys.cbp_gettype();
```

### Arguments
None

### Returns
"" - No Paste Available.

"Text" - Text paste available

filename - 4C format paste is available using format of filename.

### Where Used
sys.cbp_gettype() can be called from anywhere as long as at least one paste operation has been done by the user.

### Example
None

### Description
sys.cbp_gettype() returns the type of clipboard paste available. The type of a paste is either "Text" or a 4C filename. The type returned when the data in the clipboard is not from a 4C application will always be "Text".

### Bugs / Features / Comments
None

### See Also
- Cut/Copy/Paste Overview
