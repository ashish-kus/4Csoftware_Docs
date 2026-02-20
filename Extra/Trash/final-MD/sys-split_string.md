---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 326
title: "sys.split_string"
---
## sys.split_string()
### Purpose
`sys.split_string()` splits a string variable into multiple vars.

### Usage
```c
count = sys.split_string(<spflags>,<string>,<avararray>,<delimstr>);
```

### Arguments
integer `<spflags>` - Either SP_DEFAULT or any combination of
- SP_NOQUOTE - Treat single or double quotes as normal characters
- SP_NOSTRIP - Do not strip out empty values. This is important when position in the string is important.
- SP_PRESERVEQUOTE - Preserve outer single or double quotes. Only meaningful when SP_NOQUOTE is not specified.

alpha `<string>` - The string to split.

alpha `<avararray>` - This should be the first member of a dimensioned var.

alpha `<delimstr>` - A string made up of the characters you want to use to determine where to split the string.

### Returns
integer `<count>` - The number of strings stored in `<avararray>`

### Where Used
`sys.split_string()` can be called from anywhere.

### Example
```c
n = sys.split_string(SP_DEFAULT,"abc,def,xyz",avar[0],",");
```
Assuming avar has a dimension of 10, this call will set n to 3, avar[0] to "abc", avar[1] to "def", and avar[2] to "xyz". avar[3] - avar[9] will each be set to "".

### Description
`sys.split_string()` splits a string into one or more strings and stores the resulting strings in a dimensioned variable. The splitting occurs at any character that matches one of the characters in `<delimstr>`. The character matched is not saved. By default single and double quotes are special and any delimiters inside of a quoted part of the string do not cause the string to split. To avoid this special treatment of single and double quotes, specify SP_NOQUOTE in `<spflags>`. Quotes act kind of odd when they are at the start of a split word. Unless SP_PRESERVEQUOTE is specified, quotes at the start of a split are stripped and the ending quote is stripped also and it also acts like a delimiter. Empty values are stripped out by default. To avoid this and have empty strings returned in the avarray specify SP_NOSTRIP in `<spflags>`.

### Bugs / Features / Comments
None

### See Also
- SP_DEFAULT()
- SP_NOQUOTE()
- SP_NOSTRIP()
- SP_PRESERVEQUOTE()
