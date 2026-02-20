<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.choose_color()

### sys.choose_color()

Purpose:

sys.choose_color() selects a color using the clients color dialog.

Usage:

rgbval = sys.choose_color(\<initrgb\>);

Arguments:

\<initrgb\> - an alpha of the form rrr:ggg:bbb that is the default
color.

Returns:

\<rgbval\> - An alpha of the form rrr:ggg:bbb. If the user cancels, then
"" is returned.

Where Used:

sys.choose_color() can be called from anywhere.

Example:

Description:

sys.choose_color() allows the user to select a color. You may store this
color and use it in subsequent calls to
[sys.set_prcolor()](./setprcolor.html) ,
[sys.set_dfcolor()](./setdfcolor.html) , and
[sys.set_dricolor()](./setdricolor.html)

Bugs/Features/Comments:

See Also:

[sys.set_prcolor()](./setprcolor.html)

[sys.set_dfcolor()](./setdfcolor.html)

[sys.set_dricolor()](./setdricolor.html)

\
\
[Back to Top](#TOPOFPAGE)
