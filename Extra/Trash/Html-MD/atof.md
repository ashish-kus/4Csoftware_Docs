<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

atof()

### atof()

Purpose:

atof() converts an alpha field to a float field, and returns the float
field.

Usage:

fval = atof(aval);

Arguments:

alpha aval;

Returns:

float fval;

There are no error returns from this PCL.

Where Used:

atof() can be called from anywhere.

Example:

fl = atof("3.24");

Description:

This PCL takes one alpha argument and converts it to a float, returning
the float. A leading or trailing sign can be used. It is possible to get
garbage in the return if the alpha argument was garbage also.

Bugs/Features/Comments:

atof() does not verify the format of aval.

See Also:

[atodate()](./atodate.html)

[atoi()](./atoi.html)

[atof()](./atof.html)

[ftoa()](./ftoa.html)

[itoa()](./itoa.html)

[sys.fmt_alpha()](./fmtalpha.html)

[sys.fmt_choice()](./fmtchoice.html)

[sys.fmt_date()](./fmtdate.html)

[sys.fmt_float()](./fmtfloat.html)

[sys.fmt_integer()](./fmtinteger.html)

[sys.fmt_time()](./fmttime.html)

\
\
[Back to Top](#TOPOFPAGE)
