---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 7
title: "atoi"
---
## atoi()
### Purpose
atoi() converts an alpha field to an integer field, and returns the integer field.

### Usage
```c
ival = atoi(aval);
```

### Arguments
alpha aval;

### Returns
integer ival;

There are no error returns from `atoi()`.

### Where Used
`atoi()` can be called from anywhere.

### Example
```c
fromdate = atoi(argv[3]);
```

### Description
This PCL takes one alpha argument and converts it to an integer, returning the integer.

### Bugs / Features / Comments
`atoi()` does not verify the format of aval.

### See Also
- atodate()
- atoi()
- atof()
- ftoa()
- itoa()
- sys.fmt_alpha()
- sys.fmt_choice()
- sys.fmt_date()
- sys.fmt_float()
- sys.fmt_integer()
- sys.fmt_time()
