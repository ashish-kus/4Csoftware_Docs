---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 249
title: "sys.put_env"
---
## sys.put_env()
### Purpose
sys.put_env() sets an environment variable.

### Usage
```c
<ret> = sys.put_env(<ENVVAR>,<value>);
```

### Arguments
alpha `<ENVVAR>` - the name of the environment variable.

alpha `<value>` - The new value for the environment variable.

### Returns
integer `<ret>`

0 - normal return

-1 - Error setting the value

### Where Used
sys.put_env() can be called from anywhere.

### Example
None

### Description
sys.put_env() is used to modify environment variables. The variables modified will be accessible to any external programs called outside of 4C. If you modify XLDATA, then it affects any subsequent opens of files. If you modify XLPROG, then it affects any subsequent program calls. Modifying XLSYSTEM is not recommended.

### Bugs / Features / Comments
None

### See Also
- sys.get_env()
- sys.get_clenv()
