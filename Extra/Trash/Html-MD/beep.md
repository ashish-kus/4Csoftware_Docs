<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

beep()

### beep()

Purpose:

beep() beeps the terminal.

Usage:

beep();

Arguments:

None

Returns:

None

Where Used:

beep() can be called from anywhere.

Example:


    if (cm_read(cmcode < 0)) {
            beep();
            sys.exit_field(sys.cur_field);
    }

Description:

Sends a beep to the terminal. Currently this is done by writing a ^G to
the std err device. Possibly in the future a visible bell could be sent
if it is defined for the terminal.

Bugs/Features/Comments:

See Also:

[sys.err_msg(),](./errmsg.html)

[sys.msg()](./msg.html)

\
\
[Back to Top](#TOPOFPAGE)
