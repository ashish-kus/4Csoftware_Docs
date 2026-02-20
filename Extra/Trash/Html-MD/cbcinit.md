<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.cbc_init()

### sys.cbc_init()

Purpose:

sys.cbc_init() clears the 4C clipboard and initializes it with default
data.

Usage:

sys.cbc_init();

Arguments:

None

Returns:

None

Where Used:

sys.cbc_init() can be called anytime to initialize the 4C clipboard.

Example:

Description:

sys.cbc_init() clears the 4C clipboard and initializes it with default
data. After calling sys.cbc_init(), the application is able to make a
series of sys.cbc_open(), sys.cbc_senddata(), and sys.cbc_close() calls.

Bugs/Features/Comments:

See Also:

[Cut/Copy/Paste Overview](../Features/cutpaste.html)

[sys.cbc_end()](./cbcend.html)

[sys.cbc_open()](./cbcopen.html)

\
\
[Back to Top](#TOPOFPAGE)
