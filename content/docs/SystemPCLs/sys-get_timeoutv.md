---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 188
title: "sys.get_timeoutv"
---
## sys.get_timeoutv()
### Purpose
sys.get_timeoutv() returns the timeout value for any server/client session/program timeout.

### Usage
oldtimeoutv = sys.get_timeoutv(TIMEOUT_TYPE);

### Arguments
TIMEOUT_TYPE must be one of

- TO_SVGLOBAL - Server Session Timeout.
- TO_SVPROGRAM - Server Program Timeout
- TO_CLGLOBAL - Client Session Timeout
- TO_CLPROGRAM - Client Program Timeout.

### Returns
0 - there is no timeout defined for TIMEOUT_TYPE.

> 0 - The #seconds associated with TIMEOUT_TYPE.

### Where Used
sys.get_timeoutv() can be called from anywhere.

### Example
The demo programs that catch timeouts have examples. See:

- demo.main.s
- lockscreen.s

### Description
sys.get_timeoutv() returns the #seconds for the specified timeout type.

### Bugs / Features / Comments
None

### See Also
- sys.set_timeout()
- sys.get_timeoutp()
- sys.set_alarm()
- sys.lock_clientws()
- sys.exit_client()
- sys.exit_4c()
