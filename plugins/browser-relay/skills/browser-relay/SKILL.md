---
name: browser-relay
description: "<用户自制> 浏览器会话：选择 Chrome、Ego Lite 或 Linux 无头浏览路线。 Route browser tasks to Web Access for Chrome, Ego Lite when Chrome automation is too slow, or Playwright for Linux headless work."
user-invocable: false
---

# browser-relay

For Chrome, use [Web Access](https://github.com/eze-is/web-access) and follow
its CDP setup for the intended, authorized Chrome session. If Chrome automation
is too slow and the task can run in a separate browser, try
[Ego Lite](https://github.com/citrolabs/ego-lite) on a supported platform.

On Linux, for a headless task that needs no sign-in, use Playwright with an
isolated Chromium context. The [bundled smoke check](README.md#optional-linux-headless-check)
exercises page creation, readback, and cleanup.

Use the intended session and exact task page. Verify the result there and
close the page you created when the task finishes.
