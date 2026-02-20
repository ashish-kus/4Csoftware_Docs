<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.null_file()

### sys.null_file()

Purpose:

sys.null_file() sets all file variables for file to a blank or 0.

Usage:

ret = sys.null_file(\<asfile\>);

Arguments:

asfile \<asfile\> - The asfile name of the file to null.

Returns:

0 - OK

-1 - Invalid \<asfile\>

Where Used:

sys.null_file() can be called from anywhere.

Example:

Description:

sys.null_file() sets all file variables for \<asfile\> to an empty
string for alpha file variables and to a 0 for numeric file variables.
sys.null_file() does not modify any permanent data. All modification is
done on the file variables in memory.

Bugs/Features/Comments:

See Also:

[sys.null_data()](./nulldata.html)

[sys.null_field()](./nullfield.html)

\
\
[Back to Top](#TOPOFPAGE)
