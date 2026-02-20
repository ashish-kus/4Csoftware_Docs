<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.fmt_integer()

### sys.fmt_integer()

Purpose:

sys.fmt_integer() formats a integer variable

Usage:

aret = sys.fmt_integer(\<ival\>,\<fmt\>);

Arguments:

integer \<ival\> - The integer value to format.

alpha \<fmt\> - A valid format for a integer variable.

Returns:

alpha \<aret\> - The formatted value.

Where Used:

sys.fmt_integer() can be called from anywhere.

Example:


    ival = -129;
    dpyval = sys.fmt_integer(ival,">>>,>>9-");

Description:

sys.fmt_integer() formats a integer variable using the passed in format.
It stores the formatted value in \<aret\>. \<ival\> is not changed by
sys.fmt_integer().

Bugs/Features/Comments:

It's difficult to tell if you passed in an invalid format, though if you
do, the application will probably display an error message at runtime.

See Also:

[sys.fmt_field()](./fmtfield.html)

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
