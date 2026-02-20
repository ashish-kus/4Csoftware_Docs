---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 243
title: "sys.pkey_verify"
---
## sys.pkey_verify()
### Purpose
`sys.pkey_verify()` verifies a the signature for a string of text using public key cryptography.

### Usage
```c
ret = sys.pkey_verify(<pkeyname>,<text>,<sig>);
```

### Arguments
- `<pkeyname>` - The name the application used when opening the key.
- `<text>` - The data to verify
- `<sig>` - The signature to verify

### Returns
- 0 - Signature verified.
- -1 - Signature verify failed.

### Where Used
`sys.pkey_verify()` can be called anytime the application has an open public/private key that they want to use to verify the digital signature of a string of text.

### Example
The following Demo programs have examples of using `sys.pkey_verify()`
- demo.pkey.1
- demo.pkey.2
- demo.serial.cr

### Description
`sys.pkey_verify()` uses public key cryptography to verify the digital signature of a string of text. The application must have open either the public or the private key corresponding to the private key that was used to digitally sign the text.

### Bugs / Features / Comments
None

### See Also
- sys.pkey_open()
- sys.pkey_close()
- sys.pkey_sign()
- sys.pkey_encrypt()
- sys.pkey_decrypt()
