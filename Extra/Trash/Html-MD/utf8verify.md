<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.utf8_verify()

### sys.utf8_verify()

Purpose:

sys.utf8_verify() verifys that all bytes in \<utf8str\> are valid and
returns 0 if they are and -1 if they are not.

Usage:

ret = sys.utf8_verify(\<utf8str\>);

Arguments:

utf8 \<utf8str\> - A string of bytes that may or may not be a valid utf8
str.

Returns:

integer \<ret\> - 0 if \<utf8str\> is a valid UTF8 string, -1 if not

Where Used:

sys.utf8_verify() can be called from anywhere.

Example:

Description:

sys.utf8_verify() verifys that all bytes in \<utf8str\> are valid and
returns 0 if they are and -1 if they are not. When -1 is returned, the
byte index into \<utf8str\> of the start of the 1st invalid utf8
character is saved in sys_ret.

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
