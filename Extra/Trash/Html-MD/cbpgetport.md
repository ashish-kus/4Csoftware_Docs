<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.cbp_getport()

### sys.cbp_getport()

Purpose:

sys.cbp_getport() returns the port number of the 4csrvr where 4C data
was copied from.

Usage:

\<portno\> = sys.cbp_getport();

Arguments:

None

Returns:

integer - \<portno\>

-1 - No 4C Format Paste Available.

\> 0 - The port number of 4csrvr originating the copy.

Where Used:

sys.cbp_getportno() can be called from anywhere as long as at least one
paste operation has been done by the user.

Example:

Description:

sys.cbp_getport() returns the port number of the 4csrvr where 4C data
was copied from. If the paste did not originate from a 4C application,
then the port num will not be known and -1 will be returned.

Bugs/Features/Comments:

See Also:

[Cut/Copy/Paste Overview](../Features/cutpaste.html)

[sys.cbp_getappname()](./cbpgetappname.html)

[sys.cbp_getipaddr()](./cbpgetport.html)

\
\
[Back to Top](#TOPOFPAGE)
