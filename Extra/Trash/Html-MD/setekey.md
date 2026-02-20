<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.set_ekey()

### sys.set_ekey()

Purpose:

sys.set_ekey() sets the end position for sequential reads.

Usage:

ret = sys.set_ekey(\<asfile\>,\<fldcdef\>,\<matchtype\>);

Arguments:

asfile - \<asfile\> - The asfile name of the file you are setting the
end key pos for.

integer \<fldcdef\> - The cdef of the fld you want to seek to.

integer \<matchflag\> - Either MATCH_FULL or MATCH_PARTIAL

Returns:

0 - End Pos Set OK

-1 - Some Error

Where Used:

sys.set_ekey() will typically be called before reading a file
sequentially.

Example:

See the demo.seekkey.1 demo program for an example.

Description:

sys.set_ekey() sets the end position for sequential reading of a file.
It is typically used along with sys.set_skey(), and sys.seek_key()
before calling sys.read_file(...,F_SEQNEXT). Before calling
sys.set_ekey() set values into the fields that need them.

Bugs/Features/Comments:

See Also:

[sys.set_skey()](./setskey.html)

[sys.seek_key()](./seekkey.html)

[sys.read_file()](./readfile.html)

\
\
[Back to Top](#TOPOFPAGE)
