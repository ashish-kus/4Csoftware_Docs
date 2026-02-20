<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.pkey_decrypt()

### sys.pkey_decrypt()

Purpose:

sys.pkey_decrypt() decrypts a publickey encrypted/base64 encoded piece
of text

Usage:

cleartext = sys.pkey_decrypt(\<pkeyname\>,\<b64text\>,\<encodingtype\>);

Arguments:

alpha - \<pkeyname\> - The name used by the application when opening the
private key.

alpha - \<b64text\> - The encrypted and encoded text to decode and
decrypt

integer - \<encodingtype\> - must be ENCODE_BASE64 or ENCODE_BASE64URL

Returns:

\<cleartext\> - The cleartext that was originally encrypted and encoded.

"" - Some error

Where Used:

sys.pkey_decrypt() can be called from anywhere as long as you have a
valid private RSA key open.

Example:

The demo program demo.pkey.1 has an example of using a public/private
key to encrypt and then using only the private key to decrypt a small
amount of text. If you try to do this with too large a piece of text you
will see that it fails at a fairly small length.

Description:

sys.pkey_decrypt() will use an open private key to decrypt a small
amount of base64 encoded text. amount of text.

Requirements

4csrvr version 5.2.8 or later

Bugs/Features/Comments:

Bugs

See Also:

[sys.pkey_open()](./pkeyopen.html)

[sys.pkey_close()](./pkeyclose.html)

[sys.pkey_sign()](./pkeysign.html)

[sys.pkey_verify()](./pkeyverify.html)

[sys.pkey_encrypt()](./pkeyencrypt.html)

\
\
[Back to Top](#TOPOFPAGE)
