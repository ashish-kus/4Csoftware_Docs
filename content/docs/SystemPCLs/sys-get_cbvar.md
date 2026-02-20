---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 122
title: "sys.get_cbvar"
---
## sys.get_cbvar()
### Purpose
sys.get_cbvar() returns the name of the variable that triggered the CB.

### Usage
```c
<alphavar> = sys.get_cbvar();
```

### Arguments
None

### Returns
```c
<varname> - Normal - <varname> triggered CB

"BOF" - BOF triggered CB

"EOF" - EOF triggered CB

"" - No current CB
```

### Where Used
sys.get_cbvar() can be called from any of the Start or End Group CB PCLS, and from the CBEOF or CBBOF PCLs.

### Example
```c
if (sys.get_cbvar() == "sys.pr_name") sys.exit_cb(); /* Stop processing for this CB */
```

### Description
sys.get_cbvar() returns the name of the CB VAR that triggered the CB. It can be used to do special processing based on the variable that triggered the CB.

### Bugs / Features / Comments
None

### See Also
- sys.exit_cb()
