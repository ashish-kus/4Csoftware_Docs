<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.pr_restart()

### sys.pr_restart()

Purpose:

sys.pr_restart() restarts the current program at the Start/Restart state

Usage:

ret = sys.pr_restart();

Arguments:

Returns:

-1 - Program is not currently open

If sys.pr_restart() succeeeds then there is no return to the calling
PCL.

Where Used:

sys.pr_restart() can be called from anytime that the program is open. A
program that has not finished executing the Open PCL or a program that
has already started executing the Exit PCL is not considered open.

Example:

Description:

sys.pr_restart() can be used by the application to restart the current
program. If the program is a screen program, the window will not
disappear. Program and file vsriables are not cleared. If you need to
reset file variables to some other initial state, you will want to use
one or more of sys.fl_save(), sys.fl_restore(), and
sys.restore_share().\
\
If the program is a scrolling program, the driver is closed and any
screen list will be cleared. If the program is a panel program and it
has an initial option panel, then that initial option panel will get
control after the Start/Restart PCL is executed.

Requirements

4csrvr version 5.2 or later

Bugs/Features/Comments:

See Also:

[sys.fl_save()](./flsave.html)

[sys.restore_share()](./restoreshare.html)

[sys.fl_restore()](./flrestore.html)

\
\
[Back to Top](#TOPOFPAGE)
