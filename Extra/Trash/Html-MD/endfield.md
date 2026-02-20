<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.end_field()

### sys.end_field()

Purpose:

sys.end_field() ends the processing of the current display field

Usage:

sys.end_field();

Arguments:

No args

Returns:

Normally there is no return, since sys.end_field() will exit the current
PCL

-1 - No current DFld

Where Used:

sys.end_field() can be called anytime a display field is being
processed.

Example:

One way sys.end_field() is used is to skip input when certain conditions
exist. For this purpose, sys.end_field() would be called from the
SFldPCL.

Description:

sys.end_field() ends the processing of the current display field. If
there is no current display field, then it does nothing and returns -1.
If there is an EFldPCL it will be executed. The differences between
sys.end_field() and sys.exit_field() are:

- sys.exit_field() allows you to specify the next DFld to be processed.
- sys.exit_field() will not execute the EFldPCL on the current DFld.

Bugs/Features/Comments:

See Also:

[sys.exit_field()](./exitfield.html)

\
\
[Back to Top](#TOPOFPAGE)
