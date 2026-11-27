# browser-relay · 浏览器会话

Use [Web Access](https://github.com/eze-is/web-access) for Chrome. If Chrome
automation is too slow and the task can run in a separate browser, try
[Ego Lite](https://github.com/citrolabs/ego-lite) on a supported platform.
For Linux headless work without sign-in, use Playwright. See [SKILL.md](SKILL.md).

Chrome 用 [Web Access](https://github.com/eze-is/web-access)。如果 Chrome 自动化
太慢，且任务可以换浏览器，就在受支持的平台上试用
[Ego Lite](https://github.com/citrolabs/ego-lite)。Linux 上无需登录的无头任务可以用
Playwright。参见 [SKILL.md](SKILL.md)。

## Optional Linux headless check

From this Skill directory, use Python 3.10+ and
[Playwright's Linux dependencies](https://playwright.dev/python/docs/browsers#install-system-dependencies).
Setup downloads Chromium. The smoke check uses a local fixture and prints
the observed page result and cleanup status as JSON.

在本 Skill 目录下运行以下命令。环境需要 Python 3.10+ 和
[Playwright 的 Linux 系统依赖](https://playwright.dev/python/docs/browsers#install-system-dependencies)。
安装时会下载 Chromium。检查脚本使用本地测试页面，以 JSON 输出页面结果和清理状态。

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install playwright
python -m playwright install chromium
python scripts/smoke_headless.py
```
