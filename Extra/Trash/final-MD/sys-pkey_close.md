---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 238
title: "sys.pkey_close"
---
## sys.pkey_close()
### Purpose
sys.pkey_close() closes the private/public key associated with \<pkeyname\>.

### Usage
```c
ret = sys.pkey_close();
```

### Arguments
- alpha - \<pkeyname\> - The name the application used when opening the key.

### Returns
integer - \<ret\>

0 - OK

-1 - \<pkeyname\> not found.

### Where Used
sys.pkey_close() can be called anytime a private/public key is open.

### Example
The following Demo programs have examples of using `sys.pkey_close()`

- demo.pkey.1
- demo.pkey.2

### Description
sys.pkey_close() simply closes an open public/private key.

### Bugs / Features / Comments
None

### See Also
- sys.pkey_open()
- sys.pkey_sign()
- sys.pkey_verify()
- sys.pkey_encrypt()
- sys.pkey_decrypt()
