---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 17
title: "sys.calc"
---
## sys.calc()
### Purpose
sys.calc() parses a formula at runtime.

### Usage
ret = sys.calc(<formula>);

### Arguments
<formula> - A string constructed of numeric variables, spaces, operators, parenthesis, and enclosed in curly braces.

### Returns
0 - Formula parsed correctly and result stored in the system variable `sys.calc_result`.

-1 - Error in parsing - and a message is displayed.

### Where Used
sys.calc() can be called from anywhere.

### Example
```c
formula = "{" + sys.fmt_float(fl1,"99.99-") + "/" +
    sys.fmt_float(fl2,"99.99-") + "}";
sys.calc(formula);
sys.err_msg("Result: " +
    sys.fmt_float(sys.calc_result,"9999.9999-"));
```

### Description
sys.calc() parses a formula at runtime and sets a result into `sys.calc_result`. If the string cannot be parsed correctly, `sys.calc()` returns -1. The value in `sys.calc_result` is undefined in this case. The formula is a single alpha variable. It can be constructed using the functions `max()` and `min()`, arithmetic operators, and parenthesis. The formula must be enclosed in curly braces. Any numeric variables that are part of the formula must be converted to alpha and concatenated in the right order.

### Bugs / Features / Comments
No syntax errors can be caught at runtime.

### See Also
- sys.fmt_float()
