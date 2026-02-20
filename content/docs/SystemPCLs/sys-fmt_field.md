---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 112
title: "sys.fmt_field"
---
## sys.fmt_field()
### Purpose
sys.fmt_field() returns a formatted field.

### Usage
aval = sys.fmt_field(<field>);

### Arguments
AnyType <field> - Any field of any data type defined in the program.

### Returns
alpha <aval> - The formatted value of <field>.

### Where Used
sys.fmt_field() can be called from anywhere.

### Example
None

### Description
sys.fmt_field() returns the formatted field, using the default display format for the field. There are no error returns.

### Bugs / Features / Comments
None

### See Also
- sys.fmt_field()
- sys.fmt_alpha()
- sys.fmt_choice()
- sys.fmt_date()
- sys.fmt_float()
- sys.fmt_integer()
- sys.fmt_time()
