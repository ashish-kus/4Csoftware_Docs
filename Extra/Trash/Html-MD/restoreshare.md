<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.restore_share()

### sys.restore_share()

Purpose:

sys.restore_share() resets all or a subset of shared in fields to their
original shared in values

Usage:

ret = sys.restore_share(\[\<filename\>\]);

Arguments:

asfile \<filename\> - Optional arg that limits the restore to fields in
\<filename\>

Returns:

integer \<ret\>

0 - OK - all applicable field values reset to original shared in value

-1 - \<filename\> was specified but not found

Where Used:

sys.restore_share() can be called from anywhere. However, it mostly
makes sense to call it when a program is restarted to restore the
original values of the shared in fields.

Example:

sys.pr.srch.1 calls sys.restore_share(sys.program) in the restart() PCL
in order to restore the original values of fields in sys.program.

Description:

sys.restore_share() resets all or a subset of shared in fields to their
original shared in values

Requirements

4csrvr version 5.2 or later.

Bugs/Features/Comments:

See Also:

[sys.fl_restore()](./flrestore.html)

[sys.fl_save()](./flsave.html)

[sys.get_saveval()](./getsaveval.html)

\
\
[Back to Top](#TOPOFPAGE)
