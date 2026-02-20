---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 312
title: "sys.set_spclabel"
---
## sys.set_spclabel()
### Purpose
sys.set_spclabel() allows a program to change the value of a function key label at run time.

### Usage
```c
ret = sys.set_spclabel(<spcname>,<label>);
```

### Arguments
alpha `<spcname>` - The name of the spc to set the label for. This will be a key to the file sys.spc_char.

alpha `<label>` - The new label that this spc has.

### Returns
integer `<ret>`

0 - OK

-1 - Probably an illegal `<spcname>`

### Where Used
sys.set_spclabel() can be called from anywhere. It normally would be called from a program that remaps the function keys to a particular users liking.

### Example
The sys.spc.ex1 program has the following code in the elp() PCL.
```c
if (spcstring[12]) {
    sys.set_spcstr("user13",spcstring[12]);
    sys.set_spclabel("user13","F11");
}
```

### Description
sys.set_spclabel() changes the label that 4C associates with a particular function key, such as the `<accept>` key.

### Bugs / Features / Comments
None

### See Also
- sys.set_spcstr()
- sys.set_spclabel()
- sys.set_spcalt()
- sys.get_spcstr()
- sys.get_spclabel()
- sys.get_spcalt()
