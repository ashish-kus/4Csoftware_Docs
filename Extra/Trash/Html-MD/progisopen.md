<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.prog_isopen()

### sys.prog_isopen()

Purpose:

sys.prog_isopen() returns 1 if the current program is open.

Usage:

ret = sys.prog_isopen();

Arguments:

arg1

Returns:

0 - Program is not open

1 - Program is open

Where Used:

sys.prog_isopen() can be called from anywhere.

Example:

Description:

sys.prog_isopen() is an easy way to determine if a screen program has a
client window currently display or if a report program has a device
open. This can be useful because some system PCLs only work when a
program is open. i.e. sys.dflist_clear(), sys.dflist_add(), and others.

Requirements

4csrvr version 6.4.3 or later

Bugs/Features/Comments:

Bugs

See Also: See Also

[Sys PCLs List](./index.html)

\
\
[Back to Top](#TOPOFPAGE)
