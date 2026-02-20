<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.pkey_close()

### sys.pkey_close()

Purpose:

sys.pkey_close() closes the private/public key associated with
\<pkeyname\>

Usage:

ret = sys.pkey_close();

Arguments:

alpha - \<pkeyname\> - The name the application used when opening the
key.

Returns:

integer - \<ret\>

0 - OK

-1 - \<pkeyname\> not found.

Where Used:

sys.pkey_close() can be called anytime a private/public key is open.

Example:

The following Demo programs have examples of using sys.pkey_close()

- demo.pkey.1
- demo.pkey.2

Description:

sys.pkey_close() simply closes an open public/private key.

Requirements

sys.pkey_close() requires 4CServer Version 4.6.1 or higher

Bugs/Features/Comments:

See Also:

[sys.pkey_open()](./pkeyopen.html)

[sys.pkey_sign()](./pkeysign.html)

[sys.pkey_verify()](./pkeyverify.html)

[sys.pkey_encrypt()](./pkeyencrypt.html)

[sys.pkey_decrypt()](./pkeydecrypt.html)

\
\
[Back to Top](#TOPOFPAGE)
