---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 54
title: "sys.create_file"
---
## sys.create_file()
### Purpose
sys.create_file() creates a file on disk.

### Usage
```c
ret = sys.create_file(<asfile>);
```

### Arguments
file \<asfile\> - The asfile name of the file to create.

### Returns
0 - File create ok

-1 - Some error, msg displayed, and file NOT created.

### Where Used
sys.create_file() can be called from anywhere, but care should be taken to make sure the file is not already in use by another program.

### Example
None

### Description
sys.create_file() creates a data file in the first data directory, or by using the external name of the file. If the file exists in the first data directory, it is removed first. If it exists in any directory other than the first, it is left alone, but a file will still be created in the first data directory.

sys.create_file() can be used to create temporary files when they are needed longer than the life of the program that created them. If they can be discarded immediately, then `sys.create_tfile()` should be used.

### Bugs / Features / Comments
sys.create_file() is obsolete - use `sys.open_file(<asfile>,F_CREATE)` instead.

If the file exists and is in use by another program the results are unpredictable. The file to create must be defined by the program creating it.

The file being created is ALWAYS created in the first data directory.

### See Also
- sys.create_tfile()
- sys.open_file()
