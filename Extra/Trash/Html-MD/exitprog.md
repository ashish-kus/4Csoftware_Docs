<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.exit_prog()

### sys.exit_prog()

Purpose:

sys.exit_prog() exits the current program.

Usage:

sys.exit_prog(\<exitcode\>);

Arguments:

integer \<exitcode\> - The value to set into \$wexit_code

Returns:

No Returns

Where Used:

sys.exit_prog() can be called from anywhere.

Example:

Description:

sys.exit_prog() ends all processing in the current program, and sets
\$wexit_code to \<exitcode\>

Bugs/Features/Comments:

See Also:

[sys.end_prog()](./endprog.html)

\
\
[Back to Top](#TOPOFPAGE)
