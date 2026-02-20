---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 197
title: "sys.init_rusage"
---
## sys.init_rusage()
### Purpose
`sys.init_rusage()` saves the current resource usage so that a later call to `sys.get_rusage()` can return the resource usage since the last call to `sys.init_rusage()`

### Usage
```c
ret = sys.init_rusage();
```

### Arguments
None

### Returns
0 - Always returns 0

### Where Used
`sys.init_rusage()` can be called from anywhere but is typically called right before code that you are monitoring for resource usage.

### Example
The `sys.profile.s` bootstrap program has examples of both `sys.init_rusage()` and `sys.get_rusage()`.

### Description
`sys.init_rusage()` saves the current resource usage so that a later call to `sys.get_rusage()` can return the resource usage since the last call to `sys.init_rusage()`

### Bugs / Features / Comments
None

### See Also
- sys.get_rusage()
