---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 235
title: "sys.open_log"
---
## sys.open_log()
### Purpose
sys.open_log() opens a CISAM log file.

### Usage
```c
ret = sys.open_log(<logname>);
```

### Arguments
alpha \<logname\> - a valid CISAM log file name.

### Returns
0 - OK

-1 - Either CISAM not available, or CISAM error and message displayed, or log file already open - message displayed also.

### Where Used
sys.open_log() can be called from anywhere.

### Example
None

### Description
sys.open_log() opens a CISAM log file. The log file remains open until a call to `sys.close_log()`, or until the 4C session terminates. This call, as well as the task start, task end, and task abort calls were added to allow the CISAM users to take advantage of what CISAM offers in terms of transaction processing. See your CISAM manual to find out what all this means. The logfile can also be opened at the start of the 4C session by specifying the CILogFile in the XLCONFIG file.

### Bugs / Features / Comments
It only works with CISAM, but as other databases are added it will be extended to include them. This may mean a change in calling sequence.

### See Also
- sys.close_log()
- sys.start_task()
- sys.end_task()
- sys.abort_task()
