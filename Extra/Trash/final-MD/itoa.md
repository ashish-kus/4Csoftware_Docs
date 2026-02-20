---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 206
title: "itoa"
---
## itoa()
### Purpose
itoa() converts an integer field to an alpha field, and returns the alpha field.

### Usage
```c
aval = itoa(ival);
```

### Arguments
integer ival;

### Returns
<aval> - alpha representation of <ival>

### Where Used
itoa() can be called from anywhere.

### Example
```c
push_prog("an.call.de.1",itoa($row_ofst+1),"0");
```

### Description
This PCL takes one integer argument and converts it to an alpha, returning the alpha.

### Bugs / Features / Comments
None

### See Also
- atodate()
- atoi()
- atof()
- ftoa()
- sys.fmt_alpha()
- sys.fmt_choice()
- sys.fmt_date()
- sys.fmt_float()
- sys.fmt_integer()
- sys.fmt_time()
