---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 239
title: "sys.pkey_decrypt"
---
## sys.pkey_decrypt()
### Purpose
sys.pkey_decrypt() decrypts a publickey encrypted/base64 encoded piece of text

### Usage
```c
cleartext = sys.pkey_decrypt(<pkeyname>,<b64text>,<encodingtype>);
```

### Arguments
alpha - `<pkeyname>` - The name used by the application when opening the private key.

alpha - `<b64text>` - The encrypted and encoded text to decode and decrypt

integer - `<encodingtype>` - must be ENCODE_BASE64 or ENCODE_BASE64URL

### Returns
`<cleartext>` - The cleartext that was originally encrypted and encoded.

"" - Some error

### Where Used
sys.pkey_decrypt() can be called from anywhere as long as you have a valid private RSA key open.

### Example
The demo program demo.pkey.1 has an example of using a public/private key to encrypt and then using only the private key to decrypt a small amount of text. If you try to do this with too large a piece of text you will see that it fails at a fairly small length.

### Description
sys.pkey_decrypt() will use an open private key to decrypt a small amount of base64 encoded text. amount of text.

### Bugs / Features / Comments
Bugs

### See Also
- sys.pkey_open()
- sys.pkey_close()
- sys.pkey_sign()
- sys.pkey_verify()
- sys.pkey_encrypt()
