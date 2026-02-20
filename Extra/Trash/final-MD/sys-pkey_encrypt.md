---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 240
title: "sys.pkey_encrypt"
---
## sys.pkey_encrypt()
### Purpose
`sys.pkey_encrypt()` encrypts and encodes a small chunk of text using either a public or private key.

### Usage
```c
b64text = sys.pkey_encrypt(<pkeyname>,<text>,<encodingtype>);
```

### Arguments
- `<pkeyname>` - The name used by the application when opening the public or private key.
- `<text>` - The clear text to encrypt.
- `<encodingtype>` - must be `ENCODE_BASE64` or `ENCODE_BASE64URL`.

### Returns
- `<b64text>` - The base64 encoding of the encrypted text.
- "" - Some error.

### Where Used
`sys.pkey_encrypt()` can be called from anywhere as long as you have a valid public or private RSA key open.

### Example
The demo program `demo.pkey.1` has an example of using a public/private key to encrypt and then using only the private key to decrypt a small amount of text. If you try to do this with too large a piece of text you will see that it fails at a fairly small length.

### Description
`sys.pkey_encrypt()` will use an open public or private key to encrypt and encode a very small amount of text. This should really only be used when it is necessary to encrypt a symmetric key and send it securely to another system. The size of text that can be encrypted is fairly small and you should assume it is no larger than 86 bytes.

### Bugs / Features / Comments
None

### See Also
- sys.pkey_open()
- sys.pkey_close()
- sys.pkey_sign()
- sys.pkey_verify()
- sys.pkey_decrypt()
