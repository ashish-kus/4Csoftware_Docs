<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.set_prcolor()

### sys.set_prcolor()

Purpose:

sys.set_prcolor() allows a program to dynamically change the background
and foreground color of a program.

Usage:

ret = sys.set_prcolor(\<fgrgbval\>,\<bgrgbval\>);

Arguments:

\<fgrgbval\> - alpha var in "rrr:ggg:bbb" format If \<fgrgbval\> is "",
it will not be changed. If it is "Default", it will change to the
programs default foreground.

\<bgrgbval\> - alpha var in "rrr:ggg:bbb" format If \<bgrgbval\> is "",
it will not be changed. If it is "Default", it will change to the
programs default background.

Returns:

The only value returned currently is 0.

Where Used:

sys.set_prcolor() can be called from anywhere but probably should be
called from either the Init PCL or the DrInit PCL.

Example:

Description:

sys.set_prcolor() allows a program to dynamically change the background
and foreground color of a program. This can be useful if it cannot be
known at layout compile time.

Bugs/Features/Comments:

sys.set_prcolor() is only implemented for scrolling programs

See Also:

[sys.set_dfcolor()](./setdfcolor.html)

[sys.set_dricolor()](./setdricolor.html)

\
\
[Back to Top](#TOPOFPAGE)
