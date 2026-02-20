<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.utf8_tocp()

### sys.utf8_tocp()

Purpose:

sys.utf8_tocp() returns the 32bit integer codepoint for the utf8
character starting at byte 0 int \<utf8char\>

Usage:

cp = sys.utf8_tocp(\<utf8char\>);

Arguments:

utf8 \<utf8char\> - A single utf8 character byte string

Returns:

integer \<cp\> - The unicode code point for the utf8 char starting at
byte 0 in \<utf8char\> or -1 if the first byte is teh start of an
invalid utf8 character.

Where Used:

sys.utf8_tocp() can be called from anywhere.

Example:

The demo.test.1 program has an example of using sys.utf8_tocp()

Description:

sys.utf8_tocp() returns the 32bit integer codepoint for the utf8
character starting at byte 0 int \<utf8char\> If the return is \>= 0,
then \<utf8char\> corresponded to the start of a valid UTF8 character
and the number of bytes in that character is then stored in sys_ret. If
the codepoint returned is less than 0, then the first byte in
\<utf8char\> was not the beginning of a valid UTF8 character

Requirements

4csrvr 6.4.3 or later

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
