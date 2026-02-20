<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.abort_task()

### sys.abort_task()

Purpose:

sys.abort_task() aborts a CISAM transaction.

Usage:

ret = sys.abort_task();

Arguments:

None

Returns:

\<integer\> ret

0 - OK

-1 - CISAM Not Available or CISAM ERROR\
\
For CISAM errors, a message has been displayed including the CISAM
errno.

Where Used:

sys.abort_task() can be called from anywhere as long as a CISAM task is
in progress.

Example:

Description:

sys.abort_task() aborts a CISAM transaction. sys.abort_task() calls
isrollback(). You should read and understand the isrollback()
documentation in the CISAM manuals.

Bugs/Features/Comments:

No Nested transactions.\
\
Beware of ENORMOUS log files.\
\
4C will eventually need to accomodate other file systems that allow
transaction processing. A new more general call will probably replace
sys.abort_task().

See Also:

[sys.open_log()](./openlog.html)

[sys.close_log()](./closelog.html)

[sys.start_task()](./starttask.html)

[sys.end_task()](./endtask.html)

\
\
[Back to Top](#TOPOFPAGE)
