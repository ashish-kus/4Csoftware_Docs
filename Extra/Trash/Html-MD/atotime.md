<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

atotime()

### atotime()

Purpose:

atotime() converts a string to a 4C time.

Usage:

tval = atotime(\<timestr\>);

Arguments:

alpha \<timestr\> - An alpha representation of a time.

Returns:

-1 - Invalid time string \>= 0 - The 4c time.

Where Used:

atotime() can be called from anywhere.

Example:

Example

Description:

atotime() converts a string to a 4c time value similar. It is fairly
flexible, but expects the \<timestr\> to have only digits, spaces, ':'s
and an optional "am", "a", "pm" or "p" suffix.

Requirements

4cserver version 6.4.7 or later.

Bugs/Features/Comments:

Bugs

See Also:

[atodate()](./atodate.html)

[](./atotime.html)

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
