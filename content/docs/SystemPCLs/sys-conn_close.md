---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 46
title: "sys.conn_close"
---
## sys.conn_close()
### Purpose
sys.conn_close() closes a remote file server connection or an external database connection.

### Usage
```c
sys.conn_close(<connname>,<closeflags>);
```

### Arguments
alpha `<connname>` - The name of the connection to close. This can be the empty string.

integer `<closeflags>` - Combination of the following flags:
- CONNCLOSE_DEFAULT - Close the named connection, or close the connection associated with XLEXTTYPE if connname is empty.
- CONNCLOSE_ALL - Close all external database and all remote file connections.
- CONNCLOSE_DBALL - Close all external database connections.
- CONNCLOSE_REMALL - Close all remote file connections.

### Returns
0 - sys.conn_close() always returns 0.

### Where Used
sys.conn_close() can be called from anywhere. However, it is the application's responsibility to make sure that any active transactions have been committed or rolled back.

### Example
None

### Description
sys.conn_close() will close one or more external db and remote file connections. sys.conn_close() will be mostly used in situations where an external connection is idle a lot. Rather than letting the firewall terminate the connection, leaving orphaned processes on the remote machine, and getting an error the next time the connection is used, sys.conn_close() will explicitly close the connection. Then the next time the connection is needed a new one will be opened.

### Bugs / Features / Comments
None

### See Also
- sys.close_file()
