---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 213
title: "sys.log_copyflds"
---
## sys.log_copyflds()
### Purpose
sys.log_copyflds() copies log rcd data to 4c file variables.

### Usage
```c
ret = sys.log_copyflds(<lclname>,<asfile>,<imagetype>);
```

### Arguments
alpha `<lclname>` - The name used to open the log file.

asfile `<asfile>` - The asfile name of the file to copy to.

integer `<imagetype>` - One of LOG_IMAGE_PKEY, LOG_IMAGE_BEFORE, or LOG_IMAGE_AFTER.

### Returns
`>= 0` - The number of fields copied.

`< 0` - Error

### Where Used
sys.log_copyflds() can be called anytime a log file is open and it has a current rcd.

### Example
None

### Description
sys.log_copyflds() copies log rcd data to 4c file variables. Fields are copied by matching name only, so if the file definition of the rcd in the log file does not match the file definition of `<asfile>` it is OK. Only those fields with matching names will be copied. The 4c file variables are updated in memory only. No file update is done. This PCL is expected to be useful for replication applications.

### Bugs / Features / Comments
None

### See Also
- sys.log_open()
- sys.log_close()
- sys.log_seek()
- sys.log_read()
- sys.log_getattr()
- sys.log_getname()
- sys.log_getval()
- sys.log_error()
