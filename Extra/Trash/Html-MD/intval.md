<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.int_val()

### sys.int_val()

Purpose:

sys.int_val() converts an alpha character to an integer value.

Usage:

ivar = sys.int_val(\<aval\>);

Arguments:

\<aval\> - The alpha to convert to ascii.

Returns:

\<ivar\> - The integer equivalent of \<aval\>.

There are no error returns.\
\
Only the first char of \<aval\> is used in the conversion. If \<aval\>
is longer than 1 char, then the rest are just ignored.

Where Used:

sys.int_val() can be called from anywhere.

Example:


    /* Convert 1 char to lower case */
    if ((avar(i,i) >= 'A') && (avar(i,i) <= 'Z'))
        avar(i,i) = sys.char_val(sys.int_val(avar(i,i))+32);

Description:

sys.int_val() converts an alpha character to its equivalent integer
value.

Bugs/Features/Comments:

See Also: sys.char_val()

\
\
[Back to Top](#TOPOFPAGE)
