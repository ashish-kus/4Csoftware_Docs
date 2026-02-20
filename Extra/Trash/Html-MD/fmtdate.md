<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.fmt_date()

### sys.fmt_date()

Purpose:

sys.fmt_date() formats a date variable

Usage:

aret = sys.fmt_date(\<dtval\>,\<fmt\>);

Arguments:

date \<dtval\> - The date value to format.

alpha \<fmt\> - A valid format for a date variable.

Returns:

alpha \<aret\> - The formatted value.

Where Used:

sys.fmt_date() can be called from anywhere.

Example:


    dt = atodate("01/01/1970");
    dpyval = sys.fmt_date(dt,"mm/dd/yyyy");

Description:

sys.fmt_date() formats a date variable using the passed in format. It
stores the formatted value in \<aret\>. \<dtval\> is not changed by
sys.fmt_date().

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
