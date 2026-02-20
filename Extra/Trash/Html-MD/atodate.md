<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

atodate()

### atodate()

Purpose:

atodate() converts an alpha date to the internal integer format.

Usage:

idate = atodate(\<adate\>);

Arguments:

alpha \<adate\> - An alpha date in "mm/dd/yy" or "mm/dd/yyyy" format.

Returns:

date \<idate\> - internal date - which is an integer.

\> 0 - The internal date representation of \<adate\>

0 - Error - bad format or Illegal date.

Where Used:

atodate() can be called from anywhere.

Example:

Description:

atodate() converts an alpha date to the 4C date format. The 4C date
format is an integer representing the number of days since Dec 31, 1799.
Thus, Jan 1, 1800 is represented by 1. 4C Does not deal with dates
earlier than Jan 1, 1800.

Bugs/Features/Comments:

There is no way to specify the \<adate\> in anything besides American
date format.

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
