---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 5
title: "atodate"
---
## atodate()
### Purpose
atodate() converts an alpha date to the internal integer format.

### Usage
idate = atodate(<adate>);

### Arguments
alpha <adate> - An alpha date in "mm/dd/yy" or "mm/dd/yyyy" format.

### Returns
date <idate> - internal date - which is an integer.

> 0 - The internal date representation of <adate>

0 - Error - bad format or Illegal date.

### Where Used
atodate() can be called from anywhere.

### Example
None

### Description
atodate() converts an alpha date to the 4C date format. The 4C date format is an integer representing the number of days since Dec 31, 1799. Thus, Jan 1, 1800 is represented by 1. 4C Does not deal with dates earlier than Jan 1, 1800.

### Bugs / Features / Comments
There is no way to specify the <adate> in anything besides American date format.

### See Also
- atodate()
- atotime()
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
