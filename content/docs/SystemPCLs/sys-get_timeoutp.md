---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 187
title: "sys.get_timeoutp"
---
## sys.get_timeoutp()
### Purpose
`sys.get_timeoutp()` returns the timeout prog and its arguments for any server/client program/session timeout.

### Usage
```c
oldtimeoutp = sys.get_timeoutp(TIMEOUT_TYPE);
```

### Arguments
`TIMEOUT_TYPE` must be one of

- TO_SVGLOBAL - Server Session Timeout.
- TO_SVPROGRAM - Server Program Timeout
- TO_CLGLOBAL - Client Session Timeout
- TO_CLPROGRAM - Client Program Timeout.

### Returns
Blank - there is no timeoutprog or no timeout defined for `TIMEOUT_TYPE`.

NonBlank - The program and args associated with `TIMEOUT_TYPE`.

### Where Used
`sys.get_timeoutp()` can be called from anywhere. However it will normally be called by a timeout processing program that wants to disable a timeout in the InitPCL and reenable it in the ExitPCL.

### Example
The demo programs that catch timeouts have examples. See:

- demo.main.s
- lockscreen.s

### Description
`sys.get_timeoutp()` returns the timeout prog and its arguments for either a program or a session timeout.

### Bugs / Features / Comments
None

### See Also
- sys.set_timeout()
- sys.get_timeoutv()
- sys.set_alarm()
- sys.lock_clientws()
- sys.exit_client()
- sys.exit_4c()
