<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.fl_restore()

### sys.fl_restore()

Purpose:

sys.fl_restore() - restore one or more fields for 1 asfile from a
previously saved value.

Usage:

ret = sys.fl_restore(\[\<name\>,\]\<asfile\> \[,\<sfldidx\> \[,
\<efldidx\]\]);

Arguments:

alpha \<name\> - An optional name that identifies a previous save.

asfile \<asfile\> - The asfile with previously saved fields to restore
fields to

integer \<sfldidx\> - Optional start fld idx in \<asfile\> to restore.

integer \<efldidx\> - Optional end fld idx in \<asfile\> to restore.

Returns:

0 - File Variables restored to previously saved values.

-1 - Invalid \<asfile\>

Where Used:

sys.fl_restore() can be called from anywhere.

Example:

Example

Description:

sys.fl_restore() can be used to restore previously saved values of
fields from a single asfile back to the same asfile.

Requirements

sys.fl_save() Requires version 5.2 or higher 4C Server.

Bugs/Features/Comments:

Restoring fld values that haven't been previously saved using
sys.fl_save() is not flagged as an error.

See Also:

[sys.fl_restore()](./flsave.html)

[sys.restore_share()](./restoreshare.html)

[sys.get_saveval()](./getsaveval.html)

\
\
[Back to Top](#TOPOFPAGE)
