---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 40
title: "sys.close_log"
---
## sys.close_log()
### Purpose
sys.close_log() closes the CISAM log file.

### Usage
```c
ret = sys.close_log();
```

### Arguments
None

### Returns
Always returns 0.

### Where Used
sys.close_log() can be called from anywhere.

### Example
None

### Description
See your CISAM documentation for detailed description of the CISAM logfile.

### Bugs / Features / Comments
As other databases are added to 4C this call will probably be changed or another added to account for differences in the databases and to make the 4C programs transparent to them.

### See Also
- sys.open_log()
- sys.start_task()
- sys.end_task()
- sys.abort_task()
