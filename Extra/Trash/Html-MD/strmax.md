<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

strmax()

### strmax()

Purpose:

strmax() returns the maximum alpha of its arguments.

Usage:

maxval = strmax(\<arg1\> \[,\<arg2\> \[,..., \[\<arg16\>\] \] ... \]);

Arguments:

alpha \<arg1\>-\<arg16\> - The alphas to compare and get the max of.

Returns:

alpha \<maxval\> - The maximum of all passed args.

Where Used:

strmax() can be called from anywhere.

Example:

Description:

strmax() returns the maximum alpha of its arguments. The comparison is a
standard lexical comparison.

Bugs/Features/Comments:

Prior to 4C Server version 4.4.7 strmax() is not reliable. Do not use
strmax() unless your server is version 4.4.7 or higher.

See Also: max() min() strmin() strlen()

\
\
[Back to Top](#TOPOFPAGE)
