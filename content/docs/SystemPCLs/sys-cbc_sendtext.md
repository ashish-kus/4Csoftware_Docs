---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 23
title: "sys.cbc_sendtext"
---
## sys.cbc_sendtext()
### Purpose
sys.cbc_sendtext() adds 1 text item to the 4C clipboard.

### Usage
```c
<ret> = sys.cbc_sendtext(<text>);
```

### Arguments
alpha \<text\> - The text to copy.

### Returns
integer \<ret\>

-1 - Error - Either `sys.cbc_open()` has not been called, or the current type is not CBC_TEXT.

0 - OK

### Where Used
`sys.cbc_sendtext()` can be called only between the corresponding `sys.cbc_open()` and `sys.cbc_close()` calls and only if the \<type\> specified in the `sys.cbc_open()` call is CBC_TEXT.

### Example
None

### Description
sys.cbc_sendtext() adds 1 text item to the 4C clipboard.

### Bugs / Features / Comments
None

### See Also
- Cut/Copy/Paste Overview
- sys.cbc_senddata()
