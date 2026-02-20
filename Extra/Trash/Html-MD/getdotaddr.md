<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_dotaddr()

### sys.get_dotaddr()

Purpose:

sys.get_dotaddr() returns the dot address of a client program in
nnn.nnn.nnn.nnn format.

Usage:

dotaddr = sys.get_dotaddr(idx);

Arguments:

integer \<idx\> - The zero based index of the client program.

Returns:

alpha \<dotaddr\> - The dot address of the client program in
nnn.nnn.nnn.nnn format.

Where Used:

sys.get_dotaddr() can be called from anywhere. One place you may want to
use it is in order to get the dotaddr to use in sys.send_msg() calls.

Example:

dotaddr = sys.get_dotaddr(0);

Description:

sys.get_dotaddr() returns the dot address of a client program in
nnn.nnn.nnn.nnn format. This can be used for any client, not just the
client connected to this 4csrvr. The dot address of the current client
is more easily gotten using the system variable sys.cl_dotaddr.

Bugs/Features/Comments:

See Also:

[sys.get_idx()](./getidx.html)

[sys.get_maxusers()](./getmaxusers.html)

[sys.get_nusers()](./getnusers.html)

\
\
[Back to Top](#TOPOFPAGE)
