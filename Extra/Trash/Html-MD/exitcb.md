<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.exit_cb()

### sys.exit_cb()

Purpose:

sys.exit_cb() exits out of the current CB processing.

Usage:

sys.exit_cb();

Arguments:

None

Returns:

0 - Normal

-1 - No current CB

Where Used:

sys.exit_cb() can be called from any PCL nested within a CB PCL.

Example:

sys.exit_cb();

Description:

sys.exit_cb() exits out of the current CB processing. This means that
all PCLs started by the current CB will be exited, and that no new PCLs
will be started by the current CB in the CURRENT CB State. sys.exit_cb()
can be used to exit the CBSGROUP, CBEGROUP, CBSELECT, CBBOF, and CBEOF
PCLs. CBBOF/CBSGROUP PCLs and CBEGROUP/CBEOF PCLs act as a group, so
when the CBBOF PCL calls sys.exit_cb(), none of the CBSGROUP PCLs will
be executed on the cur rcd. Likewise, on EOF, when one of the CBEGROUP
PCLs calls sys.exit_cb(), the CBEOF PCL will not get executed.
sys.exit_cb() only acts on the current CB. If there are more than one
active CB for a driver, calling sys.exit_cb() only exits the current CB.
All others will still process. There is no difference between
sys.exit_cb() and sys.end_cb().

Bugs/Features/Comments:

sys.exit_cb() is no different than sys.end_cb(). In the future, they may
be different.

See Also:

[sys.end_cb()](./endcb.html)

\
\
[Back to Top](#TOPOFPAGE)
