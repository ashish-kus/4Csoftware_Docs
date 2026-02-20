<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_extfnopt()

### sys.get_extfnopt()

Purpose:

sys.get_extfnopt() allows the application to get information about a 4C
External Library including last error information.

Usage:

optval = sys.get_extfnopt(\<extlibname\>,\<optname\>);

Arguments:

alpha \<extlibname\> - The name of the library.

alpha \<optname\> - The name of the option.

Returns:

alpha \<optval\> - The value to of the option.

Where Used:

sys.get_extfnopt() can be called from any 4C program that uses that
library.

Example:

msg = sys.get_extfnopt("FCCom","LastMessage");

Description:

sys.get_extfnopt() allows the application to get information about a
particular library including last error and message information.

- MessageLevel - The Message reporting level the library uses for the
  current 4C program.
- LastError - The error number returned by the last function call into
  this library for the current 4C program.
- LastMessage - The message, error or info, reported by last function
  call into this library.

Requirements

4csrvr version 5.8.7 or later.

Bugs/Features/Comments:

Bugs

See Also:

[sys.set_extfnopt()](./setextfnopt.html)

[Sys PCLs List](./index.html)

\
\
[Back to Top](#TOPOFPAGE)
