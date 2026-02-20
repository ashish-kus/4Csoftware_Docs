<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.fmt_time()

### sys.fmt_time()

Purpose:

sys.fmt_time() formats a time variable

Usage:

aret = sys.fmt_time(\<tmval\>,\<fmt\>);

Arguments:

time \<tmval\> - The time value to format.

alpha \<fmt\> - A valid format for a time variable.

Returns:

alpha \<aret\> - The formatted value.

Where Used:

sys.fmt_time() can be called from anywhere.

Example:


    tm = (14 * 60 * 60) + (32 * 60) + 24;
    dpyval = sys.fmt_time(tm,"HH:mm:ss");

Description:

sys.fmt_time() formats a time variable using the passed in format. It
stores the formatted value in \<aret\>. \<tmval\> is not changed by
sys.fmt_time().

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
