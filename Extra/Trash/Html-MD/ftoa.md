<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

ftoa()

### ftoa()

Purpose:

ftoa() converts a float field to an alpha field, and returns the alpha
field.

Usage:

aval = ftoa(fval);

Arguments:

float fval;

Returns:

alpha aval;

There are no error returns from this PCL.

Where Used:

ftoa() can be called from anywhere.

Example:

sys.err_msg("fl =",ftoa(fl));

Description:

This PCL takes one float argument and converts it to an alpha, returning
the alpha. It is mostly useful in converting float fields to alpha for
display in error messages and in passing arguments.

Bugs/Features/Comments:

ftoa() does not allow specifying a format, but sys.fmt_float() can be
called if this is necessary.

See Also: atodate() itoa() atoi() atof() sys.fmt_alpha()
sys.fmt_choice() sys.fmt_date() sys.fmt_float() sys.fmt_integer()
sys.fmt_time()

\
\
[Back to Top](#TOPOFPAGE)
