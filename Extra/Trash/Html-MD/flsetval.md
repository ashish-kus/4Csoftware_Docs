<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.fl_setval()

### sys.fl_setval()

Purpose:

sys.fl_setval() - Converts an alpha to the appropriate datatype and
stores it in a file variable.

Usage:

ret = sys.fl_setval(\<asfile\>,\<fldidx\>,\<aval\>);

Arguments:

asfile \<asfile\> - The asfile associated with the file variable you are
setting.

integer \<fldidx\> - The idx of the fld in \<asfile\>. Normally, you
will use the CDEFINE for the fld.

alpha \<aval\> - The value to convert and store into the file variable.

Returns:

-1 - Error - Invalid \<asfile\> or \<fldidx\>

0 - File var set OK

Where Used:

sys.fl_setval() can be called from anywhere.

Example:

The global system PCL sys.rcd_exists() has an example of using
sys.fl_setval().

Description:

sys.fl_setval() converts \<aval\> to the appropriate datatype and stores
it into the file variable associated with \<asfile\> and \<fldidx\>.
This can be useful in situations where you cannot reference a file
variable simply by name as in the case of dynamic files.

Bugs/Features/Comments:

See Also:

[sys.fl_getval()](./flgetval.html)

[sys.get_dfile()](./getdfile.html)

\
\
[Back to Top](#TOPOFPAGE)
