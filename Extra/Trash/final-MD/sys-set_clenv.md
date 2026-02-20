---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 275
title: "sys.set_clenv"
---
## sys.set_clenv()
### Purpose
sys.set_clenv() allows the server to set an environment variable on the client.

### Usage
```c
sys.set_clenv(<envvar>,<envval>);
```

### Arguments
alpha `<envvar>` - The name of the environment variable.

alpha `<envval>` - The value to set the environment variable to.

### Returns
0 - Always returns 0

### Where Used
sys.set_clenv() is most useful when the you are going to have the 4cclient run another program and you need that program to have access to special info that you don't want to pass as arguments to the program.

### Example
None

### Description
sys.set_clenv() sets an environment variable in the current client process. Only the running client and any process that the client starts have access to environment variables set this way.

### Bugs / Features / Comments
None

### See Also
- sys.get_clenv()
- sys.get_env()
- sys.put_env()
