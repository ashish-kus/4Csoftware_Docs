<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.run_fldloop()

### sys.run_fldloop()

Purpose:

sys.run_fldloop() allows programmatic switching between option panel fld
loops and the main fldloop.

Usage:

ret = sys.run_fldloop(\<fldidx\>);

Arguments:

integer - \<fldidx\> - The index of a display field in the fldloop that
you want to switch to.

Returns:

integer - \<ret\>

No Return - Fld Loop Switched

-1 - Either the \<fldidx\> is invalid or \<fldidx\> is in the current
executing fld loop.\

Where Used:

sys.run_fldloop() can be called any time the current screen program has
at least one option panel.

Example:

Description:

sys.run_fldloop() allows the application to change the current fldloop
to a different fldloop.

Requirements

Both 4csrvr and 4cclient version 5.2 and later are required.

Bugs/Features/Comments:

See Also:

[4C Panels Documentation](../Features/Panels/index.html)

\
\
[Back to Top](#TOPOFPAGE)
