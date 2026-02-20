<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.encode_text()

### sys.encode_text()

Purpose:

sys.encode_text() encodes the \<fromtext\> alpha field using the
specified \<encodingmethod\> and returns the encoded text.

Usage:

etext = sys.encode_text(\<fromtext\>,\<encodingtype\>);

Arguments:

alpha \<fromtext\> - A 4C alpha field or literal.

integer - \<encodingtype\> - This must be one of ENCODE_NONE,
ENCODE_BASE16, ENCODE_BASE64, or ENCODE_BASE64URL

Returns:

"" - Some Error

Any other alpha - \<fromtext\> was encoded successfully.

Where Used:

sys.encode_text() can be called from anywhere.

Example:

Description:

sys.encode_text() encodes the \<fromtext\> using the specified
\<encodingmethod\> and returns the result as an alpha variable. The
\<fromtext\> 4C field is not modified by sys.encode_text.

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
