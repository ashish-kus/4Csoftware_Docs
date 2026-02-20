<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.cbc_close()

### sys.cbc_close()

Purpose:

sys.cbc_close() ends the clipboard copy operation for the current type.

Usage:

\<ret\> = sys.cbc_close(\<asfile\>);

Arguments: asfile - \<asfile\> - Should be the same asfile used in the
sys.cbc_open() call.

Returns:

integer - \<ret\>

-1 - Error - illegal \<asfile\> or \<asfile\> does not match the asfile
used in the sys.cbc_open() call.

0 - OK

Where Used:

sys.cbc_close() can be called anytime while a clipboard copy operation
is open.

Example:

Description:

sys.cbc_close() ends the clipboard copy operation for the current type
and sends the data to the client. Even though the client has the data it
will not be available for pasting by the 4C Client or by any other
client application until the 4csrvr application has called
sys.cbc_end().

Bugs/Features/Comments:

See Also:

[Cut/Copy/Paste Overview](../Features/cutpaste.html)

[sys.cbc_open()](./cbcopen.html)

[sys.cbc_end()](./cbcend.html)

[sys.cbc_senddata()](./cbcsenddata.html)

[sys.cbc_sendtext()](./cbcsendtext.html)

\
\
[Back to Top](#TOPOFPAGE)
