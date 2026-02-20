<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.set_spcstr()

### sys.set_spcstr()

Purpose:

sys.set_spcstr() allows a program to change the value of a function key
at run time.

Usage:

ret = sys.set_spcstr(\<spcname\>,\<value\>);

Arguments:

alpha \<spcname\> - The name of the spc to set. This will be a key to
the file sys.spc_char.

alpha \<value\> - The new value that this spc has. Characters preceded
by a '\\ or a '^' are treated as control characters and are converted
first.

Returns:

integer \<ret\>

0 - OK

-1 - Probably an illegal \<spcname\>

Where Used:

sys.set_spcstr() can be called from anywhere. It normally would be
called from a program that remaps the function keys to a particular
users liking.

Example:

The sys.spc.ex1 program has the following code in the elp() PCL.\
\


    if (spcstring[12]) {
        sys.set_spcstr("user13",spcstring[12]);
        sys.set_spclabel("user13","F11");
    }

Description:

sys.set_spcstr() changes the escape sequence that 4C is expecting for a
particular function key, such as the \<accept\> key.

Bugs/Features/Comments:

See Also: sys.set_spcstr() sys.set_spclabel() sys.set_spcalt()
sys.get_spcstr() sys.get_spclabel() sys.get_spcalt()

\
\
[Back to Top](#TOPOFPAGE)
