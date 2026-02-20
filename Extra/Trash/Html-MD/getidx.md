<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_idx()

### sys.get_idx()

Purpose:

sys.get_idx() returns the index into the user table of the current
process.

Usage:

\<useridx\> = sys.get_idx();

Arguments:

None

Returns:

integer \<useridx\> - The index into the internal user info table.

Where Used:

sys.get_idx()() can be called from anywhere.

Example:

Description:

sys.get_idx() returns the index into the internal user table for the
current 4C process.

Bugs/Features/Comments:

See Also: sys.get_maxusers() sys.get_nusers() sys.get_ttyname()
sys.get_username()

\
\
[Back to Top](#TOPOFPAGE)
