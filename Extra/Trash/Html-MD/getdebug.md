<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_debug()

### sys.get_debug()

Purpose:

sys.get_debug() returns either "ON" or "OFF" indicating whether the 4C
debugger is currently running or not.

Usage:

dbgmode = sys.get_debug();

Arguments:

None

Returns:

"ON" - Debugger is active

"OFF - Debugger is not active.

Where Used:

sys.get_debug() can be called from anywhere. It is called in the
bootstrap program sys.prog.mstr in order to display it on the screen.

Example:

The following stmt is from the bootstrap program sys.prog.mstr. It is in
the Init PCL.\
\


    sys.uscr_dbflag = sys.get_debug();

Description:

sys.get_debug() returns either "ON" or "OFF" indicating whether the 4C
debugger is currently running or not.

Bugs/Features/Comments:

See Also: sys.set_debug()

\
\
[Back to Top](#TOPOFPAGE)
