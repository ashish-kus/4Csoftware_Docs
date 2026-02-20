---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 253
title: "sys.rand_integer"
---
## sys.rand_integer()
### Purpose
sys.rand_integer() returns a random integer >= lowval and <= highval

### Usage
```c
ival = sys.rand_integer(lowval,highval);
```

### Arguments
- integer/int64 - lowval
- integer/int64 - highval

### Returns
- integer/int64 - ival

### Where Used
sys.rand_integer() can be called from anywhere.

### Example
None

### Description
sys.rand_integer() returns a random integer between the 2 passed in values. On error -1 is returned and sys_ret is set to SYSRET_ERROR. The values passed in can be either 32bit integer values or 64bit integer values.

### Bugs / Features / Comments
None

### See Also
- sys.rand_string()
- mathfunc
