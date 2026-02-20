<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.rand_integer()

### sys.rand_integer()

Purpose:

sys.rand_integer() returns a random integer \>= lowval and \<= highval

Usage:

ival = sys.rand_integer(lowval,highval);

Arguments:

integer/int64 - lowval

integer/int64 - highval

Returns:

integer/int64 - ival

Where Used:

sys.rand_integer() can be called from anywhere.

Example:

Description:

sys.rand_integer() returns a random integer between the 2 passed in
values. On error -1 is returns and sys_ret is set to SYSRET_ERROR. The
values passed in can be either 32bit integer values or 64bit integer
values

Requirements

Bugs/Features/Comments:

See Also:

[sys.rand_string()](./randstring.html)

[mathfunc](./mathfunc.html)\
\
[Back to Top](#TOPOFPAGE)
