<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_dfrow()

### sys.get_dfrow()

Purpose:

sys.get_dfrow() returns the row number that a particular field is
displayed on.

Usage:

row = sys.get_dfrow(\<DFLABEL\>);

Arguments:

integer \<DFLABEL\> - the unique label id of the display field. This is
in the display field specs and normally is upper case.

Returns:

integer \<row\>

\> 0 - row number of field.

-1 - No current program or illegal DFLABEL

Where Used:

sys.get_dfrow() can be called from anywhere and would normally be used
to pass a row ofst to another program to help it position itself.

Example:

The sys.fh.maint program uses the following code to tell
sys.prreset.type to position itself below FILENAME.\
\


    type = sys_prresettype(
             sys.get_dfrow(FILENAME),
             sys.get_dfcol(FILENAME)-1);

\
\
Note: sys_prresettype() is a global PCL that pushes sys.prreset.type
passing the row and col as alpha strings.

Description:

sys.get_dfrow() returns the row number that a particular field is
displayed on. The row returned is the actual row, which may differ from
the defined row in the display field definitions. In the case of
scrolling programs, the row returned for a multi field corresponds to
the row for the current item. For screen programs using sys.dr_epedit(),
or sys.dr_epselect1() this item is normally highlighted.

Bugs/Features/Comments:

See Also: sys.get_dfcol() sys.get_linenum()

\
\
[Back to Top](#TOPOFPAGE)
