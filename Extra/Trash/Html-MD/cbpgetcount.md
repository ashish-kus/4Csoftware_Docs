<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.cbp_getcount()

### sys.cbp_getcount()

Purpose:

sys.cbp_getcount() returns the number of clipboard paste items
available.

Usage:

count = sys.cbp_getcount();

Arguments:

None

Returns:

-1 - No Paste Available.

\>= 0 - count of items available.

Where Used:

sys.cbp_getcount() can be called from anywhere as long as at least one
paste operation has been done by the user.

Example:

Description:

sys.cbp_getcount() returns the number of clipboard paste items
available.

Bugs/Features/Comments:

See Also:

[Cut/Copy/Paste Overview](../Features/cutpaste.html)

\
\
[Back to Top](#TOPOFPAGE)
