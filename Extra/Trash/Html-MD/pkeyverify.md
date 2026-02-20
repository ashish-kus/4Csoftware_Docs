<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.pkey_verify()

### sys.pkey_verify()

Purpose:

sys.pkey_verify() verifies a the signature for a string of text using
public key cryptography.

Usage:

ret = sys.pkey_verify(\<pkeyname\>,\<text\>,\<sig\>);

Arguments:

alpha - \<pkeyname\> - The name the application used when opening the
key.

alpha - \<text\> - The data to verify

alpha - \<sig\> - The signature to verify

Returns:

0 - Signature verified.

-1 - Signature verify failed.

Where Used:

sys.pkey_verify() can be called anytime the application has an open
public/private key that they want to use to verify the digital signature
of a string of text.

Example:

The following Demo programs have examples of using sys.pkey_verify()

- demo.pkey.1
- demo.pkey.2
- demo.serial.cr

Description:

sys.pkey_verify() uses public key cryptography to verify the digital
signature of a string of text. The application must have open either the
public or the private key corresponding to the private key that was used
to digitally sign the text.

Requirements

sys.pkey_open() requires 4CServer Version 4.6.1 or higher

Bugs/Features/Comments:

See Also:

[sys.pkey_open()](./pkeyopen.html)

[sys.pkey_close()](./pkeyclose.html)

[sys.pkey_sign()](./pkeysign.html)

[sys.pkey_encrypt()](./pkeyencrypt.html)

[sys.pkey_decrypt()](./pkeydecrypt.html)

\
\
[Back to Top](#TOPOFPAGE)
