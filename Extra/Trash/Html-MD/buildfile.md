<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.build_file()

### sys.build_file()

Purpose:

sys.build_file() compiles a files.

Usage:

ret = sys.build_file(\<filename\>);

Arguments:

alpha \<filename\> - The name of the file to build. This is the name of
the file defined in the data dictionary and has nothing to do with any
asfiles defined for any program.

Returns:

integer \<ret\>

0 - OK

-1 - Error - Probably no such file or compile error, a message has been
displayed.

Where Used:

sys.build_file() can be called from anywhere. It most likely will be
called from system development programs, and not from other application
programs.

Example:

The sys.fh.maint program uses the \<user15\> key to compile a file. The
PCL associated with this key is:\
\


    sys.build_file(sys.fh_fname);

Description:

sys.build_file() compiles the named file. Any errors during compilation
cause an appropriate message to be displayed, and for sys.build_file()
to return -1.\
\
4C does not compile files in the sense that machine code is generated.
4C reads the data dictionary spec files and converts them into easy to
interpret tables and stores the result in the XLSEQFILE. It does the
same with programs. The terms build and compile will be used to both
mean read the 4C specs and write the XLSEQFILE tables.

Bugs/Features/Comments:

See Also:

[sys.build_prog()](./buildprog.html)

[sys.reset_prog()](./resetprog.html)

\
\
[Back to Top](#TOPOFPAGE)
