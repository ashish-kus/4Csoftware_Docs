<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

islower()

### islower()

Purpose:

islower() indicates if \<str\> is all lowercase letters or not.

Usage:

ret = islower(\<str\>);

Arguments:

alpha \<str\> - The alpha var to check.

Returns:

integer \<ret\>

0 - \<str\> is not composed of ONLY lowercase letters.

1 - \<str\> is composed of ONLY lowercase letters.

Where Used:

islower() can be called from anywhere.

Example:

Description:

islower() returns 1 if \<str\> is composed of ONLY lowercase letters. If
there are any characters other than A-Z, then islower() returns 0. If
\<str\> is NULL, then islower() will return 1 because there are no
non-lowercase letters.

Bugs/Features/Comments:

See Also: isdigit() isupper() toupper()

\
\
[Back to Top](#TOPOFPAGE)
