<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.fmt_choice()

### sys.fmt_choice()

Purpose:

sys.fmt_choice() formats an choice variable

Usage:

aret = sys.fmt_choice(\<aval\>,\<fmt\>);

Arguments:

alpha \<aval\> - The alpha value to format.

alpha \<fmt\> - A valid format for a choice variable.

Returns:

alpha \<aret\> - The formatted value.

Where Used:

sys.fmt_choice() can be called from anywhere.

Example:


    ans = 'y'
    dpyval = sys.fmt_choice(ans,"Yes:No");

Description:

sys.fmt_choice() formats a choice variable using the passed in format.
It stores the formatted value in \<aret\>. \<aval\> is not changed by
sys.fmt_choice().

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
