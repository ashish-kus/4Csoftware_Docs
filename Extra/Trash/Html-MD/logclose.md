<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.log_close()

### sys.log_close()

Purpose:

sys.log_close() closes an open log.

Usage:

ret = sys.log_close(\<lclname\>);

Arguments:

alpha \<lclname\> - The name specified when the log was opened.

Returns:

0 - OK

-1 - \<lclname\> is not a currently open log.

Where Used:

sys.log_close() can be called from anywhere.

Example:

Description:

sys.log_close() explicitly closes an open log. Logs are implicitly
closed if the application does not call sys.close_log() and the 4C
program that opened the log exits.

Bugs/Features/Comments:

See Also:

[sys.log_open()](./logopen.html)

[sys.log_seek()](./logseek.html)

[sys.log_read()](./logread.html)

[sys.log_getattr()](./loggetattr.html)

[sys.log_getname()](./loggetname.html)

[sys.log_getval()](./loggetval.html)

[sys.log_copyflds()](./logcopyflds.html)

[sys.log_error()](./logerror.html)

\
\
[Back to Top](#TOPOFPAGE)
