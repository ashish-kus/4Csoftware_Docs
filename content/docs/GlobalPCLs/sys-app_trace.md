---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 5
title: "sys.app_trace"
---
## sys.app_trace()
### Purpose
`sys.app_trace()` creates a trace file of the state of the 4csrvr process when it is called and it writes to log records to the application log.

### Usage
```c
sys.app_trace(<type>,<typedet>,<severity>,<message>,<option>);
```

### Arguments
- alpha `<type>` - An application specific type up 20 chars.
- alpha `<typedet>` - Detail of the type if needed. Up to 30 chars.
- integer `<severity>` - a value indicating how important the log message is. The higher the severity the more important the message.
- alpha `<message>` - A detailed message up to 200 characters.
- alpha `<option>` - currently Verbose or NoVerbose

### Returns
None

### Where Used
`sys.app_trace()` can be called from anywhere.

### Example
The demo.dbg.main program has an example of calling `sys.app_trace()`.

### Description
`sys.app_trace` uses the 1st 4 arguments to write a record to the application log. It then creates a full trace of the current state of the 4csrvr process and writes this to a trace file in the FC_TEMP directory. Finally, it writes another record to the application log with a type of "TraceFile" and a message indicating the full path of the trace file.

### Bugs / Features / Comments
Bugs

### See Also
- sys.app_log()
