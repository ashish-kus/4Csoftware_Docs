---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 138
title: "sys.get_env"
---
## sys.get_env()
### Purpose
sys.get_env() returns the value of an environment variable.

### Usage
\<avar\> = `sys.get_env`(\<ENVVAR\>);

### Arguments
alpha \<ENVVAR\> - the name of the environment variable.

### Returns
alpha \<avar\> - The value of the env var.

NULL alpha - no value defined for this env var.

There are no error returns.

### Where Used
sys.get_env() can be called from anywhere. It can be used to determine different programs to run based on site env vars.

### Example
The following example is from the system program "sh". `sys.get_env()` is used to determine which shell to run.

```c
/*
    start the shell
*/
if ((prog = `sys.get_env`("SHELL")) == "")
    prog = "/bin/sh";
`sys.msg`(""); /* Force Flush of Output */
`sys.make_task`(prog); /* Can't use sh() because of PCL name conflict */
`sys.exit_prog`(0);
```

### Description
Return the value of an environment variable. It can be used to decide one of several programs to run that may be different at different sites. If used too much in this way, the programs will become difficult to maintain.

### Bugs / Features / Comments
None

### See Also
- sys.get_clenv()
- sys.put_env()
