---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 18
title: "sys.cbc_close"
---
## sys.cbc_close()
### Purpose
sys.cbc_close() ends the clipboard copy operation for the current type.

### Usage
```c
<ret> = sys.cbc_close(<asfile>);
```

### Arguments
asfile - `<asfile>` - Should be the same asfile used in the `sys.cbc_open()` call.

### Returns
integer - `<ret>`

-1 - Error - illegal `<asfile>` or `<asfile>` does not match the asfile used in the `sys.cbc_open()` call.

0 - OK

### Where Used
sys.cbc_close() can be called anytime while a clipboard copy operation is open.

### Example
None

### Description
sys.cbc_close() ends the clipboard copy operation for the current type and sends the data to the client. Even though the client has the data it will not be available for pasting by the 4C Client or by any other client application until the 4csrvr application has called `sys.cbc_end()`.

### Bugs / Features / Comments
None

### See Also
- Cut/Copy/Paste Overview
- sys.cbc_open()
- sys.cbc_end()
- sys.cbc_senddata()
- sys.cbc_sendtext()
