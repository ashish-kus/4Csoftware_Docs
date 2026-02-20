<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.stop_busy()

### sys.stop_busy()

Purpose:

sys.stop_busy() stops a progress bar on the client.

Usage:

sys.stop_busy(\<name\>);

Arguments:

\<name\> - The alpha that was used to start this progress bar in
[sys.start_busy()](./startbusy.html)

Returns:

-1 - means no progress bar with name \<name\> was found. Otherwise 0 is
returned.

Where Used:

sys.stop_busy() can be called from anywhere.

Example:

Description:

This system pcl causes a currently running progress bar to stop running
on the client's display.

Bugs/Features/Comments:

See Also:

[sys.start_busy()](./startbusy.html)

[sys.set_busy()](./setbusy.html)

\
\
[Back to Top](#TOPOFPAGE)
