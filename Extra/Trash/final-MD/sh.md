---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 316
title: "sh"
---
## sh()
### Purpose
sh() starts a copy of the shell to run a command.

### Usage
ret = sh(<cmd>); or\
ret = sh();

### Arguments
<cmd> - The cmd to run, including all arguments. The arguments and the command name must be separated by spaces.

The <cmd> argument is optional, and if not used, an interactive copy of the shell is started. This can be useful for a menu entry.

### Returns
0 - 255 - The exit status of the shell.

-1 - Error starting shell or shell terminated with a signal.

### Where Used
sh() can be called from anywhere.

### Example
```c
cmd = "xled sys.pcl_stmt " + sys.ph_prname + ' ' + sys.ph_pclname;
sh(cmd);
```

### Description
sh() starts a copy of the shell to run a command. If arguments are passed to sh(), they are assumed to make up a command. The shell will be started with the '-c' option, passing all arguments to the shell to parse. If no arguments are passed to sh(), then an interactive copy of the shell is started. Which shell is used depends on the environment variable 'SHELL'. If not set, then '/bin/sh' is started. It is better to use sh() to run a command than sys.make_task() because you do not need to know the absolute path name of the command to run. The shell will use the 'PATH' environment variable.

### Bugs / Features / Comments
None

### See Also
- lsh()
