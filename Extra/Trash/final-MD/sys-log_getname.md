---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 216
title: "sys.log_getname"
---
## sys.log_getname()
### Purpose
sys.log_getname() returns a fieldname of a field in the log file.

### Usage
```c
aval = sys.log_getname(<lclname>,<fldidx>);
```

### Arguments
alpha `<lclname>` - The name used to open the log file.

integer `<fldidx>` - The idx of the fld in the current log rcd. The `<fldidx>` must be >= 0 and < total number of fields in the current log rcd.

### Returns
alpha `<aval>` - The name of the requested field.

"" - Error

### Where Used
sys.log_getname() can be called anytime a log file is open and there is a current log rcd.

### Example
The 4cSys application uses sys.log_getname() in the log.view.det program.

### Description
sys.log_getname() returns a fieldname of a field in the log file.

### Bugs / Features / Comments
None

### See Also
- sys.log_open()
- sys.log_close()
- sys.log_seek()
- sys.log_read()
- sys.log_getattr()
- sys.log_getval()
- sys.log_copyflds()
- sys.log_error()
