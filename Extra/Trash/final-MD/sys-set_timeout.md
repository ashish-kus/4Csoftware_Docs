---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 314
title: "sys.set_timeout"
---
## sys.set_timeout()
### Purpose
sys.set_timeout() sets either a program or session timeout.

### Usage
```c
sys.set_timeout(TIMEOUT_TYPE,<timeoutval>,[<timeoutprog>]);
```

### Arguments
TIMEOUT_TYPE must be one of:

- TO_SVGLOBAL - Server Session Timeout.
- TO_SVPROGRAM - Server Program Timeout
- TO_CLGLOBAL - Client Session Timeout
- TO_CLPROGRAM - Client Program Timeout.

integer `<timeoutval>`
`<timeoutval>` is the number of seconds to wait for user input before the timeout is triggered.

alpha `<timeoutprog>`
`<timeoutprog>` is an optional argument specifying program name and arguments separated by colons. The timeoutprog will be called when the timeout is triggered.

### Returns
There is no return value for this SysPcl.

### Where Used
sys.set_timeout() can be called from anywhere. More than likely though, it will be called from the InitPCL of a program that needs to set timeouts.

### Example
The demo programs that catch timeouts have examples. See:

- demo.main.s
- locksreen.s

### Description
sys.set_timeout() allows setting of a server program and session timeouts as well as client program and session timeouts dynamically. For a server session timeout, if no timeout prog is specified, then the 4csrvr will exit after killing all 4c programs. For client session timeout, if no timeout prog is specified, the 4C client will exit, but the 4csrvr will not immediately exit. For a server program or a client program timeout, if no timeout program is specified, the program will exit with a -4 code when the timeout is reached. To disable a timeout, use a timeoutval of 0.

### Bugs / Features / Comments
TIMEOUT_GLOBAL can be used interchangeably with TO_SVGLOBAL and TIMEOUT_PROGRAM can be used interchangeably with TO_SVPROGRAM. Newer programs should use TO_SVGLOBAL and TO_SVPROGRAM. If a program is used to catch a timeout, it may be necessary to disable further timeouts until the program exits.

### See Also
- sys.set_alarm()
- sys.get_timeoutp()
- sys.get_timeoutv()
- sys.lock_clientws()
- sys.exit_client()
- sys.exit_4c()
