<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.cbp_gettype()

### sys.cbp_gettype()

Purpose:

sys.cbp_gettype() returns the type of clipboard paste available.

Usage:

type = sys.cbp_gettype();

Arguments:

None

Returns:

"" - No Paste Available.

"Text" - Text paste available

filename - 4C format paste is available using format of filename.

Where Used:

sys.cbp_gettype() can be called from anywhere as long as at least one
paste operation has been done by the user.

Example:

Description:

sys.cbp_gettype() returns the type of clipboard paste available. The
type of a paste is either "Text" or a 4C filename. The type returned
when the data in the clipboard is not from a 4C application will always
be "Text"

Bugs/Features/Comments:

See Also:

[Cut/Copy/Paste Overview](../Features/cutpaste.html)

\
\
[Back to Top](#TOPOFPAGE)
