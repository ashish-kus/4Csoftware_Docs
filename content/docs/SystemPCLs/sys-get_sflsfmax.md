---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 180
title: "sys.get_sflsfmax"
---
## sys.get_sflsfmax()
### Purpose
sys.get_sflsfmax() returns the max sfl slot fault value.

### Usage
```c
sflsfmax = sys.get_sflsfmax();
```

### Arguments
None

### Returns
integer <sflsfmax> - The max number of files allocated in non-shared memory instead of shared memory because there were no available sfl slots when a file def was being read into shared memory.

### Where Used
sys.get_sflsfmax() can be called from anywhere. It is used in the system program sys.mem.summary to help in configuring the system.  
sys.get_sflsfmax() is meant for INTERNAL USE ONLY.

### Example
The following stmt is the StFld PCL for sflsfmax in the program sys.mem.summary.  
```c
sflsfmax = sys.get_sflsfmax();
```

### Description
sys.get_sflsfmax() returns the max sfl slot fault value. This is the maximum number of files allocated in non-shared memory instead of shared memory at one time because no sfl slot was available when a file needed it. sfl stands for an internal structure named sys_file.

### Bugs / Features / Comments
If when running the sys.mem.summary program you usually have File Slot Faults, you probably need to increase the number of files specified in the XLCONFIG file.

### See Also
- sys.get_sflmfmax()
- sys.get_spmfmax()
- sys.get_spsfmax()
