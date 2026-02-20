<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_datetype()

### sys.get_datetype()

Purpose:

sys.get_datetype() returns the current input date format.

Usage:

datetype = sys.get_datetype();

Arguments:

None

Returns:

alpha \<datetype\>

"AMERICAN" - Current date input format is American.

"EUROPEAN" - Current date input format is European.

Where Used:

sys.get_datetype() can be called from anywhere.

Example:

Description:

sys.get_datetype() returns the current input date format. The type
returned is either "AMERICAN" or "EUROPEAN".

Bugs/Features/Comments:

See Also: sys.set_datetype()

\
\
[Back to Top](#TOPOFPAGE)
