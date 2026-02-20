---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 111
title: "sys.fmt_date"
---
## sys.fmt_date()
### Purpose
sys.fmt_date() formats a date variable

### Usage
aret = sys.fmt_date(<dtval>,<fmt>);

### Arguments
date <dtval> - The date value to format.

alpha <fmt> - A valid format for a date variable.

### Returns
alpha <aret> - The formatted value.

### Where Used
sys.fmt_date() can be called from anywhere.

### Example
```c
dt = atodate("01/01/1970");
dpyval = sys.fmt_date(dt,"mm/dd/yyyy");
```

### Description
sys.fmt_date() formats a date variable using the passed in format. It stores the formatted value in <aret>. <dtval> is not changed by sys.fmt_date().

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
