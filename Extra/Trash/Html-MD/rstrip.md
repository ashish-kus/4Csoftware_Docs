<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.r_strip()

### sys.r_strip()

Purpose:

sys.r_strip() strips all trailing \<stripchar\> characters from the end
of \<originalstring\>

Usage:

\<aret\> = sys.r_strip(\<originalstring\>,\<stripchar\>);

Arguments:

alpha \<originalstring\> - The alpha variable to strip trailing
\<stripchar\> characters from.

alpha \<stripchar\> - A string of length 1 indicating the character that
should be stripped from then end of \<originalstring\>.

Returns:

alpha \<aret\> - A copy of \<originalstring\> with the trailing
\<stripchar\> characters deleted.

Where Used:

sys.r_strip() can be called from anywhere.

Example:

Description:

Requirements

Bugs/Features/Comments:

See Also:

[Sys PCLs List](./index.html)

\
\
[Back to Top](#TOPOFPAGE)
