---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 115
title: "sys.fmt_time"
---
## sys.fmt_time()
### Purpose
sys.fmt_time() formats a time variable

### Usage
aret = sys.fmt_time(<tmval>,<fmt>);

### Arguments
time <tmval> - The time value to format.

alpha <fmt> - A valid format for a time variable.

### Returns
alpha <aret> - The formatted value.

### Where Used
sys.fmt_time() can be called from anywhere.

### Example
```c
tm = (14 * 60 * 60) + (32 * 60) + 24;
dpyval = sys.fmt_time(tm,"HH:mm:ss");
```

### Description
sys.fmt_time() formats a time variable using the passed in format. It stores the formatted value in <aret>. <tmval> is not changed by sys.fmt_time().

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
