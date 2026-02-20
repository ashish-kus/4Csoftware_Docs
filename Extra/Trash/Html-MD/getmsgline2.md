<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_msgline2()

### sys.get_msgline2()

Purpose:

sys.get_msgline2() returns the value of the 4C environment variable
XLMSGLINE2.

Usage:

msgline2 = sys.get_msgline2();

Arguments:

None

Returns:

integer \<msgline2\>

\> 0 - The 4C Message Line Number Two

Where Used:

sys.get_msgline2() can be called from anywhere. It is most likely used
in system programs that may allow the user to change the value.

Example:

In the system program sys.help.set, the Init PCL calls
sys.get_msgline2() in order to display the current value before allowing
the user to change it. The entire Init PCL follows:\
\


    helpmsg = sys.get_help();
    fkhelp = sys.get_fkhelp();
    msgl1 = sys.get_msgline1();
    msgl2 = sys.get_msgline2();
    retsel = sys.get_return();

Description:

sys.get_msgline2() returns the value of the 4C environment variable
XLMSGLINE2. This env variable is used to control where 4C displays fkey
help messages. This is normally one of the last two lines available on
the screen.

Bugs/Features/Comments:

The values stored in the 4C Environment variables may be different than
those at the shell. Calls to sys.set_help() etc do not modify the
shell's environment, only 4C's internal copy. Even shells started from
4C will not share the same environment if the 4C environment has changed
during running.\
\
Of Course this is subject to change.

See Also: sys.get_fkhelp() sys.get_help() sys.get_msgline1()
sys.get_return() sys.set_fkhelp() sys.set_help() sys.set_msgline1()
sys.set_msgline2() sys.set_return()

\
\
[Back to Top](#TOPOFPAGE)
