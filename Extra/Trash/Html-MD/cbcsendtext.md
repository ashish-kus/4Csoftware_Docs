<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.cbc_sendtext()

### sys.cbc_sendtext()

Purpose:

sys.cbc_sendtext() adds 1 text item to the 4C clipboard.

Usage:

\<ret\> = sys.cbc_sendtext(\<text\>);

Arguments:

alpha \<text\> - The text to copy.

Returns:

integer \<ret\>

-1 - Error - Either sys.cbc_open() has not been called, or the current
type is not CBC_TEXT.

0 - OK

Where Used:

sys.cbc_sendtext() can be called only between the corresponding
sys.cbc_open() and sys.cbc_close() calls and only if the \<type\>
specified in the sys.cbc_open() call is CBC_TEXT.

Example:

Description:

sys.cbc_sendtext() adds 1 text item to the 4C clipboard.

Bugs/Features/Comments:

See Also:

[Cut/Copy/Paste Overview](../Features/cutpaste.html)

[sys.cbc_senddata()](./cbcsenddata.html)

\
\
[Back to Top](#TOPOFPAGE)
