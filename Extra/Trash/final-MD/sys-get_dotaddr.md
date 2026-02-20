---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 136
title: "sys.get_dotaddr"
---
## sys.get_dotaddr()
### Purpose
sys.get_dotaddr() returns the dot address of a client program in nnn.nnn.nnn.nnn format.

### Usage
```c
dotaddr = sys.get_dotaddr(idx);
```

### Arguments
integer <idx> - The zero based index of the client program.

### Returns
alpha <dotaddr> - The dot address of the client program in nnn.nnn.nnn.nnn format.

### Where Used
sys.get_dotaddr() can be called from anywhere. One place you may want to use it is in order to get the dotaddr to use in `sys.send_msg()` calls.

### Example
```c
dotaddr = sys.get_dotaddr(0);
```

### Description
sys.get_dotaddr() returns the dot address of a client program in nnn.nnn.nnn.nnn format. This can be used for any client, not just the client connected to this 4csrvr. The dot address of the current client is more easily gotten using the system variable `sys.cl_dotaddr`.

### Bugs / Features / Comments
None

### See Also
- sys.get_idx()
- sys.get_maxusers()
- sys.get_nusers()
