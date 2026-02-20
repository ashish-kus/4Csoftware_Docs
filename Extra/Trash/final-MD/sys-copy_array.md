---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 48
title: "sys.copy_array"
---
## sys.copy_array()
### Purpose
sys.copy_array() copies one or more elements of an array to another array.

### Usage
```c
ret = copyarray(<fromarrayitem>, <toarrayitem> [, <maxitemstocopy> ]);
```

### Arguments
\<fromarrayitem\> - Any 4c array item. This specifies the start of where to begin the copy from.

\<toarrayitem\> - Any 4c array item. This specifies the start where to begin the copy to.

integer - \<maxitemstocopy\> - Optional argument specifying the maximum number of array items to copy.

### Returns
\< 0 - Error

\>= 0 - The number of items actually copied.

### Where Used
sys.copy_array() can be called from anywhere.

### Example
None

### Description
sys.copy_array() can be used to copy 1 or more array items from 1 array to either the same array or a different array. If copying to the same array, the application must make sure that the copy to area does not overlap the copy from area by specifying the \<maxitemstocopy\>. The system makes sure that items copied from and to are never outside of the bounds of the 2 arrays.

### Bugs / Features / Comments
None

### See Also
- None
