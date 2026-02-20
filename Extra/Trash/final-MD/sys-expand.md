---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 97
title: "sys.expand"
---
## sys.expand()
### Purpose
sys.expand() expands the env vars in a string and returns the expanded string.

### Usage
aret = sys.expand(<str>);

### Arguments
alpha <str> - The alpha var to expand.

### Returns
alpha aret - The expanded string.

### Where Used
sys.expand() can be called from anywhere.

### Example
```c
str = sys.expand("${XLEXP}/sys.file_hdr.xl");
```

### Description
sys.expand() expands the env vars in a string and returns the expanded string.

### Bugs / Features / Comments
The env parts of a string must be indicated with the ${VAR} notation.

### See Also
- sys.cbp_exit()
- sys.char_val()
