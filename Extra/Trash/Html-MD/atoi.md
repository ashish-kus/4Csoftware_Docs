<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

atoi()

### atoi()

Purpose:

atoi() converts an alpha field to an integer field, and returns the
integer field.

Usage:

ival = atoi(aval);

Arguments:

alpha aval;

Returns:

integer ival;

There are no error returns from atoi().

Where Used:

atoi() can be called from anywhere.

Example:

fromdate = atoi(argv\[3\]);

Description:

This PCL takes one alpha argument and converts it to an integer,
returning the integer.

Bugs/Features/Comments:

atoi() does not verify the format of aval.

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
