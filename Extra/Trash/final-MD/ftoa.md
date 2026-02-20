---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 116
title: "ftoa"
---
## ftoa()
### Purpose
ftoa() converts a float field to an alpha field, and returns the alpha field.

### Usage
```c
aval = ftoa(fval);
```

### Arguments
float fval;

### Returns
alpha aval;

### Where Used
ftoa() can be called from anywhere.

### Example
```c
sys.err_msg("fl =",ftoa(fl));
```

### Description
This PCL takes one float argument and converts it to an alpha, returning the alpha. It is mostly useful in converting float fields to alpha for display in error messages and in passing arguments.

### Bugs / Features / Comments
ftoa() does not allow specifying a format, but `sys.fmt_float()` can be called if this is necessary.

### See Also
- atodate()
- itoa()
- atoi()
- atof()
- sys.fmt_alpha()
- sys.fmt_choice()
- sys.fmt_date()
- sys.fmt_float()
- sys.fmt_integer()
- sys.fmt_time()
