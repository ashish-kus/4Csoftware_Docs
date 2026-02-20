<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_clpref()

### sys.get_clpref()

Purpose:

sys.get_clpref() returns a client preference to the application.

Usage:

prefval = sys.get_clpref(\<prefflags\>,\<preftype\>);

Arguments:

integer \<prefflags\> - Either PREF_CURRENTUSER or PREF_ALLUSERS

alpha \<preftype\>

Returns:

alpha \<prefval\>

Where Used:

sys.get_clpref() can be called from anywhere during an interactive 4C
session.

Example:

Description:

sys.get_clpref() returns a client preference as a string. The preference
requested can be either a current user preference or an all user
preference. In order to retrieve a preference specific to the current
user, set \<prefflags\> to PREF_CURRENTUSER. In order to retrieve a
preference specific to all users, set \<prefflags\> to PREF_ALLUSERS.
\<preftype\> can be any of the preference names listed in: [Client
Preferences](../Config/cl-pref.html)

Requirements

sys.get_clpref() requires both client and server to be at version 4.4.4
or higher.

Bugs/Features/Comments:

sys.get_clpref() is not supported by the non interactive 4C client,
4ccl.

See Also:

[sys.get_clinfo()](./getclinfo.html)

[sys.set_clpref()](./setclpref.html)

\
\
[Back to Top](#TOPOFPAGE)
