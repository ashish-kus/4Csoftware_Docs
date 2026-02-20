<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.build_prlist()

### sys.build_prlist()

Purpose:

INTERNAL USE ONLY\
\
sys.build_prlist() builds a list of ALL currently running programs into
a file using the sys.t_prlist file definition.

Usage:

sys.build_prlist(\<t_prlist\>);

Arguments:

file \<t_prlist\> - the asfile name of a file using the sys.t_prlist
definition.

Returns:

0 - OK file built -1 - The asfile passed was not sys.t_prlist

Where Used:

sys.build_prlist() can be called from anywhere. It is meant to be USED
INTERNALLY ONLY and currently is used by the 4C debugger programs.

Example:

The follwing example is from the 4C debugger program sys.dbg.trace. It
is in the init PCL.\
\


    sys.create_tfile(sys.t_prlist);
    sys.build_prlist(sys.t_prlist);

Description:

sys.build_prlist() builds a list of ALL currently running programs into
a file using the sys.t_prlist file definition. This file can then be
read to see which programs are running for the current user.

Bugs/Features/Comments:

Since this is meant for internal use, the file definition may change
when needed.

See Also:

[sys.build_stlist()](./buildstlist.html)

\
\
[Back to Top](#TOPOFPAGE)
