# browser-relay · 浏览器会话

## 中文

- [Playwright](https://playwright.dev/docs/locators) 用脚本按角色、标签或文字定位并操作网页元素，适合能用这些方式定位控件的任务。
- [Computer Use](https://developers.openai.com/api/docs/guides/tools-computer-use) 看截图来点击、输入和滚动，适合需要看界面才能操作的任务，比如只有画面可供判断的画布。

Chrome 和 Ego Lite 是浏览器环境，具体能用哪种交互方式取决于宿主提供的接口。必须用 Chrome
时，建议用 [Web Access](https://github.com/eze-is/web-access)。它提供搜索和网页读取，也能
通过 CDP 代理操作指定的已获授权 Chrome 会话。其余情况下，优先用宿主支持的
[Ego Lite](https://github.com/citrolabs/ego-lite)。宿主支持时，独立页面任务可以并行，同一页面
上的操作按顺序执行。

Ego Lite 的 `ego-browser` 有自己的 TaskSpace 和 Page API，支持部分 Playwright 选择器语法。
可用 `snapshot()`、`click()`、`fill()` 按页面结构操作，也可用 `screenshot()`、`mouse`、
`keyboard` 按画面操作。参见 [SKILL.md](SKILL.md)。

## English

- [Playwright](https://playwright.dev/docs/locators) scripts browser actions when page elements can be located by role, label, or text.
- [Computer Use](https://developers.openai.com/api/docs/guides/tools-computer-use) reads screenshots and can click, type, and scroll. Use it for tasks that depend on the visible interface, such as a canvas without useful page elements.

Chrome and Ego Lite are browser environments. Use the interaction interfaces
your host makes available. When Chrome is required, use
[Web Access](https://github.com/eze-is/web-access) for search, page retrieval, or
CDP access to the intended, authorized Chrome session. Otherwise prefer
[Ego Lite](https://github.com/citrolabs/ego-lite) on a supported host. Run
independent page tasks in parallel where supported and keep same-page actions sequential.

Ego Lite's `ego-browser` tool has its own TaskSpace and Page API and accepts
a subset of Playwright selector syntax. Use structured page controls such as
`snapshot()`, `click()`, and `fill()`, or visual controls such as
`screenshot()`, `mouse`, and `keyboard`. See [SKILL.md](SKILL.md).
