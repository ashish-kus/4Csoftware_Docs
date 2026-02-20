<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_timeoutv()

### sys.get_timeoutv()

Purpose:

sys.get_timeoutv() returns the timeout value for any server/client
session/program timeout.

Usage:

oldtimeoutv = sys.get_timeoutv(TIMEOUT_TYPE);

Arguments:

TIMEOUT_TYPE must be one of

- TO_SVGLOBAL - Server Session Timeout.
- TO_SVPROGRAM - Server Program Timeout
- TO_CLGLOBAL - Client Session Timeout
- TO_CLPROGRAM - Client Program Timeout.

Returns:

0 - there is no timeout defined for TIMEOUT_TYPE.

\> 0 - The \#seconds associated with TIMEOUT_TYPE.

Where Used:

sys.get_timeoutv() can be called from anywhere.

Example:

The demo programs that catch timeouts have examples. See:

- demo.main.s
- lockscreen.s

Description:

sys.get_timeoutv() returns the \#seconds for for the specified timeout
type.

Bugs/Features/Comments:

See Also: [sys.set_timeout()](./settimeout.html)

[sys.get_timeoutp()](./gettimeoutp.html)

[sys.set_alarm()](./setalarm.html)

[sys.lock_clientws()](./lockclientws.html)

[sys.exit_client()](./exitclient.html)

[sys.exit_4c()](./exit_4c.html)

\
\
[Back to Top](#TOPOFPAGE)
