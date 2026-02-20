[]{#TOPOFPAGE} Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [Global PCLs List](./index.html)

sys.app_trace()

### sys.app_trace() {#sys.app_trace align="center"}

Purpose:

sys.app_trace() creates a trace file of the state of the 4csrvr process
when it is called and it writes to log records to the application log.

Usage:

sys.app_trace(\<type\>,\<typedet\>,\<severity\>,\<message\>,\<option\>);

Arguments:

alpha \<type\> - An application specific type up 20 chars.

alpha \<typedet\> - Detail of the type if needed. Up to 30 chars.

integer \<severity\> - a value indicating how important the log message
is. The higher the serverity the more important the message.

alpha \<message\> - A detailed message up to 200 characters.

alpha \<option\> - currently Verbose or NoVerbose

Returns:

None

Where Used:

sys.app_trace() can be called from anywhere.

Example:

The demo.dbg.main program has an example of calling sys.app_trace()

Description:

sys.app_trace uses the 1st 4 arguments to write a rcd to the application
log. It then creates a full trace of the current state of the 4csrvr
process and writes this to a trace file in the FC_TEMP diirectory.
Finally it writes another rcd to the application log with a type of
\"TraceFile\" and a message indicating the full path of the trace file.

Requirements

4csrvr version 6.4.4 and later

Bugs/Features/Comments:

Bugs

See Also: See Also

[sys.app_log()](./applog.html)

\
\
[Back to Top](#TOPOFPAGE)
