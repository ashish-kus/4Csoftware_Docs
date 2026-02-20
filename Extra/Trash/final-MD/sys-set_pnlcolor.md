---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 304
title: "sys.set_pnlcolor"
---
## sys.set_pnlcolor()
### Purpose
sys.set_pnlcolor() changes the background color of a panel.

### Usage
```c
ret = sys.set_pnlcolor(<pnlcdef>,<rgbval>);
```

### Arguments
integer `<pnlcdef>` - Use the C Define for the panel for this arg.

alpha `<rgbval>` - alpha var in "rrr:ggg:bbb" format.

### Returns
0 - OK - Message sent to client to change the background color

-1 - Error, one of:
  - Client version earlier than 4.4.4
  - Current program doesnt have a window.
  - Invalid `<rgbval>`

### Where Used
sys.set_pnlcolor() can be called for any Panel Class program from any PCL except the InitPCL and the ExitPCL.

### Example
```c
ret = sys.set_pnlcolor(PNL_MAIN,"173:216:230");
```

### Description
sys.set_pnlcolor() allows the application to change the background color of a panel at runtime. If the value of `<rgbval>` is "Default", the panel background will be set to the default background color for that panel. Otherwise the panel background will be set to the color corresponding to `<rgbval>`.

### Bugs / Features / Comments
sys.set_pnlcolor() always sends a message to the client. There is no check to see if the panel bg color is already the same as it is being set to.

### See Also
- sys.set_pnlimage()
