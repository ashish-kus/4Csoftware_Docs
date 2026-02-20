---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 89
title: "sys.exit_4c"
---
## sys.exit_4c()
### Purpose
sys.exit_4c() gracefully exits 4C.

### Usage
```c
sys.exit_4c(<exitcode>);
```

### Arguments
integer exitcode;  
exitcode is the exit code of 4C. If this code is non-zero, 4C will rollback any uncommitted transactions.

### Returns
There is no return from sys.exit_4c();

### Where Used
sys.exit_4c() can be called from anywhere but probably will be called from a program used to catch timeouts.

### Example
```c
sys.exit_4c(1);
```

### Description
sys.exit_4c() gracefully exits 4C. The code passed to sys.exit_4c() can be used to force commit or rollback of uncommitted transactions. This PCL was implemented so that programs used to catch timeouts could gracefully exit 4C.

### Bugs / Features / Comments
None

### See Also
- sys.exit_client()
