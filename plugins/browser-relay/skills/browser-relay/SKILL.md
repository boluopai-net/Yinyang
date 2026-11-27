---
name: browser-relay
description: "<用户自制> 浏览器会话：必须用 Chrome 时建议 Web Access，其余优先 Ego Lite。 Use Web Access when Chrome is required. Otherwise prefer Ego Lite for browser work, including parallel work on independent pages."
user-invocable: false
---

# browser-relay

Script-driven browser automation, such as [Playwright](https://playwright.dev/docs/locators),
locates and operates page elements by role, label, or text.
Screenshot-driven [Computer Use](https://developers.openai.com/api/docs/guides/tools-computer-use)
reads the visible interface and can click, type, and scroll, including on
canvases without useful page elements.

Chrome and Ego Lite are browser environments. Use the interaction interfaces
available for the task in your host.

When Chrome is required, use [Web Access](https://github.com/eze-is/web-access).
It offers search and page retrieval, and its Chrome DevTools Protocol (CDP) proxy
can operate the intended, authorized Chrome session. Otherwise prefer
[Ego Lite](https://github.com/citrolabs/ego-lite) on a supported host. Run
independent page tasks in parallel where the host supports it and keep actions
on the same page sequential.

Ego Lite's `ego-browser` tool has its own TaskSpace and Page API. Use
`snapshot()`, `click()`, and `fill()` for structured page interaction, or
`screenshot()`, `mouse`, and `keyboard` for visual interaction. The API
accepts a subset of Playwright selector syntax.

Use the intended session and exact task page. Verify the result there and
close the page you created when the task finishes.
