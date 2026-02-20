<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.cbc_senddata()

### sys.cbc_senddata()

Purpose:

sys.cbc_senddata() adds 1 data item to the 4C clipboard.

Usage:

\<ret\> = sys.cbc_senddata(\<asfile\>);

Arguments:

asfile \<asfile\> - The 4C asfile that holds the data to be copied.

Returns:

integer \<ret\>

-1 - Error - Either sys.cbc_open() has not been called, illegal asfile,
or, in the case of CBC_4CTYPE copy, the filename of \<asfile\> does not
match the filename of the \<asfile\> used in the sys.cbc_open() call.

0 - OK

Where Used:

sys.cbc_senddata() can be called only between the corresponding
sys.cbc_open() and sys.cbc_close() calls.

Example:

Description:

sys.cbc_senddata() adds 1 data item to the 4C clipboard.

Bugs/Features/Comments:

See Also:

[Cut/Copy/Paste Overview](../Features/cutpaste.html)

[sys.cbc_sendtext()](./cbcsendtext.html)

\
\
[Back to Top](#TOPOFPAGE)
