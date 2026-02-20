<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

index()

### index()

Purpose:

index() returns an integer indicating the relative position that str2 is
found in str1.

Usage:

idx = index(str1,str2);

Arguments:

alpha str1;

alpha str2;

Returns:

-1 - str2 not found in str1

\>= 0 - rel pos of str2 in str1

Where Used:

index() can be called from anywhere.

Example:


    if (index(pattern,answ) < 0) {
            sys.err_msg("Illegal Answer");
            sys.exit_field(sys.cur_field);
    }

Description:

index() returns an integer indicating the relative position that str2 is
found in str1. str2 can be longer than one char, but must be \<= length
of str1. If str2 is null, 0 is returned. If str1 is null, -1 is
returned.

Bugs/Features/Comments:

If str2 is null, 0 is returned. If str1 is null, -1 is returned.

See Also: strlen(), strmax(), strmin()

\
\
[Back to Top](#TOPOFPAGE)
