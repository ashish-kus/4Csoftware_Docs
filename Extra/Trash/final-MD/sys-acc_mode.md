---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 4
title: "sys.acc_mode"
---
## sys.acc_mode()
### Purpose
sys.acc_mode() returns the the last access mode for a file.

### Usage
accmode = sys.acc_mode([ <asprog>, ] <asfile>);

### Arguments
alpha <asprog> - Optional asprog name of the program to find <asfile> in. The default is the current program.

asfile <asfile> - The asfile name of the file to return the last access mode for.

### Returns
integer accmode

ACC_ADD - The last access of <asfile> was for add.

ACC_DELETE - The last access of <asfile> was for delete.

ACC_MODIFY - The last access of <asfile> was for modify.

ACC_NORMAL - <asfile> has not been read for any update mode. accessed yet, or it has already been updated.

### Where Used
sys.acc_mode() can be called from anywhere.

### Example
None

### Description
sys.acc_mode() returns the mode that <asfile> will be updated in if you were to call `sys.upd_file()` at the same pt in your program. Thus a `sys.read_file()` that returns an error for whatever reason will cause `sys.acc_mode()` to return ACC_NORMAL. A `sys.read_file()` for delete that is successful will cause `sys.acc_mode()` to return ACC_DELETE. Once `sys.upd_file()` is called `sys.acc_mode()` will return ACC_NORMAL. If your program does not call `sys.upd_file()`, but returns to a state prior to the state it was in when the last `sys.read_file()` was called `sys.acc_mode()` will also return ACC_NORMAL. This means that if you read a file on field 4 in modify mode, but you do not call `sys.upd_file()` and your program processes field 4 again, or some other previous state, fld 3, 2, 1 or SLOOP, then `sys.acc_mode()` will return ACC_NORMAL, not ACC_MODIFY.

### Bugs / Features / Comments
None

### See Also
- sys.read_file()
- sys.upd_file()
