---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 6
title: "atof"
---
## atof()
### Purpose
atof() converts an alpha field to a float field, and returns the float field.

### Usage
```c
fval = atof(aval);
```

### Arguments
alpha aval;

### Returns
float fval;

There are no error returns from this PCL.

### Where Used
atof() can be called from anywhere.

### Example
```c
fl = atof("3.24");
```

### Description
This PCL takes one alpha argument and converts it to a float, returning the float. A leading or trailing sign can be used. It is possible to get garbage in the return if the alpha argument was garbage also.

### Bugs / Features / Comments
atof() does not verify the format of aval.

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
