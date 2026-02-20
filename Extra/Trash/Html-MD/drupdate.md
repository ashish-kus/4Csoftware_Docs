<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.dr_update()

### sys.dr_update()

Purpose:

sys.dr_update() updates the fields in a driver temp file.

Usage:

sys.dr_update();

Arguments:

None

Returns:

0 - OK

-1 - Error

Where Used:

sys.dr_update() can be called by the application any time there is a
current 4c driver record.

Example:

Description:

sys.dr_update() is useful to update fields in a driver temp file that
have been dr included in the driver. It does not modify the driver file
itself, only the temp file used by the driver.

Requirements

sys.dr_update() requires the 4c server to be at version 5.6.8 or higher.

Bugs/Features/Comments:

See Also:

[sys.dr_update()](./drupdate.html)

\
\
[Back to Top](#TOPOFPAGE)
