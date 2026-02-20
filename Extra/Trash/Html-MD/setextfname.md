<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.set_extfname()

### sys.set_extfname()

Purpose:

sys.set_extfname() allows you to set the external file name of a file.

Usage:

sys.set_extfname(\<asfile\>,\<extfname\>);

Arguments:

asfile \<asfile\> - The asfile name of the file to set the extname of.

alpha \<extfname\> - The new external name to use.

Returns:

None

Where Used:

sys.set_extfname() can be called from anywhere. However, it will
probably be called before any rcd accesses are made.

Example:

Description:

sys.set_extfname() allows you to set the external name of a file. The
external name can be any name valid in the fiel definition. This
includes directory names, environment variables, and absolute path
names. sys.set_extfname() closes the file if it is open to this program.
The next rcd access will cause the file to be opened using the the new
name. If there is a problem with the new name, it will show up when the
file is re-opened. All other programs using the same file will continue
with the same external name they were using before. The only programs
that are affected by the new name besides the current program are
programs that are started AFTER the sys.set_extfname() call AND share
the file FULL.

Bugs/Features/Comments:

No checking to see if name is valid is done

See Also:

[sys.open_file()](./openfile.html)

[sys.ext_filename()](./extfilename.html)

\
\
[Back to Top](#TOPOFPAGE)
