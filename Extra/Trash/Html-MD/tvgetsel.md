<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.tv_getsel()

### sys.tv_getsel()

Purpose:

sys.tv_getsel() returns the index of the currently selected item for the
TreeView program.

Usage:

idx = sys.tv_getsel();

Arguments:

None

Returns:

-1 - Program is not a TreeView program or program is not open yet. 0 -
OK

Where Used:

sys.tv_getsel() should be used in the TVSelectPCL or the TVActionPCL.

Example:

See the sys.menu.tv program for an example of how to use
sys.tv_getsel().

Description:

sys.tv_getsel() returns the index of the currently selected item for the
TreeView program. The index is based on the order the items were added
to the TreeView program. The first item always has an index of 0 and the
last item always has an index of nitems-1. The easiest way for an
application to know what info goes with a particular item is to build a
temp file, indexed by item idx, while adding items to the TreeView
program. Sys.tv_getsel() can then be used to set the key for the temp
file when the TVSelectPCL or TVActionPCL is executed.

Bugs/Features/Comments:

See Also:

[sys.tv_add()](./tvadd.html)

\
\
[Back to Top](#TOPOFPAGE)
