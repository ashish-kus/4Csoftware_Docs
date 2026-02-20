<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.l_strip()

### sys.l_strip()

Purpose:

sys.l_strip() strips all leading \<stripchar\> characters from the
beginning of \<originalstring\>

Usage:

\<aret\> = sys.l_strip(\<originalstring\>,\<stripchar\>);

Arguments:

alpha \<originalstring\> - The alpha variable to strip leading
\<stripchar\> characters from.

alpha \<stripchar\> - A string of length 1 indicating the character that
should be stripped from the beginning of \<originalstring\>.

Returns:

alpha \<aret\> - A copy of \<originalstring\> with the leading
\<stripchar\> characters deleted.

Where Used:

sys.l_strip() can be called from anywhere.

Example:

Description:

Requirements

Bugs/Features/Comments:

See Also:

[Sys PCLs List](./index.html)

\
\
[Back to Top](#TOPOFPAGE)
