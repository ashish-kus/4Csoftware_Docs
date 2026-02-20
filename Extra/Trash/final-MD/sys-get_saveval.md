---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 178
title: "sys.get_saveval"
---
## sys.get_saveval()
### Purpose
sys.get_saveval() returns a single saved variable

### Usage
```c
ret = sys.get_saveval([ <name>, ] <var>);
```

### Arguments
- alpha `<name>` - An optional name that identifies a previous save.
- var - `<var>` - A 4C variable of any type

### Returns
Return depends on saved variable type.

### Where Used
sys.get_saveval() can be called from anywhere.

### Example
None

### Description
sys.get_saveval() will return the saved value of a variable that was saved using `sys.fl_save()`. It does not store into the variable itself, rather it stores into `<ret>`. This makes it easier to compare save values with current values. You can of course store into the variable itself explicitly.

### Bugs / Features / Comments
The only way to verify that there was no error is to check that `sys_ret` is equal to `SYSRET_OK`.

Assigning a saved variable to an incompatible variable (i.e. integer to alpha) is not flagged as an error.

### See Also
- sys.fl_save()
- sys.restore_share()
- sys.fl_restore()
