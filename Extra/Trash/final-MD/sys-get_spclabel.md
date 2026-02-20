---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 182
title: "sys.get_spclabel"
---
## sys.get_spclabel()
### Purpose
sys.get_spclabel() returns the current value of a label for a 4C function key.

### Usage
```c
spclabel = sys.get_spclabel(<spcname>);
```

### Arguments
alpha `<spcname>` - The name of the spc to get the label for. This will be a key to the file sys.spc_char.

### Returns
<alpha> spclabel - The value of the label for `<spcname>`. This will be blank if an illegal `<spcname>` is specified.

### Where Used
sys.get_spclabel() can be called from anywhere. It normally would be called so that you can indicate to the user what function key to press.

### Example
The following is from the slp() PCL of sys.spc.set.
```c
spcstring = sys.get_spcstr(sys.spc_name);
spclabel = sys.get_spclabel(sys.spc_name);
spcalt = sys.get_spcalt(sys.spc_name);
ok = ''
```

### Description
sys.get_spclabel() returns the label of a 4C function key.

### Bugs / Features / Comments
None

### See Also
- sys.set_spcstr()
- sys.set_spclabel()
- sys.set_spcalt()
- sys.get_spcstr()
- sys.get_spclabel()
- sys.get_spcalt()
