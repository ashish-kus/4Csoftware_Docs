---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 110
title: "sys.fmt_choice"
---
## sys.fmt_choice()
### Purpose
sys.fmt_choice() formats an choice variable

### Usage
aret = sys.fmt_choice(<aval>,<fmt>);

### Arguments
alpha <aval> - The alpha value to format.

alpha <fmt> - A valid format for a choice variable.

### Returns
alpha <aret> - The formatted value.

### Where Used
sys.fmt_choice() can be called from anywhere.

### Example
```c
ans = 'y'
dpyval = sys.fmt_choice(ans,"Yes:No");
```

### Description
sys.fmt_choice() formats a choice variable using the passed in format. It stores the formatted value in <aret>. <aval> is not changed by sys.fmt_choice().

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
