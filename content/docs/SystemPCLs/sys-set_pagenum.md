---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 303
title: "sys.set_pagenum"
---
## sys.set_pagenum()
### Purpose
sys.set_pagenum() allows you to modify the internal 4C page number variable.

### Usage
```c
ret = sys.set_pagenum(<newpagenum>);
```

### Arguments
integer `<pagenum>` - The new pagenumber to set for the current output device.

### Returns
integer `<ret>`

0 - OK

-1 - Current program has no current output device.

### Where Used
sys.set_pagenum() can be called from anywhere. It makes most sense to call it in report programs after a `sys.page()` call and before the printing of any headers, especially those that may print the page number.

### Example
None

### Description
sys.set_pagenum() changes the internal variable for the current page number of the current output device. This only affects the return of the system PCL `sys.get_pagenum()`. Internally, another variable is kept that maintains the absolute page number. This means that `sys.get_linediff()` and `sys.get_pagediff()` work even after a call to `sys.set_pagenum()`. Both of those PCLs rely on the internal absolute page number variable.

### Bugs / Features / Comments
No checks for ridiculous numbers (i.e. negative) are done.

### See Also
- sys.page()
- sys.get_pagenum()
