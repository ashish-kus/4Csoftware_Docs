<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.char_val()

### sys.char_val()

Purpose:

sys.char_val() converts an integer to an ascii character.

Usage:

avar = sys.char_val(\<ival\>);

Arguments:

\<ival\> - The integer to convert to ascii.

Returns:

\<avar\> - A one character string.

There are no error returns.\
\
\<ival\> will always be converted, even if it is a non-printing
character.

Where Used:

sys.char_val() can be called from anywhere.

Example:


    /* Convert 1 char to lower case */
    if ((avar(i,i) >= 'A') && (avar(i,i) <= 'Z'))
        avar(i,i) = sys.char_val(sys.int_val(avar(i,i))+32);

Description:

sys.char_val() converts an integer to an ascii character. The return
value is always length 1.

Bugs/Features/Comments:

\<ival\> will always be converted, even if it is a non-printing
character.

See Also:

[sys.int_val()](./intval.html)

\
\
[Back to Top](#TOPOFPAGE)
