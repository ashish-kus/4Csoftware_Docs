<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_keystate()

### sys.get_keystate()

Purpose:

sys.get_keystate() lets the application determine if any of Shift,
Control, or Alt was pressed when the user clicked a button or listview
column hdr.

Usage:

if (sys.get_keystate(\<key\>)) do_something();

Arguments:

Alpha - \<key\> - Should be one of "Shift", "Control" or "Alt"

Returns:

0 - Specified key was not pressed

1 - Specified key was pressed

Where Used:

sys.get_keystate() can be called from anywhere.

Example:

The global 4cSys PCL lv_sortby() checks if either Shift or Control is
pressed and if so will sort descending instead of ascending.

Description:

Long Description

Requirements

4csrvr version 5.0.6 and higher

4cclient version 5.0.6 and higher

Bugs/Features/Comments:

See Also:

[Sys PCLs List](./index.html)

\
\
[Back to Top](#TOPOFPAGE)
