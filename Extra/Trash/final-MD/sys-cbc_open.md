---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 21
title: "sys.cbc_open"
---
## sys.cbc_open()
### Purpose
`sys.cbc_open()` begins a specific type of clipboard copy operation.

### Usage
```c
<ret> = sys.cbc_open(<type>,<flags>,<asfile>);
```

### Arguments
integer - `<type>` - Must be one of:
- CBC_4CTYPE
- CBC_TEXTTYPE
- CBC_DIFTYPE

integer - `<flags>` - Currently are used only when `<type>` is CBC_TEXT. You can specify combinations of the following for `<flags>`
- CBC_FIXED - Sends text in FixSeq len format
- CBC_VAR - Sends text in VarSeq format.
- CBC_CSV - Comma separate fields
- CBC_TSV - Tab separate fields
- CBC_SQUOTE - Quote alpha literals with single quotes
- CBC_DQUOTE - Quote alpha literals with double quotes
- CBC_QUOTE - Same as CBC_DQUOTE

asfile - `<asfile>` - The 4C asfile that is used as a template for formatting data.

### Returns
integer - `<ret>`
- -1 - Error - illegal `<type>` or illegal `<asfile>`
- 0 - OK

### Where Used
`sys.cbc_open()` can be called anytime after `sys.cbc_init()` has been called to begin the copy for the specified type.

### Example
None

### Description
`sys.cbc_open()` begins a specific type of clipboard copy operation. All `sys.cbc_open()` calls need to have a corresponding `sys.cbc_close()` call. Only one clipboard format can be open for copying at any one time.

### Bugs / Features / Comments
None

### See Also
- Cut/Copy/Paste Overview
- sys.cbc_close()
- sys.cbc_init()
- sys.cbc_senddata()
- sys.cbc_sendtext()
