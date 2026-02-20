---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 217
title: "sys.log_getval"
---
## sys.log_getval()
### Purpose
sys.log_getval() returns a formatted field from a log rcd.

### Usage
aval = sys.log_getval(<lclname>,<fldidx>,<imagetype>);

### Arguments
alpha <lclname> - The name used to open the log file.

integer <fldidx> - The idx of the fld in the current log rcd. The <fldidx> must be >= 0 and < total number of fields in the current log rcd.

integer <imagetype> - One of LOG_IMAGE_PKEY, LOG_IMAGE_BEFORE, or LOG_IMAGE_AFTER.

### Returns
alpha <aval> - The formatted value of the requested field.

"" - If sys.errno is set then this indicates an error.

### Where Used
sys.log_getval() can be called anytime a log file is open and it has a current rcd.

### Example
The 4cSys application has examples of using sys.log_getval() in the log.view.det program.

### Description
sys.log_getval() returns a formatted field from a log rcd. Use the <imagetype> parameter to specify whether the value you want corresponds to the original value (LOG_IMAGE_BEFORE), the updated value (LOG_IMAGE_AFTER) or a primary key value (LOG_IMAGE_PKEY). Not all log rcds will have a BeforeImage or an AfterImages. This will depend on the way the log was defined and the update type. All log rcds will have a PKeyImage.

### Bugs / Features / Comments
None

### See Also
- sys.log_open()
- sys.log_close()
- sys.log_seek()
- sys.log_read()
- sys.log_getattr()
- sys.log_getname()
- sys.log_copyflds()
- sys.log_error()
