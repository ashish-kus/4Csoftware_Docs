---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 200
title: "sys.is_clsrvr"
---
## sys.is_clsrvr()
### Purpose
sys.is_clsrvr() returns 1 if 4c is client/server 4c.

### Usage
```c
ret = sys.is_clsrvr();
```

### Arguments
None

### Returns
0 - Not running Client/Server 4c

1 - Running Client/Server 4c

### Where Used
sys.is_clsrvr() can be called from anywhere.

### Example
```c
if (sys.is_clsrvr()) dosomething(); else dosomethingelse();
```

### Description
sys.is_clsrvr() is meant to allow you to distinguish between character4c and client/srvr 4c while your application is running.

### Bugs / Features / Comments
This is not available in older character versions of 4c.

### See Also
- sys.cbp_exit()
- sys.char_val()
