<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.create_tfile()

### sys.create_tfile()

Purpose:

sys.create_tfile() creates a temporary file on disk.

Usage:

ret = sys.create_tfile(\<asfile\>);

Arguments:

file \<asfile\> - The asfile name of the file to create.

Returns:

0 - Temp File create ok

-1 - Some error, msg displayed, and file NOT created.

Where Used:

sys.create_tfile() can be called from anywhere.

Example:

The bootstrap program sys.filedoc.s creates a temporary file using the
template of sys.file_temp. It does it with the following statement taken
from filelist().\
\
sys.create_tfile(file_temp);\
\
file_temp is defined in sys.filedoc.s in the program file definitions.

Description:

sys.create_tfile() creates a data file in a temp directory. If the file
is already in use by the program creating it, it is closed first. When
the program that creates the temporary file exits, the temporary file is
removed.\
\
sys.create_tfile() can be used to create temporary files when they are
not needed any longer than the life of the program that creates them. If
they cannot be discarded immediately, then sys.create_file() should be
used.\
\
The file being created is created in a temp directory that can be
specified by the user.

Bugs/Features/Comments:

sys.create_tfile() is obsolete - use sys.open_file(\<asfile\>,F_TEMP)
instead.\
\
In order to share the file name across programs, you must specify FULL
SHARE on the Entire File in the program share definition.

See Also:

[sys.create_file()](./createfile.html)

[sys.open_file()](./open_file.html)

\
\
[Back to Top](#TOPOFPAGE)
