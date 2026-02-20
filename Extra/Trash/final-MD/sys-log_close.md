---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 212
title: "sys.log_close"
---
## sys.log_close()
### Purpose
sys.log_close() closes an open log.

### Usage
ret = sys.log_close(<lclname>);

### Arguments
alpha <lclname> - The name specified when the log was opened.

### Returns
0 - OK

-1 - <lclname> is not a currently open log.

### Where Used
sys.log_close() can be called from anywhere.

### Example
None

### Description
sys.log_close() explicitly closes an open log. Logs are implicitly closed if the application does not call `sys.close_log()` and the 4C program that opened the log exits.

### Bugs / Features / Comments
None

### See Also
- sys.log_open()
- sys.log_seek()
- sys.log_read()
- sys.log_getattr()
- sys.log_getname()
- sys.log_getval()
- sys.log_copyflds()
- sys.log_error()
