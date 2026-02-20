---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 3
title: "sys.abort_task"
---
## sys.abort_task()
### Purpose
sys.abort_task() aborts a CISAM transaction.

### Usage
```c
ret = sys.abort_task();
```

### Arguments
None

### Returns
\<integer\> ret

0 - OK

-1 - CISAM Not Available or CISAM ERROR

For CISAM errors, a message has been displayed including the CISAM errno.

### Where Used
sys.abort_task() can be called from anywhere as long as a CISAM task is in progress.

### Example
None

### Description
sys.abort_task() aborts a CISAM transaction. `sys.abort_task()` calls `isrollback()`. You should read and understand the `isrollback()` documentation in the CISAM manuals.

### Bugs / Features / Comments
No Nested transactions.

Beware of ENORMOUS log files.

4C will eventually need to accommodate other file systems that allow transaction processing. A new more general call will probably replace `sys.abort_task()`.

### See Also
- sys.open_log()
- sys.close_log()
- sys.start_task()
- sys.end_task()
