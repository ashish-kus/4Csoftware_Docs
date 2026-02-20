<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.cbp_getnflds()

### sys.cbp_getnflds()

Purpose:

sys.cbp_getnflds() returns the number of flds in the current clipboard
paste operation.

Usage:

nflds = sys.cbp_getnflds();

Arguments:

None

Returns:

-1 - No Paste Available.

\>= 0 - Number of flds in each clipboard paste item.

Where Used:

sys.cbp_getnflds() can be called from anywhere as long as at least one
paste operation has been done by the user.

Example:

Description:

sys.cbp_getnflds() returns the number of flds in the current clipboard
paste operation. If the format is a 4C clipboard format, then the number
of fields will is the number of fields defined in the 4c file definition
used as the template. If the format is a text format paste, then the
number of fields will be one.

Bugs/Features/Comments:

See Also:

[Cut/Copy/Paste Overview](../Features/cutpaste.html)

\
\
[Back to Top](#TOPOFPAGE)
