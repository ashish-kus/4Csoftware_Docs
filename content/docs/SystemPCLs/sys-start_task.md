---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 330
title: "sys.start_task"
---
## sys.start_task()
### Purpose
sys.start_task() starts a CISAM transaction.

### Usage
```c
ret = sys.start_task();
```

### Arguments
None

### Returns
\<integer\> ret

0 - OK

-1 - CISAM Not Available or CISAM ERROR

For CISAM errors, a message has been displayed including the CISAM errno.

### Where Used
sys.start_task() can be called from anywhere, but its usage will need to coincide with logical transactions.

### Example
None

### Description
sys.start_task() starts a CISAM transaction. If you have already started a transaction and have not called `sys.end_task()`, then CISAM will abort the transaction in progress and start a new one. `sys.start_task()` calls `isbegin()`. You should read and understand the `isbegin()` documentation in the CISAM manuals.

### Bugs / Features / Comments
No Nested transactions.

Beware of ENORMOUS log files.

4C will eventually need to accommodate other file systems that allow transaction processing. A new more general call will probably replace `sys.start_task()`.

### See Also
- sys.open_log()
- sys.close_log()
- sys.end_task()
- sys.abort_task()
