---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 311
title: "sys.set_spcalt"
---
## sys.set_spcalt()
### Purpose
sys.set_spcalt() allows a program to change the alternate escape sequence that 4C expects for a function key.

### Usage
```c
ret = sys.set_spcalt(<spcname>,<value>);
```

### Arguments
alpha `<spcname>` - The name of the spc to set the alt sequence for. This will be a key to the file sys.spc_char.

alpha `<value>` - The new alt sequence that this spc has. Characters preceded by a '\\ or a '^' are treated as control characters and are converted first.

### Returns
integer `<ret>`

0 - OK

-1 - Probably an illegal `<spcname>`

### Where Used
sys.set_spcalt() can be called from anywhere. It normally would be called from a program that remaps the function keys to a particular users liking.

### Example
The sys.spc.set program has the following code in the elp() PCL.
```c
if (spcalt)
    sys.set_spcalt(sys.spc_name,spcalt);
```

### Description
sys.set_spcalt() changes the alternate escape sequence that 4C is expecting for a particular function key, such as the `<accept>` key.

### Bugs / Features / Comments
None

### See Also
- sys.set_spcstr()
- sys.set_spclabel()
- sys.get_spcstr()
- sys.get_spclabel()
- sys.get_spcalt()
