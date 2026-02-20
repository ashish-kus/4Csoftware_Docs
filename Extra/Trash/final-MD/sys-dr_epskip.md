---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 64
title: "sys.dr_epskip"
---
## sys.dr_epskip()
### Purpose
None
### Usage
```c
ret = sys.dr_epskip(<count>);
```
### Arguments
integer `<count>` - Number of lines to skip. Should be greater than 0.
### Returns
integer `<ret>`

0 - Currently this is the only return.
### Where Used
`sys.dr_epskip()` can be called only from the EndPage PCL of scrolling programs.
### Example
None
### Description
This PCL skips `<count>` lines for a scrolling program. It should only be called during the EndPage PCL processing. `sys.dr_epskip()` works like `sys.page()` except that `<count>` lines are skipped instead of doing a page break. It can be used when printing labels or when you want to do your own line counting.
### Bugs / Features / Comments
This PCL is obsolete and may be removed without notice. Instead, you should use the bootstrap fields to define the page layout, or in special cases, use the `<nskips>` arg to `sys.page()`.
### See Also
- sys.page()
