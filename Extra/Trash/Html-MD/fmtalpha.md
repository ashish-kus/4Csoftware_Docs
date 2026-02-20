<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.fmt_alpha()

### sys.fmt_alpha()

Purpose:

sys.fmt_alpha() formats an alpha variable

Usage:

aret = sys.fmt_alpha(\<aval\>,\<fmt\>);

Arguments:

alpha \<aval\> - The alpha value to format.

alpha \<fmt\> - A valid format for an alpha variable.

Returns:

alpha \<aret\> - The formatted value.

Where Used:

sys.fmt_alpha() can be called from anywhere.

Example:


    ssno = "123456789";
    dpyval = sys.fmt_alpha(ssno,"999-99-9999");

Description:

sys.fmt_alpha() formats an alpha variable using the passed in format. It
stores the formatted value in \<aret\>. \<aval\> is not changed by
sys.fmt_alpha().

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
