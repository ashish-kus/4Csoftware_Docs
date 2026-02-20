---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 109
title: "sys.fmt_alpha"
---
## sys.fmt_alpha()
### Purpose
sys.fmt_alpha() formats an alpha variable

### Usage
aret = sys.fmt_alpha(<aval>,<fmt>);

### Arguments
alpha <aval> - The alpha value to format.

alpha <fmt> - A valid format for an alpha variable.

### Returns
alpha <aret> - The formatted value.

### Where Used
sys.fmt_alpha() can be called from anywhere.

### Example
```c
ssno = "123456789";
dpyval = sys.fmt_alpha(ssno,"999-99-9999");
```

### Description
sys.fmt_alpha() formats an alpha variable using the passed in format. It stores the formatted value in <aret>. <aval> is not changed by sys.fmt_alpha().

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
