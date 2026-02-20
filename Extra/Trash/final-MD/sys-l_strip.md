---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 222
title: "sys.l_strip"
---
## sys.l_strip()
### Purpose
sys.l_strip() strips all leading `<stripchar>` characters from the beginning of `<originalstring>`

### Usage
```c
<aret> = sys.l_strip(<originalstring>,<stripchar>);
```

### Arguments
alpha `<originalstring>` - The alpha variable to strip leading `<stripchar>` characters from.

alpha `<stripchar>` - A string of length 1 indicating the character that should be stripped from the beginning of `<originalstring>`.

### Returns
alpha `<aret>` - A copy of `<originalstring>` with the leading `<stripchar>` characters deleted.

### Where Used
sys.l_strip() can be called from anywhere.

### Example
None

### Description
None

### Bugs / Features / Comments
None

### See Also
- Sys PCLs List
