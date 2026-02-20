<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.dev_nlines()

### sys.dev_nlines()

Purpose:

sys.dev_nlines() returns the number of lines on the current output
device.

Usage:

nlines = sys.dev_nlines();

Arguments:

None

Returns:

integer nlines - The number of lines on the current output device.

Where Used:

sys.dev_nlines() can be called from anywhere, but you should be careful
if it is called from the Init, End, or Exit PCLs.

Example:

Description:

sys.dev_nlines() returns the number of lines on the current output
device. The current output device may not be same device as that
specified by the program. This is possible if sys.dev_nlines() is called
from the Init PCL, and the calling program is not using the same device.
In this case sys.dev_nlines() would return the number of lines for the
calling programs output device.

Bugs/Features/Comments:

See Also:

[sys.get_msgline1()](./getmsgline1.html)

[sys.get_msgline2()](./getmsgline2.html)

\
\
[Back to Top](#TOPOFPAGE)
