---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 22
title: "sys.cbc_senddata"
---
## sys.cbc_senddata()
### Purpose
sys.cbc_senddata() adds 1 data item to the 4C clipboard.

### Usage
```c
<ret> = sys.cbc_senddata(<asfile>);
```

### Arguments
asfile `<asfile>` - The 4C asfile that holds the data to be copied.

### Returns
integer `<ret>`

-1 - Error - Either `sys.cbc_open()` has not been called, illegal asfile, or, in the case of CBC_4CTYPE copy, the filename of `<asfile>` does not match the filename of the `<asfile>` used in the `sys.cbc_open()` call.

0 - OK

### Where Used
`sys.cbc_senddata()` can be called only between the corresponding `sys.cbc_open()` and `sys.cbc_close()` calls.

### Example
None

### Description
sys.cbc_senddata() adds 1 data item to the 4C clipboard.

### Bugs / Features / Comments
None

### See Also
- Cut/Copy/Paste Overview
- sys.cbc_sendtext()
