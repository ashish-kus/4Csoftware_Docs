<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.utf8_charat()

### sys.utf8_charat()

Purpose:

sys.utf8_charat() returns the utf8 character at \<idx\> in \<utf8str\>

Usage:

utf8char = sys.utf8_charat(\<utf8str\>,\<idx\>);

Arguments:

utf8 \<utf8str\> - A valid UTF8 string

integer \<idx\> - The character, not byte, index into \<utf8str\> to get
the character.

Returns:

utf8 \<utf8char\> - A utf8 string corresponding to a single Unicode
codepoint. \<utf8char\> can be from 0 to 4 bytes. If 0 bytes, then
either \<idx\> was invalid or \<utf8str\> was not a valid UTF8 string.

Where Used:

sys.utf8_charat() can be called from anywhere.

Example:

The demo.utf8.1 has an example of using sys.utf8_charat() in the test1()
PCL

Description:

sys.utf8_charat() returns the utf8 character at \<idx\> in \<utf8str\>.
The single utf8 character can be up to 4 bytes in length.

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
