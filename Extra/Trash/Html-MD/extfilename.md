<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.ext_filename()

### sys.ext_filename()

Purpose:

sys.ext_filename() returns the external name of a 4c file

Usage:

fullpath = sys.ext_filename(\[ \<asprog\>, \] \<asfile\>)

Arguments:

alpha \<asprog\> - Optional asprog name of the program to find
\<asfile\> in. The default is the current program.

asfile \<asfile\> - The 4c asfile to use.

Returns:

alpha \<fullpath\> - The external filename of the file

Where Used:

sys.ext_filename() can be called from anywhere.

Example:

Description:

sys.ext_filename() returns the external name of a 4c file. If the file
is open and the file is a filesystem file, the path returned will
normally be a full pathname to the file. If the file has not been opened
yet, then the path returned will be the exyternal name defined in the 4c
file definition for the file.

Requirements

Bugs/Features/Comments:

See Also:

[sys.open_file()](./openfile.html)

[sys.set_extfname()](./setextfname.html)

\
\
[Back to Top](#TOPOFPAGE)
