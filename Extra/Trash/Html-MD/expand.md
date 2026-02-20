<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.expand()

### sys.expand()

Purpose:

sys.expand() expands the env vars in a string and returns the expanded
string.

Usage:

aret = sys.expand(\<str\>);

Arguments:

alpha \<str\> - The alpha var to expand.

Returns:

alpha aret - The expanded string.

Where Used:

sys.expand() can be called from anywhere.

Example:

str = sys.expand("\${XLEXP}/sys.file_hdr.xl");

Description:

sys.expand() expands the env vars in a string and returns the expanded
string.

Bugs/Features/Comments:

The env parts of a string must be indicated with the \${VAR} notation.

See Also:

\
\
[Back to Top](#TOPOFPAGE)
