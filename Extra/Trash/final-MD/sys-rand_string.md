---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 254
title: "sys.rand_string"
---
## sys.rand_string()
### Purpose
`sys.rand_string()` returns a random string of length `<len>` from the characters `<charset>`.

### Usage
```c
rstr = sys.rand_string(<charset>,<len>);
```

### Arguments
- alpha `<charset>` - The set of characters to use to create the random string.
- integer `<len>` - The length of the string to return.

### Returns
- alpha `<rstr>` - The random string.

### Where Used
`sys.rand_string()` can be called from anywhere.

### Example
There are some examples of `sys.rand_string()` in the demo program dtf32.bld.1.

### Description
`sys.rand_string()` is used to create a cryptographically strong random string from the characters in `<charset>`. It can be used to create random numbers by limiting `<charset>` to the digits you want to allow in the number and then converting the return to a number. For example, to create a random 5 digit number use:
```c
n = atoi(sys.rand_string("0123456789",5));
```

### Bugs / Features / Comments
None

### See Also
- sys.rand_integer()
- mathfunc
