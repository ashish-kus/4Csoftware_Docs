<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.rset_dfield()

### sys.rset_dfield()

Purpose:

sys.rset_dfield() resets the data field associated with a display field
to its original value.

Usage:

ret = sys.rset_dfield(\<LABEL\>);

Arguments:

\<LABEL\> - the label of the display field that you want to reset.

Returns:

0 - OK

-1 - no display field with label \<LABEL\>

Where Used:

sys.rset_dfield() can be called from anywhere, but it only makes sense
sometime after sys.set_dfield() has been called.

Example:

Description:

sys.rset_dfield() just resets the display field corresponding to
dfldlabel to be associated with the field defined as the display field.
It only makes sense to use this PCL if previously you have used the
sys.set_dfield() PCL.

Bugs/Features/Comments:

See Also: sys.set_dfield()

\
\
[Back to Top](#TOPOFPAGE)
