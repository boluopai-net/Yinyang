# browser-relay · 浏览器会话

## 中文

- [Playwright](https://playwright.dev/docs/locators) 用脚本按角色、标签或文字定位并操作网页元素，适合能用这些方式定位控件的任务。
- [Computer Use](https://developers.openai.com/api/docs/guides/tools-computer-use) 看截图来点击、输入和滚动，适合需要看界面才能操作的任务，比如只有画面可供判断的画布。

Chrome 和 Ego Lite 是浏览器环境，具体能用哪种交互方式取决于宿主提供的接口。Chrome 用
[Web Access](https://github.com/eze-is/web-access)。它提供搜索和网页读取，也能通过 CDP
代理操作指定的已获授权 Chrome 会话。如果 Chrome 自动化太慢，且任务可以换浏览器，就在
受支持的平台上试用 [Ego Lite](https://github.com/citrolabs/ego-lite)，用它的 TaskSpace 控制页面。
参见 [SKILL.md](SKILL.md)。

## English

- [Playwright](https://playwright.dev/docs/locators) scripts browser actions when page elements can be located by role, label, or text.
- [Computer Use](https://developers.openai.com/api/docs/guides/tools-computer-use) reads screenshots and can click, type, and scroll. Use it for tasks that depend on the visible interface, such as a canvas without useful page elements.

Chrome and Ego Lite are browser environments. Use the interaction interfaces
your host makes available. [Web Access](https://github.com/eze-is/web-access)
offers search and page retrieval, and its CDP proxy can operate the intended,
authorized Chrome session. If Chrome automation is too slow and the task can
use a separate browser, try [Ego Lite](https://github.com/citrolabs/ego-lite)
on a supported platform using its TaskSpace controls. See [SKILL.md](SKILL.md).
