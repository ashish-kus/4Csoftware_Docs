<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_filename()

### sys.get_filename()

Purpose:

sys.get_filename() returns the 4C filename for \<asfile\>

Usage:

\<filename\> = sys.get_filename(\[ \<asprog\>, \] \<asfile\>);

Arguments:

alpha \<asprog\> - Optional asprog name of the program to find
\<asfile\> in. The default is the current program.

asfile \<asfile\>

Returns:

alpha \<filename\>

Where Used:

sys.get_filename() can be called from anywhere.

Example:

Description:

sys.get_filename() returns the 4C filename for \<asfile\> It can be
useful in PCLs that use an asfile as input parameters. Internally, 4C
saves an asfile as an integer, so this is a way for an application to
determine at runtime what 4C filename is associated with a PCL
parameter.

Bugs/Features/Comments:

See Also:

[sys.get_asfile()](./getasfile.html)

\
\
[Back to Top](#TOPOFPAGE)
