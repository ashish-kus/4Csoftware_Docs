<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.set_sortdf()

### sys.set_sortdf()

Purpose:

sys.set_sortdf() sets a bitmap on the column label of a listview column
to indicate that the list is sorted on that field in either ascending or
descending order.

Usage:

ret = sys.set_sortdf(\<dfldcdef\>,\<sortflag\>);

Arguments:

integer \<dfldidx\> - The CDEF for the display field.

integer \<sortflag\> - Either SORT_NORMAL or SORT_REVERSE

Returns:

-1 - Not a scrolling program or no such dfldidx.

Where Used:

sys.set_sortdf() will normally be called from the DrInit PCL of a
scrolling panel program with a listview panel.

Example:

The bootstrap program sys.df.fm.pnl uses sys.set_sortdf().

Description:

sys.set_sortdf() sets a bitmap on the column label of a listview column
to indicate that the list is sorted on that field in either ascending or
descending order.

Bugs/Features/Comments:

See Also:

\
\
[Back to Top](#TOPOFPAGE)
