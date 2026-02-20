---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 30
title: "sys.cbp_getport"
---
## sys.cbp_getport()
### Purpose
sys.cbp_getport() returns the port number of the 4csrvr where 4C data was copied from.

### Usage
\<portno\> = `sys.cbp_getport();`

### Arguments
None

### Returns
integer - \<portno\>

-1 - No 4C Format Paste Available.

> 0 - The port number of 4csrvr originating the copy.

### Where Used
`sys.cbp_getport()` can be called from anywhere as long as at least one paste operation has been done by the user.

### Example
None

### Description
sys.cbp_getport() returns the port number of the 4csrvr where 4C data was copied from. If the paste did not originate from a 4C application, then the port num will not be known and -1 will be returned.

### Bugs / Features / Comments
None

### See Also
- Cut/Copy/Paste Overview
- `sys.cbp_getappname()`
- `sys.cbp_getipaddr()`
