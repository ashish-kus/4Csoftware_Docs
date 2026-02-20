---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 99
title: "sys.field_wasinp"
---
## sys.field_wasinp()
### Purpose
`sys.field_wasinp()` indicates whether the current field allowed input from the user or not.

### Usage
```c
if (sys.field_wasinp()) dosomething();
```

### Arguments
None

### Returns
0 - Current field did not allow input for some reason.  
This could be because `sys.end_field()` was called from the FldSfld PCL, the field is display only, Accept was entered on a field preceding this field, Ftab was entered on a field preceding this field, or a scrolling program is in column modify mode on a different field.

1 - The current field allowed input  
This does not necessarily mean that anything was input, only that the user was prompted for input. The user could have entered `<CR>` only and the return will still be 1.

-1 - There is no current field.

### Where Used
`sys.field_wasinp()` can be called only during FIELD processing.

### Example
```c
/*
     This is an example from the bootstrap
     program sys.df.maint1
     

     End field PCL for sys.df_litflag
     

     If no input was allowed on this field,
     do not push the lit maint program
*/
if (sys.field_wasinp() == 0)
     return;

sys.push_prog("sys.dflit.maint");
```

### Description
`sys.field_wasinp()` allows the user program to determine if the current field allowed input or not. Mainly it is used to know whether a field did not allow input because of forward tabbing, column modify mode, or end of data. It is useful in determining whether other programs should be pushed or not.  
It should only be called from the FldEfld PCL of any field.  
`sys.field_wasinp()` does not indicate what the user may have input, only that input was allowed. The user could have entered `<CR>` or a function key, and the return will still be 1.

### Bugs / Features / Comments
None

### See Also
- sys.end_field()
- sys.exit_field()
- sys.stop_tab()
