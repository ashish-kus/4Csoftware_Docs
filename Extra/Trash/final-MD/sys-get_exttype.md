---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 140
title: "sys.get_exttype"
---
## sys.get_exttype()
### Purpose
sys.get_exttype() returns the external type of a 4C file defined as External.

### Usage
```c
type = sys.get_exttype(<asfile>);
```

### Arguments
asfile <asfile> - The asfile name of the file you want to get the ext type for.

### Returns
"" - <asfile> is not defined as External.

any alpha - the exttype of <asfile>

### Where Used
sys.get_exttype() can be called from anywhere.

### Example
None

### Description
sys.get_exttype(<asfile>) returns the External type of the file.

### Bugs / Features / Comments
None

### See Also
- sys.set_exttype()
