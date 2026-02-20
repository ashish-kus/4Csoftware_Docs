---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 205
title: "isupper"
---
## isupper()
### Purpose
isupper() indicates if \<str\> is all uppercase letters or not.

### Usage
ret = isupper(\<str\>);

### Arguments
alpha \<str\> - The alpha var to check.

### Returns
integer \<ret\>

0 - \<str\> is not composed of ONLY uppercase letters.

1 - \<str\> is composed of ONLY uppercase letters.

### Where Used
isupper() can be called from anywhere.

### Example
None

### Description
isupper() returns 1 if \<str\> is composed of ONLY uppercase letters. If there are any characters other than A-Z, then isupper() returns 0. If \<str\> is NULL, then isupper() will return 1 because there are no non-uppercase letters.

### Bugs / Features / Comments
None

### See Also
- isdigit()
- islower()
- toupper()
