<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.start_task()

### sys.start_task()

Purpose:

sys.start_task() starts a CISAM transaction.

Usage:

ret = sys.start_task();

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

sys.start_task() can be called from anywhere, but its usage will need to
coincide with logical transactions.

Example:

Description:

sys.start_task() starts a CISAM transaction. If you have already started
a transaction and have not called sys.end_task(), then CISAM will abort
the transaction in progress and start a new one. sys.start_task() calls
isbegin(). You should read and understand the isbegin() documentation in
the CISAM manuals.

Bugs/Features/Comments:

No Nested transactions.\
\
Beware of ENORMOUS log files.\
\
4C will eventually need to accomodate other file systems that allow
transaction processing. A new more general call will probably replace
sys.start_task().

See Also: sys.open_log() sys.close_log() sys.end_task() sys.abort_task()

\
\
[Back to Top](#TOPOFPAGE)
