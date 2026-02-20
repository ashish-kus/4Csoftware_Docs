<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.fmt_float()

### sys.fmt_float()

Purpose:

sys.fmt_float() formats a float variable

Usage:

aret = sys.fmt_float(\<fval\>,\<fmt\>);

Arguments:

float \<fval\> - The float value to format.

alpha \<fmt\> - A valid format for a float variable.

Returns:

alpha \<aret\> - The formatted value.

Where Used:

sys.fmt_float() can be called from anywhere.

Example:


    fval = 129.23;
    dpyval = sys.fmt_float(fval,">>>,>>9.99-");

Description:

sys.fmt_float() formats a float variable using the passed in format. It
stores the formatted value in \<aret\>. \<fval\> is not changed by
sys.fmt_float().

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
