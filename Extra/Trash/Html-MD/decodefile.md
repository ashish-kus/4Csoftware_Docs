<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.decode_file()

### sys.decode_file()

Purpose:

sys.decode_file() decodes the \<fromfile\> using the specified
\<encodingmethod\> to \<tofile\>

Usage:

ret = sys.decode_file(\<fromfilename\>,\<tofilename\>,\<encodingtype\>);

Arguments:

alpha \<fromfilename\> - the full pathname of the file you are reading
encoded data from.

alpha \<tofilename\> - the full pathname of the file you are writing the
decoded data to.

integer - \<encodingtype\> - This must be one of ENCODE_NONE,
ENCODE_BASE16, or ENCODE_BASE64

Returns:

0 - File was decoded successfully.

\< 0 - Some Error

Where Used:

sys.decode_file() can be called from anywhere.

Example:

Description:

sys.decode_file() decodes the \<fromfile\> using the specified
\<encodingmethod\> to \<tofile\> The \<fromfile\> is not modified by
sys.encode_file.

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
