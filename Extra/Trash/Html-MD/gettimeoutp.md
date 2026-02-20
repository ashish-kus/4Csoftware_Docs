<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_timeoutp()

### sys.get_timeoutp()

Purpose:

sys.get_timeoutp() returns the timeout prog and its arguments for any
server/client program/session timeout.

Usage:

oldtimeoutp = sys.get_timeoutp(TIMEOUT_TYPE);

Arguments:

TIMEOUT_TYPE must be one of

- TO_SVGLOBAL - Server Session Timeout.
- TO_SVPROGRAM - Server Program Timeout
- TO_CLGLOBAL - Client Session Timeout
- TO_CLPROGRAM - Client Program Timeout.

Returns:

Blank - there is no timeoutprog or no timeout defined for TIMEOUT_TYPE.

NonBlank - The program and args associated with TIMEOUT_TYPE.

Where Used:

sys.get_timeoutp() can be called from anywhere. However it will normally
be called by a timeout processing program that wants to disable a
timeout in the InitPCL and reenable it in the ExitPCL.

Example:

The demo programs that catch timeouts have examples. See:

- demo.main.s
- lockscreen.s

Description:

sys.get_timeoutp() returns the timeout prog and its arguments for either
a program or a session timeout.

Bugs/Features/Comments:

See Also:

[sys.set_timeout()](./settimeout.html)

[sys.get_timeoutv()](./gettimeoutv.html)

[sys.set_alarm()](./setalarm.html)

[sys.lock_clientws()](./lockclientws.html)

[sys.exit_client()](./exitclient.html)

[sys.exit_4c()](./exit_4c.html)

\
\
[Back to Top](#TOPOFPAGE)
