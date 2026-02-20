<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.cp_toutf8()

### sys.cp_toutf8()

Purpose:

sys.cp_toutf8() converts 1 to 30 32 bit integer Unicode Codepoints to
one UTF8 string.

Usage:

utf8str = sys.cp_toutf8(\<cp01\> \[,\<cp02\> ... ,\<cp30\> \]);

Arguments:

integer \<cpNN\> - Any valid Unicode 32bit codepoint.

Returns:

utf8 \<utf8str\> - A valid UTF8 string

Where Used:

sys.cp_toutf8() can be called from anywhere.

Example:

The demo.utf8.1 program, though silly and pointless, has several
examples of using sys.cp_toutf8(\_ to create UTF8 strings.

Description:

sys.cp_toutf8() converts 1 to 30 32 bit integer Unicode Codepoints to
one UTF8 string. The total number of bytes in the returned utf8 string
is stored in sys_ret.

Requirements

4csrvr version 6.4.3 or later.

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
