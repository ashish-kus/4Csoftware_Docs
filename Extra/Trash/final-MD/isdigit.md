---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 201
title: "isdigit"
---
## isdigit()
### Purpose
isdigit() indicates if `<str>` is all digits or not.

### Usage
```c
ret = isdigit(<str>);
```

### Arguments
alpha `<str>` - The alpha var to check.

### Returns
integer `<ret>`

0 - `<str>` is not composed of ONLY digits.

1 - `<str>` is composed of ONLY digits.

### Where Used
isdigit() can be called from anywhere.

### Example
None

### Description
isdigit() returns 1 if `<str>` is composed of ONLY digits. If there are any characters other than 0-9, then isdigit() returns 0. If `<str>` is NULL, then isdigit() will return 1 because there are no non-digit characters.

### Bugs / Features / Comments
None

### See Also
- islower()
- isupper()
- toupper()
