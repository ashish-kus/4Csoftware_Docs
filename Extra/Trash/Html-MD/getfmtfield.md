<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_fmtfield()

### sys.get_fmtfield()

Purpose:

sys.get_fmtfield() formats a field and stores the formatted field in the
\<retbuf\> arg.

Usage:

ret = sys.get_fmtfield(\[\<asprog\>\], \<asfilename\>, \<fieldname\>,
\<retbuf\>);

Arguments:

asprog \<asprog\> - The asprog name of the program to use to find
\<asfilename\> and \<fieldname\>.\
\
This is an optional argument, and if not used, the current program is
assumed.

alpha \<asfilename\> - The asfile name of the file containing
\<fieldname\>.

alpha \<fieldname\> - The name of the field you want to format. This
must be passed in quotes, or in an alpha variable. Dimesioned variables
can be used also using a format like "field\[n\]"

alpha \<retbuf\> - The alpha field where 4C will store the formatted
field. This field is passed by name and should not be quoted.

Returns:

0 - OK - the formatted value of \<fieldname\> is in \<retbuf\>.

-1 - Error - Either \<asprog\> or \<asfilename\> or \<fieldname\> is
invalid.

Where Used:

sys.get_fmtfield() can be called from anywhere. It is useful in programs
that are report/screen writers and you don't know what is to be
displayed until runtime.

Example:

There are several examples in the 4C debugger program sys.dbg.fld.det.

Description:

sys.get_fmtfield() formats a field and stores the formatted field in the
\<retbuf\> arg.

Bugs/Features/Comments:

Only the format that is defined for \<fieldname\> in the data dictionary
is used. You cannot specify another format.

See Also:

[sys.get_afield()](./getafield.html)

[sys.get_ffield()](./getffield.html)

[sys.get_ifield()](./getifield.html)

[sys.put_fmtfield()](./putfmtfield.html)

[sys.put_afield()](./putafield.html)

[sys.put_ffield()](./putffield.html)

sys.put_ifield()

\
\
[Back to Top](#TOPOFPAGE)
