---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 230
title: "sys.null_data"
---
## sys.null_data()
### Purpose
sys.null_data() sets all non primary key file variables for a file to a blank or 0.

### Usage
```c
ret = sys.null_data(<asfile>);
```

### Arguments
asfile <asfile> - The asfile name of the file to null the data for.

### Returns
0 - OK

-1 - Invalid <asfile>

### Where Used
sys.null_data() can be called from anywhere.

### Example
None

### Description
sys.null_data() sets all non primary key file variables for <asfile> to an empty string for alpha file variables and to a 0 for numeric file variables. sys.null_data() does not modify any permanent data. All modification is done on the file variables in memory.

### Bugs / Features / Comments
None

### See Also
- sys.null_file()
- sys.null_field()
