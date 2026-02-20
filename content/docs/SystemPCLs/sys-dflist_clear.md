---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 61
title: "sys.dflist_clear"
---
## sys.dflist_clear()
### Purpose
None
### Usage
```c
ret = sys.dflist_clear(<dflabel>);
```
### Arguments
integer - `<dflabel>` - This should be the DFLABEL of the display field.
### Returns
integer `<ret>`

0 - OK

< 0 - Invalid `<dflabel>`, or cur program is not a screen program
### Where Used
`sys.dflist_clear()` can be called from any screen program that is open. You can not call `sys.dflist_clear()` in the InitPCL.
### Example
None
### Description
`sys.dflist_clear()` clears all choices in a list type display field. The list type display fields are:

- sellist
- inplist
- chkbox
- rbgroup
### Bugs / Features / Comments
None
### See Also
- sys.dflist_add()
