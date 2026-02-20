---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 293
title: "sys.set_eod"
---
## sys.set_eod()
### Purpose
sys.set_eod() sets the end of data flag for the current 4C program.

### Usage
```c
sys.set_eod();
```

### Arguments
None

### Returns
Always returns 0

### Where Used
sys.set_eod() can be called from anytime that current program is in the input field processing loop.

### Example
None

### Description
sys.set_eod() sets the end of data flag for the current program. This causes 4C to stop asking for input, but it continues all field processing and end fld loop processing. It acts as if the user entered \<accept\> except that no fkey PCL is run.

Requirements

sys.set_eod() requires 4CServer Version 4.6.2 or higher.

### Bugs / Features / Comments
None

### See Also
- sys.stack_fkey()
