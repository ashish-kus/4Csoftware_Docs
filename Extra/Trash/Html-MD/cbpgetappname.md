<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.cbp_getappname()

### sys.cbp_getappname()

Purpose:

sys.cbp_getappname() returns the 4C application name where 4C data was
copied from.

Usage:

\<appname\> = sys.cbp_getappname();

Arguments:

None

Returns:

alpha \<appname\>

"" - No 4C Format Paste Available.

alpha \<appname\> - The application name originating the copy.

Where Used:

sys.cbp_getappname() can be called from anywhere as long as at least one
paste operation has been done by the user.

Example:

Description:

sys.cbp_getappname() returns the 4C application name where 4C data was
copied from. If the paste did not originate from a 4C application, then
the application name will not be known and an empty string will be
returned.

Bugs/Features/Comments:

See Also:

[Cut/Copy/Paste Overview](../Features/cutpaste.html)

[sys.cbp_getipaddr()](./cbpgetipaddr.html)

[sys.cbp_getport()](./cbpgetport.html)

\
\
[Back to Top](#TOPOFPAGE)
