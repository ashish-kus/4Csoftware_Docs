<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.close_log()

### sys.close_log()

Purpose:

sys.close_log() closes the CISAM log file.

Usage:

ret = sys.close_log();

Arguments:

None

Returns:

Always returns 0.

Where Used:

sys.close_log() can be called from anywhere.

Example:

Description:

See your CISAM documentation for detailed description of the CISAM
logfile.

Bugs/Features/Comments:

As other databases are added to 4C this call will probably be changed or
another added to account for differences in the databases and to make
the 4C programs transparent to them.

See Also:

[sys.open_log()](./openlog.html)

[sys.start_task()](./starttask.html)

[sys.end_task()](./endtask.html)

[sys.abort_task()](./aborttask.html)

\
\
[Back to Top](#TOPOFPAGE)
