---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 219
title: "sys.log_read"
---
## sys.log_read()
### Purpose
None
### Usage
```c
ret = sys.log_read(<lclname>,<readtype>);
```
### Arguments
alpha `<lclname>` - The name used in opening the log

integer `<readtype>` - Either LOG_READNEXT or LOG_READEXACT
### Returns
0 - Log rcd read

-1 - Either log not open or invalid `<readtype>`
### Where Used
`sys.log_read()` can be called anytime a log is open.
### Example
The log.view.det has an example of `sys.log_read()` using LOG_READEXACT and the log.view.key program has an example of `sys.log_read()` using LOG_READNEXT. Both programs are in the 4cSys application.
### Description
`sys.log_read()` reads a single log rcd. Once read, that rcd becomes the current log record and `sys.log_getattr()`, `sys.log_getname()`, `sys.log_getval()`, and `sys.log_copyflds()` can be used on that rcd. Before the first call to `sys.log_read()` using LOG_READNEXT, the application should call `sys.log_seek()`. Before every call to `sys.log_read()` using LOG_READEXACT, the application should call `sys.log_seek()`.
### Bugs / Features / Comments
None
### See Also
- sys.log_open()
- sys.log_close()
- sys.log_seek()
- sys.log_getattr()
- sys.log_getname()
- sys.log_getval()
- sys.log_copyflds()
- sys.log_error()
