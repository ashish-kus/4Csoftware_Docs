<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.err_msg()

### sys.err_msg()

Purpose:

sys.err_msg() - Displays an status message

Usage:

sys.msg(\[Arg1-Arg15\]);

Arguments:

AnyType - arg1,arg2,...,arg15 - The parts of the msg

Returns:

Where Used:

sys.msg() can be called from anywhere.

Example:

sys.msg("Processing...",sys.pr_name);

Description:

sys.msg() displays a message on in the status area and does not wait for
any user response.

Requirements

4CServer version 5.0.6-05 or higher is required for using non alpha
arguments

Bugs/Features/Comments:

sys.msg() is obsolete. Use sys.message() instead.

See Also:

[sys.message()](./message.html)

[sys.err_msg()](./errmsg.html)

\
\
[Back to Top](#TOPOFPAGE)
