<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.cbp_exit()

### sys.cbp_exit()

Purpose:

sys.cbp_exit() exits the paste loop.

Usage:

sys.cbp_exit(\[\<code\>\]);

Arguments:

integer \<code\> - Optional code. Currently unused.

Returns:

None

Where Used:

sys.cbp_exit() can be called anytime during the paste loop but when used
is usually called during PasteInit.

Example:

Description:

sys.cbp_exit() exits the paste loop. The most likely reason to call
sys.cbp_exit() is that the user has tried to paste an incompatible type
of data to the 4C application. After calling sys.cbp_exit(), 4C will
next process the PasteEnd state.

Bugs/Features/Comments:

See Also:

[Cut/Copy/Paste Overview](../Features/cutpaste.html)

\
\
[Back to Top](#TOPOFPAGE)
