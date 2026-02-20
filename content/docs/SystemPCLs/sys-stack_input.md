---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 328
title: "sys.stack_input"
---
## sys.stack_input()
### Purpose
sys.stack_input() allows a program to stack input.

### Usage
```c
ret = sys.stack_input(inp1 [,inp2 [..., [inp16]] ... ]);
```

### Arguments
inp1 - inp16 - Up to 16 alpha args  
inp1 is mandatory and inp2 through inp16 are optional.

### Returns
0 - OK

There are no error returns.

### Where Used
sys.stack_input() can be called from anywhere. Of course, it has no affect until input is needed from the user.

### Example
```c
sys.stack_input("0001");
```

### Description
sys.stack_input() allows a program to stack input. Stacked input acts as if the user entered that which is stacked in the same order it was stacked. Each stacked input is followed by a <CR>. This is not really a stack, it is a FirstIn FirstOut list. So successive stack input calls are added to the end of the list rather than the head of the list. The arguments passed to sys.stack_input() are also processed in the same order. This can be used when you want to try to anticipate a users response and save keystrokes. Calls to sys.stack_input() and sys.stack_fkey() can be intermixed with predictable results.

### Bugs / Features / Comments
Every argument passed to sys.stack_input() gets a <CR> appended to it, even though this is not always wanted.

### See Also
- sys.stack_fkey()
