---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 42
title: "sys.cl_restart"
---
## sys.cl_restart()
### Purpose
`sys.cl_restart()` restarts the client.

### Usage
```c
ret = sys.cl_restart([<argstring>])
```

### Arguments
alpha `<argstring>` - If specified, these arguments replace the original arguments to the 4c client.

### Returns
-1 - Client version is earlier than 4.4.4

Otherwise there will be no return, the 4csrvr process will exit.

### Where Used
`sys.cl_restart()` should only be used in rare circumstances. Possibly, when updating a client preference that requires a restart.

### Example
None

### Description
`sys.cl_restart()` causes the interactive 4c client to terminate and start another session. The new session will be started with the same arguments as the original session unless you specify a new `<argstring>`.

### Bugs / Features / Comments
`sys.cl_restart()` is not supported by the non interactive 4C client, 4ccl.

### See Also
- sys.set_clpref()
- sys.exit_4c()
