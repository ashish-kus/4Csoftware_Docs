---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 96
title: "sys.exit_prog"
---
## sys.exit_prog()
### Purpose
sys.exit_prog() exits the current program.

### Usage
```c
sys.exit_prog(<exitcode>);
```

### Arguments
integer <exitcode> - The value to set into $wexit_code

### Returns
No Returns

### Where Used
sys.exit_prog() can be called from anywhere.

### Example
None

### Description
sys.exit_prog() ends all processing in the current program, and sets $wexit_code to <exitcode>

### Bugs / Features / Comments
None

### See Also
- sys.end_prog()
