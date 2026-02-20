---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 29
title: "sys.cbp_getnflds"
---
## sys.cbp_getnflds()
### Purpose
`sys.cbp_getnflds()` returns the number of flds in the current clipboard paste operation.

### Usage
```c
nflds = sys.cbp_getnflds();
```

### Arguments
None

### Returns
- -1 - No Paste Available.
- >= 0 - Number of flds in each clipboard paste item.

### Where Used
`sys.cbp_getnflds()` can be called from anywhere as long as at least one paste operation has been done by the user.

### Example
None

### Description
`sys.cbp_getnflds()` returns the number of flds in the current clipboard paste operation. If the format is a 4C clipboard format, then the number of fields will is the number of fields defined in the 4c file definition used as the template. If the format is a text format paste, then the number of fields will be one.

### Bugs / Features / Comments
None

### See Also
- Cut/Copy/Paste Overview
