---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 126
title: "sys.get_clpref"
---
## sys.get_clpref()
### Purpose
sys.get_clpref() returns a client preference to the application.

### Usage
```c
prefval = sys.get_clpref(<prefflags>,<preftype>);
```

### Arguments
integer `<prefflags>` - Either PREF_CURRENTUSER or PREF_ALLUSERS

alpha `<preftype>`

### Returns
alpha `<prefval>`

### Where Used
sys.get_clpref() can be called from anywhere during an interactive 4C session.

### Example
None

### Description
sys.get_clpref() returns a client preference as a string. The preference requested can be either a current user preference or an all user preference. In order to retrieve a preference specific to the current user, set `<prefflags>` to PREF_CURRENTUSER. In order to retrieve a preference specific to all users, set `<prefflags>` to PREF_ALLUSERS. `<preftype>` can be any of the preference names listed in: Client Preferences.

### Bugs / Features / Comments
sys.get_clpref() is not supported by the non interactive 4C client, 4ccl.

### See Also
- sys.get_clinfo()
- sys.set_clpref()
