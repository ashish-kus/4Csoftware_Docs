---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 181
title: "sys.get_spcalt"
---
## sys.get_spcalt()
### Purpose
`sys.get_spcalt()` returns the alternate value of a 4C function key.

### Usage
```c
spcalt = sys.get_spcalt(<spcname>);
```

### Arguments
None

### Returns
`<alpha> spcalt` - The alternate value of the spc for `<spcname>`. This will be blank if an illegal `<spcname>` is specified. Any control characters are converted to a displayable format.

### Where Used
`sys.get_spcalt()` can be called from anywhere. It normally would be called from a program that remaps the function keys to a particular users liking.

### Example
The following is from the `slp()` PCL of `sys.spc.set`.
```c
spcstring = sys.get_spcstr(sys.spc_name);
spclabel = sys.get_spclabel(sys.spc_name);
spcalt = sys.get_spcalt(sys.spc_name);
ok = ''
```

### Description
`sys.get_spcalt()` returns the alternate value of a 4C function key. The alternate value is normally an escape sequence that the user types in order to trigger a 4C function key. The 4C function key is triggered whenever 4C recognizes the `spcstring` sequence or the `spcalt` sequence in the input stream.

### Bugs / Features / Comments
None

### See Also
- sys.set_spcstr()
- sys.set_spclabel()
- sys.set_spcalt()
- sys.get_spcstr()
- sys.get_spclabel()
- sys.get_spcalt()
