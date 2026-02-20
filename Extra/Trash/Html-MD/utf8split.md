<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

pclname()

### pclname()

Purpose:

sys.utf8_split() splits a UTF8 string into an array of UTF8 characters
and/or an array of Unicode codepoints.

Usage:

ret = sys.utf8_split(\<utf8str\> \[, \<utf8array\[idx\]\> \] \[,
\<cparray\[idx\]\>\]);

Arguments:

utf8 \<utf8str\> - A valid utf8 string

utf8 \<utf8array\[idx\]\> - The starting item in a utf8array to store
the utf8 characters into

integer \<cparray\[idx\]\> - The starting item in an integer array to
store the codepoints into\
\
Both \<utf8array\[idx\]\> and \<cparray\[idx\]\> are aptional arguments
but at least one of them must be specified.

Returns:

integer \<ret\> - -1 on error, or the total number of items stored in
either of the two arrays passed in.

Where Used:

sys.utf8_split() can be called from anywhere.

Example:

Description:

sys.utf8_split() splits a UTF8 string into an array of UTF8 characters
and/or an array of Unicode codepoints.

Requirements

4csrvr version 6.4.3 or later

Bugs/Features/Comments:

See Also:

[sys.cp_toutf8()](./cptoutf8.html)

[sys.utf8_charat()](./utf8charat.html)

[sys.utf8_count()](./utf8count.html)

[sys.utf8_fix()](./utf8fix.html)

[sys.utf8_join()](./utf8join.html)

[sys.utf8_split()](./utf8split.html)

[sys.utf8_tocp()](./utf8tocp.html)

[sys.utf8_verify()](./utf8verify.html)

\
\
[Back to Top](#TOPOFPAGE)
