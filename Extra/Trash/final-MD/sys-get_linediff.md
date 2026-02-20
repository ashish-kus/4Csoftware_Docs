---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 162
title: "sys.get_linediff"
---
## sys.get_linediff()
### Purpose
`sys.get_linediff()` returns the number of lines printed by nested programs since the last field printed by the current program.

### Usage
```c
ldiff = sys.get_linediff();
```

### Arguments
None

### Returns
`>= 0` - number of lines printed by other programs since last field printed by this program.

There are no error returns.

### Where Used
`sys.get_linediff()` can be called from rpt programs after pushing another program, but before printing another field.

### Example
```c
/*
     Print details if any
*/
sys.push_prog("print.detail");
/*
     Skip past nested progs and leave one blank line
     If nothing was printed by "print.detail", then
     no call to sys.skip() is made.
*/
if ((ldiff = sys.get_linediff()) > 0)
     sys.skip(ldiff + 1);
```

### Description
`sys.get_linediff()` returns to the user program the number of lines printed by all nested programs since the last field was printed by the current program. If a page boundary is crossed, it is reflected in the return of `sys.get_linediff()`. 

`sys.get_linediff()` is meant to be called by scrolling programs after calling other printing programs in order to determine the number of lines that need to be skipped before printing the next iteration. 

It makes no sense to call `sys.get_linediff()` from a non-scrolling program or from any non-printing program.

### Bugs / Features / Comments
None

### See Also
- sys.page()
- sys.skip()
- sys.end_page()
- sys.exit_page()
- sys.page_isfull()
- sys.get_pagediff()
- sys.is_tof()
