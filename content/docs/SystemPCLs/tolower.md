---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 336
title: "tolower"
---
## tolower()
### Purpose
tolower() converts any upper case letters in an alpha variable to lower case.

### Usage
```c
aret = tolower(<avar>);
```

### Arguments
alpha `<avar>` - The alpha variable to convert.

### Returns
alpha `<aret>` - The converted alpha.

### Where Used
tolower() can be called from anywhere.

### Example
None

### Description
tolower() translates an alpha variable by converting all upper case letters to lowercase. All other characters are left untouched. The converted alpha is the return value of tolower(). The original alpha is left unchanged unless it is specified as `<aret>`.

### Bugs / Features / Comments
None

### See Also
- toupper()
- isdigit()
- islower()
- isupper()
