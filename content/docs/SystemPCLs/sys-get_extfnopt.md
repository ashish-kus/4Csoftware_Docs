---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 139
title: "sys.get_extfnopt"
---
## sys.get_extfnopt()
### Purpose
`sys.get_extfnopt()` allows the application to get information about a 4C External Library including last error information.

### Usage
```c
optval = sys.get_extfnopt(<extlibname>,<optname>);
```

### Arguments
- `<extlibname>` - The name of the library.
- `<optname>` - The name of the option.

### Returns
- `<optval>` - The value to of the option.

### Where Used
`sys.get_extfnopt()` can be called from any 4C program that uses that library.

### Example
```c
msg = sys.get_extfnopt("FCCom","LastMessage");
```

### Description
`sys.get_extfnopt()` allows the application to get information about a particular library including last error and message information.

- MessageLevel - The Message reporting level the library uses for the current 4C program.
- LastError - The error number returned by the last function call into this library for the current 4C program.
- LastMessage - The message, error or info, reported by last function call into this library.

### Bugs / Features / Comments
None

### See Also
- sys.set_extfnopt()
- Sys PCLs List
