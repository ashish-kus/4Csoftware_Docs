---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 199
title: "sys.int_val"
---
## sys.int_val()
### Purpose
sys.int_val() converts an alpha character to an integer value.

### Usage
ivar = sys.int_val(<aval>);

### Arguments
<aval> - The alpha to convert to ascii.

### Returns
<ivar> - The integer equivalent of <aval>.

### Where Used
sys.int_val() can be called from anywhere.

### Example
```c
/* Convert 1 char to lower case */
if ((avar(i,i) >= 'A') && (avar(i,i) <= 'Z'))
    avar(i,i) = sys.char_val(sys.int_val(avar(i,i))+32);
```

### Description
sys.int_val() converts an alpha character to its equivalent integer value.

### Bugs / Features / Comments
None

### See Also
- sys.char_val()
