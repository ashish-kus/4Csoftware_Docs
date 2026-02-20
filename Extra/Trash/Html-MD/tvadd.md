<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.tv_add()

### sys.tv_add()

Purpose:

sys.tv_add() adds a new item to a TreeView program.

Usage:

sys.tv_add(\<flags\>,\<depth\>, \<label\>, \<normalimage\>,
\<selimage\>);

Arguments:

\<flags\> - Can be combination of TV_DEFAULT, TV_EXPAND and TV_NOEXPAND.

\<depth\> - The depth of this item. You must use 0 for the roots of the
tree.

\<label\> - The text to display with this item.

\<normalimage\> - the name of an image file, if any, to display when
this item is not selected. The name should be relative to the 4c images
directory. The image must reside on the server and it will be copied to
the client when needed and then future uses will get the image file from
the client.

\<selimage\> - the name of an image file, if any, to display when this
item is selected. If blank, then the \<normalimage\> will be used.

Returns:

-1 - Program is not a TreeView program or program is not open yet.

0 - Normal.

Where Used:

sys.tv_add() should be called from the OpenPCL of a TreeView program.

Example:

See the sys.menu.tv bootstrap program for an example of how to use
sys.tv_add().

Description:

sys.tv_add() adds 1 item to the TreeView program at the requested depth.
Items are always added at the bottom of the list.

Bugs/Features/Comments:

See Also:

[sys.tv_getsel()](./tvgetsel.html)

\
\
[Back to Top](#TOPOFPAGE)
