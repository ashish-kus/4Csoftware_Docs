<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.rep_string()

### sys.rep_string()

Purpose:

sys.rep_string() allows you to replace or delete characters from an
alpha var in

Usage:

aval = sys.rep_string(\<rsflags\>,\<originalstring\>,\[ \<matchstr\>, \]
\[ \<repstr\> \]);

Arguments:

integer \<rsflags\> - Any number of predefined flags that can be
combined using the '\|' operator. See below for flag descriptions.

alpha \<originalstring\> - The alpha var to modify

alpha \<matchstring\> - The string, or sometimes the set of characters,
that you want to match in \<originalstring\> \<matchstring\> is optional
when RS_CONVERT is specified but mandatory in all other cases.

alpha \<repstr\> - The string, or sometimes the set of characters, that
are used to replace the matched string or character in
\<originalstring\> \<repstr\> is optional when either RS_SQUEEZE or
RS_CONVERT is specified but mandatory in all other cases.\
\
Allowable sflags are:\
\
RS_DEFAULT - Same as RS_ALL\
\
RS_ALL - Perform replace or squeeze on all matches found in
\<originalstring\>\
\
RS_FIRST - Perform replace or squeeze on only the first match found in
\<originalstring\>\
\
RS_LAST - Perform replace or squeeze on only the last match found in
\<originalstring\>\
\
RS_LEADING - Perform replace or squeeze on only the leading matches
found in \<originalstring\>\
\
RS_TRAILING - Perform replace or squeeze on only the trailing matches
found in \<originalstring\>\
\
RS_ANY - Treat \<matchstr\> as a set of characters to match and replace
rather than as a string to match and replace.\
\
RS_IGNORECASE - Make comparisons ignoring case.\
\
RS_TRANSLATE - Treat both \<matchstr\> and \<repstr\> as sets of
characters rather than strings. When a match is found in \<matchstr\>,
that character is replaced by the character in \<repstring\> at the
index the matching char was found in \<matchstring\>\
\
RS_SQUEEZE - Squeeze multiple sequential occurences of any character in
\<matchstring\> to a single occurence. \<matchstr\> is treated as a set
of characters to match against rather than as a string to match.
\<repstring\>, if specified, is ignored.\
\
RS_CONVERT - Convert all escape sequences in \<originalstring\> to their
character equivalents. i.e. \t gets converted to a real tab character,
\n to a newline, \r to a carriage return, etc. \<matchstr\> and
\<repstr\>, if specified, are both ignored.

Returns:

alpha \<aret\> - The new modified string.

Where Used:

sys.rep_string() can be called from anywhere.

Example:

The Demo application has a simple example in the demo.repstr.1 program.

Description:

sys.rep_string() can be used to delete, replace, or squeeze one or more
occurences of a substring within an alpha variable. The result of the
string manipulation is returned as an alpha variable. The original alpha
is left unchanged unless it is specified as \<aret\>. Some \<rsflag\>
values are incompatible if used together and the resulting string
manipulation done will not be well defined.\
\
Do not use RS_TRANSLATE and RS_SQUEEZE together.\
\
Specifying an empty string for \<repstr\> without RS_TRANSLATE will
delete matching characters or sequences of characters.

Requirements

4C Server Version 5.6.3-03 or higher

Bugs/Features/Comments:

See Also:

[sys.split_string()](./splitstring.html)

[sys.l_strip()](./lstrip.html)

[sys.r_strip()](./rstrip.html)

[sys.l_fill()](./lfill.html)

[sys.r_fill()](./rfill.html)

[toupper()](./toupper.html)

[tolower()](./tolower.html)

[Sys PCLs List](./index.html)

\
\
[Back to Top](#TOPOFPAGE)
