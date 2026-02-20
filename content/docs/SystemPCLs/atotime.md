---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 8
title: "atotime"
---
## atotime()
### Purpose
atotime() converts a string to a 4C time.

### Usage
tval = atotime(<timestr>);

### Arguments
alpha <timestr> - An alpha representation of a time.

### Returns
-1 - Invalid time string 
>= 0 - The 4c time.

### Where Used
atotime() can be called from anywhere.

### Example
None

### Description
atotime() converts a string to a 4c time value similar. It is fairly flexible, but expects the <timestr> to have only digits, spaces, ':'s and an optional "am", "a", "pm" or "p" suffix.

### Bugs / Features / Comments
Bugs

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
