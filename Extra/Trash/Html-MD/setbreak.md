<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.set_break()

### sys.set_break()

Purpose:

sys.set_break() sets a 4c session breakpoint.

Usage:

ret =
sys.set_break(\<prname\>,\<brktype\>,\<name\>,\<asfilename\>,\<fromval\>,\<toval\>,\<flags\>);

Arguments:

alpha \<prname\> - The name of the program to set the breakpoint in. Use
"ALL" to set the breakpoint for all programs.

integer \<brktype\> - One of BRK_PROGRAM, BRK_PCL, BRK_VARIABLE, or
BRK_SYSPCL

alpha \<name\> - A name specific to the type of breakpoint being set. It
will be one of pclname, varname, or syspcl name. For BRK_PROGRAM, the
\<name\> argument is ignored.

alpha \<asfilename\> - The asfile name for the variable used in a
BRK_VARIABLE breakpoint. For all other breakpoint types the
\<asfilename\> argument is ignored.

alpha \<fromval\> - The alpha represenation of the from value for a
BRK_VARIABLE breakpoint when when the \<flags\> argument includes
BRK_FRVAL. For any other breakpoint type or a BRK_VARIABLE breakpoint
with \<flags\> that include BRK_FRANY the \<fromval\> argument is
ignored.

alpha \<toval\> - The alpha represenation of the to value for a
BRK_VARIABLE breakpoint when the \<flags\> argument includes BRK_TOVAL.
For any other breakpoint type or a BRK_VARIABLE breakpoint with
\<flags\> that include BRK_TOANY the \<toval\> argument is ignored.

integer \<flags\> - Combinations of BRK_ENTRY, BRK_EXIT, BRK_FRANY,
BRK_FRVAL, BRK_TOANY, BRK_TOVAL, BRK_LINENO. When setting a BRK_PCL on a
specific linenumber of a PCL the flags argument should be set to
(BRK_LINENO \| lineno).

Returns:

0 - OK. Currently, this is the only value returned.

Where Used:

Normally this is used by the system dbg programs when a developer is
doing interactive debugging of a 4c session. However, an application may
want to set breakpoints on it's own without user control when they use
their own program for debugging some exceptional conditions. When used
this way, the env var FC_DBGMAIN should be set to the application
program that should run when breakpoints are encountered.

Example:

Description:

sys.set_break() is useful for applications that need to debug seldom
encountered issues that are rarely duplicatable. One scenario for this
is to set a breakpoint on the SysPCL sys.upd_file() specifying
BRK_ENTRY. Then in the application program referenced by FC_DBGMAIN,
check for the conditions that you are looking for, such as a value in a
file changing to a specific value and if that condition is met, call
sys.app_trace() to create a complete trace of the current state of the
4c session and then somehow inform the developer via email or text
message that the trace was created so someone can look into it. When
used this way, the breakpoint is handled by the application program and
there should be no end user interaction. The end user will not notice
anything different than normal.\
\
Unless specificall cleared with sys.clr_break() breakpoints remain in
effect across the entire 4c session.

Requirements

In order for the application to run it's own program when a breakpoint
is required, the env var FC_DBGMAIN must be set correctly and the 4C
Server version must be 6.4.3 or later

Bugs/Features/Comments:

See Also: sys.clr_break()

\
\
[Back to Top](#TOPOFPAGE)
