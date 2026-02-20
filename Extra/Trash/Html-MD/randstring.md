<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.rand_string()

### sys.rand_string()

Purpose:

sys.rand_string() returns a random string of length \<len\> from the
characters \<charset\>.

Usage:

rstr = sys.rand_string(\<charset\>,\<len\>);

Arguments:

alpha \<charset\> - The set of characters to use to create the random
string.

integer \<len\> - The length of the string to return.

Returns:

alpha \<rstr\> - The random string.

Where Used:

sys.rand_string() can be called from anywhere.

Example:

There are some examples of sys.rand_string() in the demo program
dtf32.bld.1

Description:

sys.rand_string() is used to create a cryptographically strong random
string from the characters in \<charset\>. It can be use to create
random numbers by limiting \<charset\> to the digits you want to allow
in the number and then converting the return to a number. For example,
to create a random 5 digit number use:


         n = atoi(sys.rand_string("0123456789",5));
         

Requirements

4csrvr version 5.0 or later

Bugs/Features/Comments:

See Also:

[sys.rand_integer()](./randinteger.html)

[mathfunc](./mathfunc.html)

\
\
[Back to Top](#TOPOFPAGE)
