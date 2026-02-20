<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.put_ffield()

### sys.put_ffield()

Purpose:

sys.put_ffield() stores a float value in a float field by name.

Usage:

ret = sys.put_ffield(\[\<asprog\>\], \<asfilename\>, \<fieldname\>,
\<fval\>);

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

float \<fval\> - The float value to store in \<fieldname\>.

Returns:

0 - OK - \<fval\> stored in \<fieldname\>

-1 - Error - Either \<asprog\> or \<asfilename\> or \<fieldname\> is
invalid.

Where Used:

sys.put_ffield() can be called from anywhere. It may be used in
report/screen writers that do not know what fields they are using until
runtime.

Example:

Description:

sys.put_ffield() locates the field identified by \<fieldname\> and
stores \<fval\> in it. sys.put_ffield() is meant to be used when you
don't know the field to store into until runtime.

Bugs/Features/Comments:

If \<fieldname\> is not a float type, no error is indicated, but no
value is stored either.

See Also:

[sys.get_fmtfield()](./getfmtfield.html)

[sys.get_afield()](./getafield.html)

[sys.get_ffield()](./getffield.html)

[sys.get_ifield()](./getifield.html)

[sys.put_fmtfield()](./putfmtfield.html)

[sys.put_afield()](./putafield.html)

sys.put_ifield()

\
\
[Back to Top](#TOPOFPAGE)
