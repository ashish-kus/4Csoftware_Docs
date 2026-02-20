---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 229
title: "sys.err_msg"
---
## sys.err_msg()
### Purpose
sys.err_msg() - Displays an status message

### Usage
```c
sys.msg([Arg1-Arg15]);
```

### Arguments
AnyType - arg1,arg2,...,arg15 - The parts of the msg

### Returns
None

### Where Used
sys.msg() can be called from anywhere.

### Example
```c
sys.msg("Processing...",sys.pr_name);
```

### Description
sys.msg() displays a message on in the status area and does not wait for any user response.

Requirements

4CServer version 5.0.6-05 or higher is required for using non alpha arguments

### Bugs / Features / Comments
sys.msg() is obsolete. Use sys.message() instead.

### See Also
- sys.message()
- sys.err_msg()
