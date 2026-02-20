<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

pclname()

### pclname()

Purpose:

sys.utf8_fix() replaces invalid byte sequences in \<utf8str\> with
\<repchar\>, or with '?' if \<repchar\> is not specified, and returns
the modified UTF8 string

Usage:

utf8str2 = sys.utf8_fix(\<utf8str\> \[, \<repchar\>\]);

Arguments:

utf8 \<utf8str\>

alpha \<repchar\> - optional arg that must be a 7bit ascii char. If none
specified, the '?' is used as the replacement character.

Returns:

utf8 \<utf8str2\> - A valid UTF8 string.

Where Used:

sys.utf8_fix() can be called from anywhere.

Example:

Description:

sys.utf8_fix() replaces invalid byte sequences in \<utf8str\> with
\<repchar\>, or with '?' if \<repchar\> is not specified, and returns
the modified UTF8 string If repchar is longer than a single character,
only the first character is used to replace invalid bytes in \<utf8str\>

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
