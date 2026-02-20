<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.err_msg()

### sys.err_msg()

Purpose:

sys.err_msg() - Displays an error message

Usage:

sys.err_msg(\[Arg1-Arg15\]);

Arguments:

AnyType - arg1,arg2,...,arg15 - The parts of the error msg

Returns:

Where Used:

sys.err_msg() can be called from anywhere.

Example:

sys.err_msg("Invalid Program Name",sys.pr_name);

Description:

sys.err_msg() displays a message and waits for a user response.

Requirements

4CServer version 5.0.6-05 or higher is required for using non alpha
arguments

Bugs/Features/Comments:

sys.err_msg() is obsolete. Use sys.message() instead.

See Also:

[sys.message()](./message.html)

[sys.msg()](./msg.html)

\
\
[Back to Top](#TOPOFPAGE)
