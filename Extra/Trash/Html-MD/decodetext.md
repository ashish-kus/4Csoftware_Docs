<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.decode_text()

### sys.decode_text()

Purpose:

sys.decode_text() decodes the \<fromtext\> alpha field using the
specified \<encodingmethod\> and returns the decoded text.

Usage:

text = sys.decode_text(\<fromtext\>,\<encodingtype\>);

Arguments:

alpha \<fromtext\> - A 4C alpha field or literal that is encoded.

integer - \<encodingtype\> - This must be one of ENCODE_NONE,
ENCODE_BASE16, ENCODE_BASE64, or ENCODE_BASE64URL

Returns:

"" - Some Error

Any other alpha - \<fromtext\> was decoded successfully.

Where Used:

sys.decode_text() can be called from anywhere.

Example:

Description:

sys.decode_text() decodes the \<fromtext\> using the specified
\<encodingmethod\> and returns the result as an alpha variable. The
\<fromtext\> 4C field is not modified by sys.decode_text.

Requirements

Requires version 5.0 or higher of 4csrvr.

Bugs/Features/Comments:

See Also:

[sys.encode_file()](./encodefile.html)

[sys.decode_file()](./decodefile.html)

[sys.encode_text()](./encodetext.html)

[sys.decode_text()](./decodetext.html)

\
\
[Back to Top](#TOPOFPAGE)
