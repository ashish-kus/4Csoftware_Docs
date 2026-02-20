<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.log_error()

### sys.log_error()

Purpose:

sys.log_error() writes a rcd to the log_err file.

Usage:

ret = sys.log_err(\<lclname\>,\<filename\>,\<severity\>,\<msg\>);

Arguments:

alpha \<lclname\> - A name. It does not need to refer to an open log.

alpha \<filename\> - A 4c filename.

alpha \<severity\> - a one char severity code. Should be '0' - '9'

alpha \<msg\> - Application specific message

Returns:

0 - Always returned

Where Used:

sys.log_error() can be called from anywhere.

Example:

Description:

sys.log_error() writes a rcd to the log_err file. The log_err file is on
the same system that the 4csrvr is running on. It has nothing to do with
the system that any open log files refer to. The idea was to allow
applications that read log files, to be able to write errors to a common
file. The 4C system will also write logging errors to this file. This
file is purged by the log.purge.1 program. Systems that use logging or
use sys.log_error() need to make sure that the log.purge.1 program is
run periodically.

Bugs/Features/Comments:

See Also:

[sys.log_open()](./logopen.html)

[sys.log_close()](./logclose.html)

[sys.log_seek()](./logseek.html)

[sys.log_read()](./logread.html)

[sys.log_getattr()](./loggetattr.html)

[sys.log_getname()](./loggetname.html)

[sys.log_getval()](./loggetval.html)

[sys.log_copyflds()](./logcopyflds.html)

\
\
[Back to Top](#TOPOFPAGE)
