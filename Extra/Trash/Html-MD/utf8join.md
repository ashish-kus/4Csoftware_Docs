<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

pclname()

### pclname()

Purpose:

sys.utf8_join() joins the elements in either a utf8 character array or a
unicode codepoint array and returns a new utf8 string.

Usage:

\<utf8str\> = sys.utf8_join(\<array\[idx\]\> \[ , \<maxelements\> \]);

Arguments:

utf8 OR integer \<array\[idx\]\> - The starting element of either a UTF8
character array or a Unicode codepoint array

integer \<maxelements\> - Optional argument that specifies the maximum
number of elements from the array to join. If not specified, then all
elements starting at index \<idx\> until the end of the array are
joined.

Returns:

utf8 \<utf8str\> - The UTF8 string created by joining the elements of
the array into a utf8 string

Where Used:

sys.utf8_join() can be called from anywhere.

Example:

Description:

sys.utf8_join() joins the elements in either a utf8 character array or a
unicode codepoint array and returns a new utf8 string.

Requirements

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
