<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.close_ldata()

### sys.close_ldata()

Purpose:

sys.close_ldata() closes an open LData connection.

Usage:

ret = sys.close_ldata(\<ldname\>);

Arguments:

\<ldname\> - an alpha var that was used in a previous call to
[sys.open_ldata()](./openldata.html)

Returns:

-1 = Failure and sys.errno will be set. Probably no open LData
connection with name \<ldname\>.

0 - Success

Where Used:

sys.close_ldata() can be called from anywhere.

Example:

Description:

Use sys.close_ldata() to close non onetime LData connections with
external processes.

Bugs/Features/Comments:

See Also:

[sys.open_ldata()](./openldata.html)

[sys.get_ldata()](./getldata.html)

[sys.set_ldata()](./setldata.html)

\
\
[Back to Top](#TOPOFPAGE)
