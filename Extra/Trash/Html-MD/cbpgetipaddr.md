<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.cbp_getipaddr()

### sys.cbp_getipaddr()

Purpose:

sys.cbp_getipaddr() returns the ipaddr of the 4csrvr where 4C data was
copied from.

Usage:

ipaddr = sys.cbp_getipaddr();

Arguments:

None

Returns:

alpha \<ipaddr\>

"" - No 4C Format Paste Available.

ipaddr - The ipaddr of 4csrvr originating the copy.

Where Used:

sys.cbp_getipaddr() can be called from anywhere as long as at least one
paste operation has been done by the user.

Example:

Description:

sys.cbp_getipaddr() returns the ipaddr of the 4csrvr where 4C data was
copied from. If the paste did not originate from a 4C application, then
the ip address will not be known and an empty string will be returned.

Bugs/Features/Comments:

See Also:

[Cut/Copy/Paste Overview](../Features/cutpaste.html)

[sys.cbp_getappname()](./cbpgetappname.html)

[sys.cbp_getport()](./cbpgetport.html)

\
\
[Back to Top](#TOPOFPAGE)
