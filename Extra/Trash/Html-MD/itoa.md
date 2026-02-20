<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

itoa()

### itoa()

Purpose:

itoa() converts an integer field to an alpha field, and returns the
alpha field.

Usage:

aval = itoa(ival);

Arguments:

integer ival;

Returns:

\<aval\> - alpha representation of \<ival\>

There are no error returns from this PCL.

Where Used:

itoa() can be called from anywhere.

Example:

push_prog("an.call.de.1",itoa(\$row_ofst+1),"0");

Description:

This PCL takes one integer argument and converts it to an alpha,
returning the alpha.

Bugs/Features/Comments:

See Also: atodate() atoi() atof() ftoa() sys.fmt_alpha()
sys.fmt_choice() sys.fmt_date() sys.fmt_float() sys.fmt_integer()
sys.fmt_time()

\
\
[Back to Top](#TOPOFPAGE)
