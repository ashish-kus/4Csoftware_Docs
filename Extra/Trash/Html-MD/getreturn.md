<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_return()

### sys.get_return()

Purpose:

sys.get_return() returns the value of the 4C environment variable
XLRETURN.

Usage:

retsel = sys.get_return();

Arguments:

None

Returns:

alpha \<retsel\>

"SELECT" - The return key will select the rcd in select screens.

"NOSELECT" - The return key will not select the rcd in select screens.
Only the \<accept\> key will select the rcd.

Where Used:

sys.get_return() can be called from anywhere. It is most likely used in
system programs that may allow the user to change the value.

Example:

In the system program sys.help.set, the Init PCL calls sys.get_return()
in order to display the current value before allowing the user to change
it. The entire Init PCL follows:\
\


    helpmsg = sys.get_help();
    fkhelp = sys.get_fkhelp();
    msgl1 = sys.get_msgline1();
    msgl2 = sys.get_msgline2();
    retsel = sys.get_return();

Description:

sys.get_return() returns the value of the 4C environment variable
XLRETURN. This env variable is used to control how a select screen acts
when a \<RETURN\> is typed. If sys.get_return() returns "SELECT", then a
select screen will treat the \<RETURN\> key like accept. Otherwise, it
will not. This may or may not be set in the users shell environment.
Even if set, it could be different, because sys.set_return() will not
affect the shell environment.

Bugs/Features/Comments:

The values stored in the 4C Environment variables may be different than
those at the shell. Calls to sys.set_help() etc do not modify the
shell's environment, only 4C's internal copy. Even shells started from
4C will not share the same environment if the 4C environment has changed
during running.\
\
Of Course this is subject to change.

See Also: sys.get_fkhelp() sys.get_help() sys.get_msgline1()
sys.get_msgline2() sys.set_fkhelp() sys.set_help() sys.set_msgline1()
sys.set_msgline2() sys.set_return()

\
\
[Back to Top](#TOPOFPAGE)
