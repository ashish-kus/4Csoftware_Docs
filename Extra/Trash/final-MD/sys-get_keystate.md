---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 160
title: "sys.get_keystate"
---
## sys.get_keystate()
### Purpose
sys.get_keystate() lets the application determine if any of Shift, Control, or Alt was pressed when the user clicked a button or listview column hdr.

### Usage
```c
if (sys.get_keystate(<key>)) do_something();
```

### Arguments
Alpha - `<key>` - Should be one of "Shift", "Control" or "Alt"

### Returns
0 - Specified key was not pressed

1 - Specified key was pressed

### Where Used
sys.get_keystate() can be called from anywhere.

### Example
The global 4cSys PCL lv_sortby() checks if either Shift or Control is pressed and if so will sort descending instead of ascending.

### Description
Long Description

Requirements

4csrvr version 5.0.6 and higher

4cclient version 5.0.6 and higher

### Bugs / Features / Comments
None

### See Also
- Sys PCLs List
