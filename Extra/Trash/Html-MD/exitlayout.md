<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.exit_layout()

### sys.exit_layout()

Purpose:

sys.exit_layout() exits all programs in the current layout.

Usage:

sys.exit_layout();

Arguments:

This PCL takes no arguments.

Returns:

0 - OK

-1 - Current program is not a screen program.

Where Used:

sys.exit_layout() can be called from a ScreenProg only.

Example:

Description:

sys.exit_layout() exits all programs in the same layout as the current
ScreenProg. If the current program is not s ScreenProg, then
sys.exit_layout() returns -1.

Bugs/Features/Comments:

Programs exited using sys.exit_layout() will have an exit code of -3.

See Also:

[sys.exit_prog()](./exitprog.html)

[sys.end_prog()](./endprog.html)

\
\
[Back to Top](#TOPOFPAGE)
