---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 220
title: "sys.log_seek"
---
## sys.log_seek()
### Purpose
sys.log_seek() sets the next log rcd ptr

### Usage
ret = sys.log_seek(<lclname>,<logdate>,<logtime>,<logsequence>);

### Arguments
alpha <lclname> - The name used when the log was opened.

date <logdate> - The date portion of the log_idx key

time <logtime> - The time portion of the log_idx key

integer <logsequence> - The sequence portion of the log_idx key

### Returns
0 - OK

-1 - <lclname> does not refer to an open log

### Where Used
sys.log_seek() can be called anytime a log is open.

### Example
The log.view.det and log.view.key 4C programs in the 4cSys application both use `sys.log_seek()`.

### Description
sys.log_seek() sets the log rcd ptr on an open log.

### Bugs / Features / Comments
None

### See Also
- sys.log_open()
- sys.log_close()
- sys.log_read()
- sys.log_getattr()
- sys.log_getname()
- sys.log_getval()
- sys.log_copyflds()
- sys.log_error()
