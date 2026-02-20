<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.utf8_count()

### sys.utf8_count()

Purpose:

sys.utf8_count() returns the number UTF8 characters in \<utf8str\>

Usage:

count = sys.utf8_count(\<utf8str\>);

Arguments:

utf8 \<utf8str\> - A valid UTF8 string

Returns:

integer \<count\> - The number of UTF8 characters in \<utf8str\>, -1 for
error

Where Used:

sys.utf8_count() can be called from anywhere.

Example:

See demo.utf8.1 for an example

Description:

sys.utf8_count() returns the number UTF8 characters in \<utf8str\>. If
\<utf8str\> is not a valid UTF8 string, then -1 is returned.

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
