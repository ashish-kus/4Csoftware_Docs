---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 143
title: "sys.get_field"
---
## sys.get_field()
### Purpose
sys.get_field() returns current display field's name.

### Usage
```c
fldname = sys.get_field();
```

### Arguments
None

### Returns
alpha <fldname>

any alpha - The current display field's name.

### Where Used
sys.get_field() can be called anytime there is a current display field. That is, anytime between SFldLp and EFldLp processing.

### Example
None

### Description
sys.get_field() returns the name of the current display field. This may be useful if the same PCL is called from more than one field and you need to display the name of the field for some reason, or just to distinguish between the fields that may have called the PCL.

### Bugs / Features / Comments
None

### See Also
- sys.get_program()
- sys.get_category()
