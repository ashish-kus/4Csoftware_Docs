---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 174
title: "sys.get_progname"
---
## sys.get_progname()
### Purpose
sys.get_progname() returns the real program name for the asprog arg.

### Usage
```c
progname = sys.get_progname(<asprog>);
```

### Arguments
asprog <asprog> - The asprog name of the 4C program that you want the real program name of.

### Returns
NULLSTRING - No such <asprog> currently active

<progname> - The real program name of <asprog>

### Where Used
sys.get_progname() can be called from anywhere. However, it is normally only used in the 4C debugger programs.

### Example
The following example is from the 4C debugger program sys.dbg.fld. It is the aspefld PCL. It is used in order to display the real program name along with the asprog name on the screen.
```c
if (sys.is_prog(asprog) == 0) {
    sys.err_msg("No Such Program:",asprog);
    sys.exit_field(sys.cur_field);
}
progname = sys.get_progname(asprog);
```

### Description
sys.get_progname() returns the real program name for the asprog arg. It is probably not real useful to normal programs, but debugger type programs will have a use for it. It was added so that the 4C debugger programs could call it when the asprog name was known in order to display the real program name.

### Bugs / Features / Comments
If more than one program is active with the same asprog name, only the most recently active one is used by sys.build_stlist().

### See Also
- sys.is_prog()
