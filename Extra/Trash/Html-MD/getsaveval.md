<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_saveval()

### sys.get_saveval()

Purpose:

sys.get_saveval() returns a single saved variable

Usage:

ret = sys.get_saveval(\[ \<name\>, \] \<var\>);

Arguments:

alpha \<name\> - An optional name that identifies a previous save.

var - \<var\> - A 4C variable of any type

Returns:

Return depends on saved variable type.

Where Used:

sys.get_saveval() can be called from anywhere.

Example:

Description:

sys.get_saveval() will return the saved value of a variable that was
saved using sys.fl_save(). It does not store into the variable itself,
rather it stores into \<ret\>. This makes it easier to compare save
values with current values. You can of course store into the variable
itself explicity.

Requirements

sys.fl_save() Requires version 5.2 or higher 4C Server.

Bugs/Features/Comments:

The only way to verify that there was no error is to check that sys_ret
is equal to SYSRET_OK.

Assigning a saved variable to an incompatible variable (i.e. integer to
alpha) is not flagged as an error.

See Also:

[sys.fl_save()](./flsave.html)

[sys.restore_share()](./restoreshare.html)

[sys.fl_restore()](./flrestore.html)

\
\
[Back to Top](#TOPOFPAGE)
