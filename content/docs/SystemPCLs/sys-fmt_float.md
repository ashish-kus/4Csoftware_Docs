---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 113
title: "sys.fmt_float"
---
## sys.fmt_float()
### Purpose
sys.fmt_float() formats a float variable

### Usage
aret = `sys.fmt_float`(<fval>,<fmt>);

### Arguments
float <fval> - The float value to format.

alpha <fmt> - A valid format for a float variable.

### Returns
alpha <aret> - The formatted value.

### Where Used
sys.fmt_float() can be called from anywhere.

### Example
```c
fval = 129.23;
dpyval = `sys.fmt_float`(fval,">>>,>>9.99-");
```

### Description
sys.fmt_float() formats a float variable using the passed in format. It stores the formatted value in <aret>. <fval> is not changed by sys.fmt_float().

### Bugs / Features / Comments
It's difficult to tell if you passed in an invalid format, though if you do, the application will probably display an error message at runtime.

### See Also
- sys.fmt_field()
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
