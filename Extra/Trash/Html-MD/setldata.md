<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.set_ldata()

### sys.set_ldata()

Purpose:

sys.set_ldata() sends data to an open LData connection.

Usage:

ret = sys.set_ldata(\<ldname\>, \<flags\>);

Arguments:

\<ldname\> - an alpha var that was used in a previous call to
[sys.open_ldata()](./openldata.html)

\<flags\> - can be one of:

- LD_DEFAULT - Using LD_DEFAULT, sys.set_ldata() will not return until
  the send data has been acknowledged or an error has been returned from
  the external process.
- LD_NOWAIT - Send the data but don't wait for acknowledgement before
  returning. Using LD_NOWAIT is faster but your application will not
  know for sure if the data was accepted by the external process.

Returns:

-1 = Failure and sys.errno will be set. Probably no open LData
connection with name \<ldname\>.

0 - Success

Where Used:

sys.set_ldata() can be called from anywhere.

Example:

Description:

Use sys.set_ldata() to send data to a non onetime LData connection. The
data sent will be copied from the field specified int the
sys.open_ldata() call.

Bugs/Features/Comments:

See Also:

[sys.open_ldata()](./openldata.html)

[sys.close_ldata()](./closeldata.html)

[sys.get_ldata()](./getldata.html)

\
\
[Back to Top](#TOPOFPAGE)
