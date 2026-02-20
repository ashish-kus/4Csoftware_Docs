---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 58
title: "sys.del_range"
---
## sys.del_range()
### Purpose
sys.del_range() deletes a set of sequential rcds in a file.

### Usage
ndel = `sys.del_range`(<asfile>, <fldidx>, <startaval>, <endaval>, <matchflag>);

### Arguments
asfile <asfile> - The file to delete rcds from.

integer <fldidx> - The fld identifier, normally the cdef for that field.

alpha <startaval> - Alpha representation of the starting value of the fld to start deleting from.

alpha <endaval> - Alpha representation of the ending value of the fld to end deleting from.

integer <matchflag> - Either MATCH_FULL or MATCH_PARTIAL. Flag indicating if the start and end values are matched in full or not.

### Returns
-1 - Error  
>= 0 - Number of rcds matched and delete attempted. Number of rcds successfully deleted is stored in sys_ret;

### Where Used
sys.del_range() can be called from anywhere.

### Example
None

### Description
sys.del_range() deletes a set of sequential rcds in a file. All fields in the file before fldidx need to be set before the call to sys.del_range.

### Bugs / Features / Comments
None

### See Also
- Sys PCLs List
