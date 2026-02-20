<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.pkey_sign()

### sys.pkey_sign()

Purpose:

sys.pkey_sign() uses an open private key to digitally sign a string of
text.

Usage:

sig = sys.pkey_sign(\<pkeyname\>,\<text\>);

Arguments:

alpha - \<pkeyname\> - The name used by the application when opening the
private key.

alpha - \<text\> - The data to sign

Returns:

alpha - \<sig\> - The digital signature of the text

"" - Error

Anything else - the digital signature of the text.

Where Used:

sys.pkey_sign() can be called anytime the private key is open.

Example:

The following Demo programs have examples of using sys.pkey_sign()

- demo.pkey.1
- demo.pkey.2
- demo.serial.cr

Description:

sys.pkey_sign() uses the open private key to create the digital
signature for a string of text. The application may store this signature
and use sys.pkey_verify() somewhere else in the application to verify
that the signed text has not been modified.

Requirements

sys.pkey_open() requires 4CServer Version 4.6.1 or higher

Bugs/Features/Comments:

See Also:

[sys.pkey_open()](./pkeyopen.html)

[sys.pkey_close()](./pkeyclose.html)

[sys.pkey_verify()](./pkeyverify.html)

[sys.pkey_encrypt()](./pkeyencrypt.html)

[sys.pkey_decrypt()](./pkeydecrypt.html)

\
\
[Back to Top](#TOPOFPAGE)
