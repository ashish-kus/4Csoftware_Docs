---
date: "2026-02-19T14:07:01+05:30"
draft: false
type: docs
weight: 6
title: "sys.app_log"
---

## sys.app_log()

### Purpose

sys.app_log() adds an entry to the application log.

---

### Usage

```c
sys.app_log(<type>, <typedet>, <severity>, <message>);
```

---

### Arguments

| Argument     | Type    | Description                                                                                                  |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------ |
| `<type>`     | alpha   | An application specific type up to 20 chars.                                                                 |
| `<typedet>`  | alpha   | Detail of the type if needed. Up to 30 chars.                                                                |
| `<severity>` | integer | A value indicating how important the log message is. The higher the severity the more important the message. |
| `<message>`  | alpha   | A detailed message up to 200 characters.                                                                     |

---

### Returns

None

---

### Where Used

sys.app_log() can be called from anywhere.

---

### Example

The `sys.app_trace()` Global PCL calls `sys.app_log()`.

---

### Description

Every 4C application maintains an application log starting with 4C server version 6.2.7. The application log is automatically purged as needed and you can configure the frequency of the purging through the System Configuration for the application.

You can view entries in the application log by running the `Application Log` entry under `Logging` in the main `sys.menu.tv` developers menu. Most entries in the application log are made by the application programs mostly for the purpose of logging events that can be reviewed later. However, there are some exceptional conditions that are automatically logged by the system.

---

### Requirements

4C server version 6.2.7 or later.

---

### Bugs / Features / Comments

None

---

### See Also

- sys.app_trace()
