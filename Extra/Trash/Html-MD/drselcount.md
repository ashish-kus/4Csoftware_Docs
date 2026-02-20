<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.dr_selcount()

### sys.dr_selcount()

Purpose:

sys.dr_selcount() returns the number of selected items to the
application.

Usage:

nitems = sys.dr_selcount();

Arguments:

None

Returns:

The number of currently selected items in a scrolling list.

Where Used:

sys.dr_selcount() is normally used when the user presses an fkey or
cmdbtn and the application wants to process each selected record.

Example:

The system programs sys.df.maint1, scf.fm, and scp.fm have examples of
using sys.dr_selcount().

Description:

sys.dr_selcount() returns the number of items selected when the user
last pressed an fkey or cmdbtn. 4C works with a set of items that is
comprised of the items currently selected when the user pressed an fkey
or cmdbtn. Even if you change the selection status of any items in this
set, the set itself will not change until another fkey or cmdbtn is
pressed by the user.

Bugs/Features/Comments:

See Also:

[sys.dr_readsel()](./drreadsel.html)

[sys.dr_setsel()](./drsetsel.html)

\
\
[Back to Top](#TOPOFPAGE)
