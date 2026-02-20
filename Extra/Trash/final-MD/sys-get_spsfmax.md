---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 185
title: "sys.get_spsfmax"
---
## sys.get_spsfmax()
### Purpose
sys.get_spsfmax() returns the max sp slot fault value.

### Usage
```c
spsfmax = sys.get_spsfmax();
```

### Arguments
None

### Returns
integer <spsfmax> - The max number of programs allocated in non-shared memory instead of shared memory because there were no available sp slots when a program was being read into shared memory.

### Where Used
sys.get_spsfmax() can be called from anywhere. It is used in the system program sys.mem.summary to help in configuring the system.  
sys.get_spsfmax() is meant for INTERNAL USE ONLY.

### Example
The following stmt is the StFld PCL for spsfmax in the program sys.mem.summary.  
```c
spsfmax = sys.get_spsfmax();
```

### Description
sys.get_spsfmax() returns the max sp slot fault value. This is the maximum number of programs allocated in non-shared memory instead of shared memory at one time because no sp slot was available when a program needed it. sp stands for an internal structure named sys_prog.

### Bugs / Features / Comments
If when running the sys.mem.summary program you usually have Program Slot Faults, you probably need to increase the number of programs specified in the XLCONFIG file.

### See Also
- sys.get_sflmfmax()
- sys.get_sflsfmax()
- sys.get_spmfmax()
