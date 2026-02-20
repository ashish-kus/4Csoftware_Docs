---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 114
title: "sys.fmt_integer"
---
## sys.fmt_integer()
### Purpose
sys.fmt_integer() formats a integer variable

### Usage
aret = sys.fmt_integer(<ival>,<fmt>);

### Arguments
integer <ival> - The integer value to format.

alpha <fmt> - A valid format for a integer variable.

### Returns
alpha <aret> - The formatted value.

### Where Used
sys.fmt_integer() can be called from anywhere.

### Example
```c
ival = -129;
dpyval = sys.fmt_integer(ival,">>>,>>9-");
```

### Description
sys.fmt_integer() formats a integer variable using the passed in format. It stores the formatted value in <aret>. <ival> is not changed by sys.fmt_integer().

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
