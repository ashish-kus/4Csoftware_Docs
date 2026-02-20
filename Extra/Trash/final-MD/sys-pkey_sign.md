---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 242
title: "sys.pkey_sign"
---
## sys.pkey_sign()
### Purpose
`sys.pkey_sign()` uses an open private key to digitally sign a string of text.

### Usage
```c
sig = sys.pkey_sign(<pkeyname>,<text>);
```

### Arguments
- `<pkeyname>` - The name used by the application when opening the private key.
- `<text>` - The data to sign.

### Returns
- `<sig>` - The digital signature of the text.
- "" - Error.
- Anything else - the digital signature of the text.

### Where Used
`sys.pkey_sign()` can be called anytime the private key is open.

### Example
The following Demo programs have examples of using `sys.pkey_sign()`:
- demo.pkey.1
- demo.pkey.2
- demo.serial.cr

### Description
`sys.pkey_sign()` uses the open private key to create the digital signature for a string of text. The application may store this signature and use `sys.pkey_verify()` somewhere else in the application to verify that the signed text has not been modified.

### Bugs / Features / Comments
None

### See Also
- sys.pkey_open()
- sys.pkey_close()
- sys.pkey_verify()
- sys.pkey_encrypt()
- sys.pkey_decrypt()
