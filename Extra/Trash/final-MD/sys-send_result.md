---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 270
title: "sys.send_result"
---
## sys.send_result()
### Purpose
sys.send_result() sends results from a 4c web application to the web client.

### Usage
```c
sys.send_result(<srtype>,<srid>,<aval>[,<aval]...);
```

### Arguments
- `<srtype>` - One of SR_DATA or SR_NAMES.
- `<srid>` - an alpha variable that the web client can use to distinguish between different types of results.
- `<aval>` - An alpha data value when using SR_DATA. An name when using SR_NAMES.

### Returns
- 0 - OK
- -1 - Current App is not a Web Application.

### Where Used
sys.send_result() can be called from any Web Application to send data to WebClient.

### Example
None

### Description
sys.send_result() can be used to send data to a Web Client. It can be used instead of or in addition to writing WebReports to send the data. If you want the req4c PHP client to be able to access data using associative arrays, then send call `sys.send_result(SR_NAMES,...)` before making multiple calls to `sys.send_result(SR_DATA,...)`.

### Bugs / Features / Comments
None

### See Also
- Web4C
