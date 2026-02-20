<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.put_afield()

### sys.put_afield()

Purpose:

sys.put_afield() stores an alpha value in an alpha field by name.

Usage:

ret = sys.put_afield(\[\<asprog\>\], \<asfilename\>, \<fieldname\>,
\<aval\>);

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

alpha \<aval\> - The alpha value to store in \<fieldname\>.

Returns:

0 - OK - \<aval\> stored in \<fieldname\>

-1 - Error - Either \<asprog\> or \<asfilename\> or \<fieldname\> is
invalid.

Where Used:

sys.put_afield() can be called from anywhere. It may be used in
report/screen writers that do not know what fields they are using until
runtime.

Example:

Description:

sys.put_afield() locates the field identified by \<fieldname\> and
stores \<aval\> in it. sys.put_afield() is meant to be used when you
don't know the field to store into until runtime.

Bugs/Features/Comments:

If \<fieldname\> is not an alpha type, no error is indicated, but no
value is stored either.

See Also:

[sys.get_fmtfield()](./getfmtfield.html)

[sys.get_afield()](./getafield.html)

[sys.get_ffield()](./getffield.html)

[sys.get_ifield()](./getifield.html)

[sys.put_fmtfield()](./putfmtfield.html)

[sys.put_ffield()](./putffield.html)

sys.put_ifield()

\
\
[Back to Top](#TOPOFPAGE)
