---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 283
title: "sys.set_dfcolor"
---
## sys.set_dfcolor()
### Purpose
sys.set_dfcolor() allows a program to dynamically change the background and foreground color of a single ScreenProg display field.

### Usage
```c
ret = sys.set_dfcolor(<dflabel>,<fgrgbval>,<bgrgbval>);
```

### Arguments
- `<dflabel>` - integer var, should be the DFLABEL for the display field.
- `<fgrgbval>` - alpha var in "rrr:ggg:bbb" format If `<fgrgbval>` is "", it will not be changed. If it is "Default", it will change to the display fields default foreground.
- `<bgrgbval>` - alpha var in "rrr:ggg:bbb" format If `<bgrgbval>` is "", it will not be changed. If it is "Default", it will change to the display fields default background.

### Returns
The only value returned currently is 0.

### Where Used
sys.set_dfcolor() can be called from anywhere but most likely will be called from the Init PCL.

### Example
None

### Description
sys.set_dfcolor() allows a program to dynamically change the background and foreground color of a single display field. This can be useful if it cannot be known at program compile time.

### Bugs / Features / Comments
sys.set_dfcolor() is not implemented for scrollhdr or scrolldet fields.

### See Also
- sys.set_prcolor()
- sys.set_dricolor()
