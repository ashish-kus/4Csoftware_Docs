<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.log_seek()

### sys.log_seek()

Purpose:

sys.log_seek() sets the next log rcd ptr

Usage:

ret = sys.log_seek(\<lclname\>,\<logdate\>,\<logtime\>,\<logsequence\>);

Arguments:

alpha \<lclname\> - The name used when the log was opened.

date \<logdate\> - The date portion of the log_idx key

time \<logtime\> - The time portion of the log_idx key

integer \<logsequence\> - The sequence portion of the log_idx key

Returns:

0 - OK

-1 - \<lclname\> does not refer to an open log

Where Used:

sys.log_seek() can be called anytime a log is open.

Example:

The log.view.det and log.view.key 4C programs in the 4cSys application
both use sys.log_seek().

Description:

sys.log_seek() sets the log rcd ptr on an open log.

Bugs/Features/Comments:

See Also:

[sys.log_open()](./logopen.html)

[sys.log_close()](./logclose.html)

[sys.log_read()](./logread.html)

[sys.log_getattr()](./loggetattr.html)

[sys.log_getname()](./loggetname.html)

[sys.log_getval()](./loggetval.html)

[sys.log_copyflds()](./logcopyflds.html)

[sys.log_error()](./logerror.html)

\
\
[Back to Top](#TOPOFPAGE)
