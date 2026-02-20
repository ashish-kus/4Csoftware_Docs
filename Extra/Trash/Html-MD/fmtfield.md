<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.fmt_field()

### sys.fmt_field()

Purpose:

sys.fmt_field() returns a formatted field.

Usage:

aval = sys.fmt_field(\<field\>);

Arguments:

AnyType \<field\> - Any field of any data type defined in the program.

Returns:

alpha \<aval\> - The formatted value of \<field\>.

Where Used:

sys.fmt_field() can be called from anywhere.

Example:

Description:

sys.fmt_field() returns the formatted field, using the default display
format for the field. There are no error returns.

Requirements

4csrvr 5.0.6

Bugs/Features/Comments:

See Also:

[sys.fmt_field()](./fmtfield.html)

[sys.fmt_alpha()](./fmtalpha.html)

[sys.fmt_choice()](./fmtchoice.html)

[sys.fmt_date()](./fmtdate.html)

[sys.fmt_float()](./fmtfloat.html)

[sys.fmt_integer()](./fmtinteger.html)

[sys.fmt_time()](./fmttime.html)

\
\
[Back to Top](#TOPOFPAGE)
