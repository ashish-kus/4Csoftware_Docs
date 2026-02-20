<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.set_busy()

### sys.set_busy()

Purpose:

sys.set_busy() allows you to modify either the title or the label of a
running progress bar.

Usage:

sys.set_busy(\<name\>, \<type\>, \<newtext\>);

Arguments:

\<name\> - The alpha that was used to start this progress bar in
[sys.start_busy()](./startbusy.html)

\<type\> - One of SB_TITLE or SB_LABEL indicating what you are changing.

\<newtext\> - The new text for the progress bar title or label.

Returns:

-1 - means no progress bar with name \<name\> was found. Otherwise 0 is
returned.

Where Used:

sys.set_busy() can be called from anywhere.

Example:

Description:

This system pcl allows you to change either the label or the title of a
currently running progress bar.

Bugs/Features/Comments:

See Also:

[sys.start_busy()](./startbusy.html)

[sys.stop_busy()](./stopbusy.html)

\
\
[Back to Top](#TOPOFPAGE)
