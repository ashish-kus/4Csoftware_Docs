<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_fltype()

### sys.get_fltype()

Purpose:

sys.get_fltype() returns the current fld loop type

Usage:

fltype = sys.get_fltype();

Arguments:

Returns:

integer \<fltype\> - One of

- FLTYPE_MAIN
- FLTYPE_DRIVER
- FLTYPE_INIT
- FLTYPE_OPTION
- FLTYPE_NONE

Where Used:

sys.get_fltype() can be called from anywhere.

Example:

The 4cSys sys.pr.srch.1 program calls sys.get_fltype() when in the
refresh() PCL in order to determine if it is in the initial option
panel. If it is in the initial option panel, it will call
sys.end_fldloop() otherwise it calls sys.dr_restart().

Description:

When using option panels it sometimes is important to be able to know
what type of fld loop was being processed when some event occurs like
the user clickin a command button.

Requirements

4csrvr version 5.2 or later.

Bugs/Features/Comments:

See Also:

[Sys PCLs List](./index.html)

\
\
[Back to Top](#TOPOFPAGE)
