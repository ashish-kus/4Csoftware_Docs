---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 28
title: "sys.cbp_getipaddr"
---
## sys.cbp_getipaddr()
### Purpose
`sys.cbp_getipaddr()` returns the ipaddr of the 4csrvr where 4C data was copied from.

### Usage
```c
ipaddr = sys.cbp_getipaddr();
```

### Arguments
None

### Returns
alpha <ipaddr>

"" - No 4C Format Paste Available.

ipaddr - The ipaddr of 4csrvr originating the copy.

### Where Used
`sys.cbp_getipaddr()` can be called from anywhere as long as at least one paste operation has been done by the user.

### Example
None

### Description
`sys.cbp_getipaddr()` returns the ipaddr of the 4csrvr where 4C data was copied from. If the paste did not originate from a 4C application, then the ip address will not be known and an empty string will be returned.

### Bugs / Features / Comments
None

### See Also
- Cut/Copy/Paste Overview
- sys.cbp_getappname()
- sys.cbp_getport()
