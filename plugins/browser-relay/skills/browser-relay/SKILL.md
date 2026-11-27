---
name: browser-relay
description: "<用户自制> 浏览器会话：Chrome 用 Web Access，适合换浏览器时可试用 Ego Lite。 Use Web Access for Chrome, or try Ego Lite when Chrome automation is too slow and the task can use a separate browser."
user-invocable: false
---

# browser-relay

Use [Playwright](https://playwright.dev/docs/locators) for scripted browser work
when page elements can be located by role, label, or text.
Use [Computer Use](https://developers.openai.com/api/docs/guides/tools-computer-use)
when you need to work from the visible interface, such as a canvas without
useful page elements. It reads screenshots and can click, type, and scroll.

Chrome and Ego Lite are browser environments. Use the interaction interfaces
available for the task in your host.

For Chrome, use [Web Access](https://github.com/eze-is/web-access). It offers
search and page retrieval, and its Chrome DevTools Protocol (CDP) proxy can
operate the intended, authorized Chrome session. If Chrome automation is too
slow and the task can run in a separate browser, try
[Ego Lite](https://github.com/citrolabs/ego-lite) on a supported platform and
use its TaskSpace controls.

Use the intended session and exact task page. Verify the result there and
close the page you created when the task finishes.
