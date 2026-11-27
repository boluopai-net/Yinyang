---
name: browser-relay
description: "<用户自制> 浏览器会话：必须用 Chrome 时建议 Web Access，其余优先 Ego Lite。 Use Web Access when Chrome is required. Otherwise prefer Ego Lite for browser work, including parallel work on independent pages."
user-invocable: false
---

# browser-relay

Prefer [Ego Lite](https://github.com/citrolabs/ego-lite) for routine browser
work on a supported host. Its `ego-browser` API supports structured page
controls, screenshots and input, and direct CDP. Batch related actions and,
where supported, run independent pages in parallel within the task's
TaskSpace. Keep dependent steps on a page in order.

When Chrome is required, use the [Web Access](https://github.com/eze-is/web-access)
CDP proxy with the intended, authorized session. Use page structure for identifiable controls and visual
interaction for steps that depend on what is visible.

Use the intended session and exact task page. Verify the result there and
close the page you created when the task finishes.

For the tool relationships and examples, see the [introduction](README.md) or
the [Chinese introduction](README.zh-CN.md).
