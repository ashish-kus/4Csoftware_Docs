---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 35
title: "sys.choose_color"
---
## sys.choose_color()
### Purpose
sys.choose_color() selects a color using the clients color dialog.

### Usage
```c
rgbval = sys.choose_color(<initrgb>);
```

### Arguments
<initrgb> - an alpha of the form rrr:ggg:bbb that is the default color.

### Returns
<rgbval> - An alpha of the form rrr:ggg:bbb. If the user cancels, then "" is returned.

### Where Used
sys.choose_color() can be called from anywhere.

### Example
None

### Description
sys.choose_color() allows the user to select a color. You may store this color and use it in subsequent calls to `sys.set_prcolor()`, `sys.set_dfcolor()`, and `sys.set_dricolor()`.

### Bugs / Features / Comments
None

### See Also
- sys.set_prcolor()
- sys.set_dfcolor()
- sys.set_dricolor()
