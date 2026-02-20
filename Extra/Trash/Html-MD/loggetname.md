<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.log_getname()

### sys.log_getname()

Purpose:

sys.log_getname() returns a fieldname of a field in the log file.

Usage:

aval = sys.log_getname(\<lclname\>,\<fldidx\>);

Arguments:

alpha \<lclname\> - The name used to open the log file.

integer \<fldidx\> - The idx of the fld in the current log rcd. The
\<fldidx\> must be \>= 0 and \< total number of fields in the current
log rcd.

Returns:

alpha \<aval\> - The name of the requested field.

"" - Error

Where Used:

sys.log_getname() can be called anytime a log file is open and there is
a current log rcd.

Example:

The 4cSys application uses sys.log_getname() in the log.view.det
program.

Description:

sys.log_getname() returns a fieldname of a field in the log file.

Bugs/Features/Comments:

See Also:

[sys.log_open()](./logopen.html)

[sys.log_close()](./logclose.html)

[sys.log_seek()](./logseek.html)

[sys.log_read()](./logread.html)

[sys.log_getattr()](./loggetattr.html)

[sys.log_getval()](./loggetval.html)

[sys.log_copyflds()](./logcopyflds.html)

[sys.log_error()](./logerror.html)

\
\
[Back to Top](#TOPOFPAGE)
