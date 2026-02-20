<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_category()

### sys.get_category()

Purpose:

sys.get_category() returns the category of the current program.

Usage:

catg = sys.get_category();

Arguments:

None

Returns:

alpha \<catg\>

The current programs category as defined in the sys.pr_catg field of
sys.program.

Where Used:

sys.get_category() can be called from anywhere.

Example:

Description:

sys.get_category() returns the category of the current program. The
programs category is defined in the file sys.program by the field
sys.pr_catg. The programs category is not compiled into the XLSEQFILE,
so if you change it, the program does not need to be re-compiled for
sys.get_category() to return the new value.

Bugs/Features/Comments:

See Also: sys.get_field() sys.get_program()

\
\
[Back to Top](#TOPOFPAGE)
