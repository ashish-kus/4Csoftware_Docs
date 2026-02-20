<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.put_fmtfield()

### sys.put_fmtfield()

Purpose:

sys.put_fmtfield() converts an alpha to the appropriate type and stores
it in a field.

Usage:

ret = sys.put_fmtfield(\[\<asprog\>\], \<asfilename\>, \<fieldname\>,
\<fmtval\>);

Arguments:

asprog \<asprog\> - The asprog name of the program to use to find
\<asfilename\> and \<fieldname\>.\
\
This is an optional argument, and if not used, the current program is
assumed.

alpha \<asfilename\> - The asfile name of the file containing
\<fieldname\>. This must be passed in quotes, or in an alpha variable.

alpha \<fieldname\> - The name of the field you want to store the value.
This must be passed in quotes, or in an alpha variable. Dimesioned
variables can be used also using a format like "field\[n\]"

alpha \<fmtval\> - The formatted value to convert and store in
\<field\>. This field is passed by name and should not be quoted.

Returns:

0 - OK - \<fmtval\> converted and stored in \<fieldname\>

-1 - Error - Either \<asprog\> or \<asfilename\> or \<fieldname\> or
\<fmtval\> is invalid.

Where Used:

sys.put_fmtfield() can be called from anywhere. It is used in the 4C
debugger programs to allow you to change the value of fields in running
programs.

Example:

There are several examples in the 4C debugger program sys.dbg.fld.det.

Description:

sys.put_fmtfield() converts an alpha to the appropriate type and stores
the converted value in \<field\>.

Bugs/Features/Comments:

See Also:

[sys.get_fmtfield()](./getfmtfield.html)

[sys.get_afield()](./getafield.html)

[sys.get_ffield()](./getffield.html)

[sys.get_ifield()](./getifield.html)

[sys.put_afield()](./putafield.html)

[sys.put_ffield()](./putffield.html)

sys.put_ifield()

\
\
[Back to Top](#TOPOFPAGE)
