<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_asfile()

### sys.get_asfile()

Purpose:

sys.get_asfile() returns the 4C asfile name for \<asfile\>

Usage:

\<name\> = sys.get_asfile(\[ \<asprog\>, \] \<asfile\>);

Arguments:

alpha \<asprog\> - Optional asprog name of the program to find
\<asfile\> in. The default is the current program.

asfile \<asfile\>

Returns:

alpha \<name\>

Where Used:

sys.get_asfile() can be called from anywhere.

Example:

Description:

sys.get_asfile() returns the 4C asfile name for \<asfile\> It can be
useful in PCLs that use an asfile as input parameters. Internally, 4C
saves an asfile as an integer, so this is a way for an application to
determine at runtime what 4C asfile name is associated with a PCL
parameter.

Bugs/Features/Comments:

See Also:

[sys.get_filename()](./getfilename.html)

\
\
[Back to Top](#TOPOFPAGE)
