# 阴阳 · Yinyang

![用尽量少的复杂性辅助个人获得个人观点、工作模型以及个人 RSI 的全局提示词形式。四条主线为容纳不一致语义、阴阳辩证法、圣状与三位一体、个人递归自改进。](assets/yinyang-cover.zh-CN.png)

阴阳是一种个人递归自改进（RSI）的形式：在改进一次工作的同时，也改进产生这些改进的方法。这里收录讨论这套实践的文集，以及 **22 个可按需安装的 Skills**，用于研究、学习、设计环境和操作设备。

<!-- reading-cover:start -->
## 选择怎样阅读和使用

这部文集讨论一种个人递归自改进的方法：把自己喜欢的哲学和观点同个人材料放在一起，由语言模型凝练成个人模型。个人模型可以用来调整工具和协作方式，实际使用的结果又为修订模型和改进方法提供依据。

阅读可以从[基本观点](docs/references/docs/core-views.zh-CN.md)开始。先挑几条感兴趣的观点，沿链接阅读相应正文，了解理由和例子，再与原有的看法比较。觉得合适的可以留下，也可以到其他作品中继续寻找喜欢的观点。

这里的**个人哲学，就是表达个人看法的文章**。已有的文章可以直接用。是否把零散的想法另写成篇，取决于写作兴趣；选读和采用观点本身就有价值。

需要把选定的哲学和观点用于实践时，可以结合个人材料凝练个人模型。个人模型是[六份工作描述](docs/references/formation/overview.zh-CN.md)中的一份，其余五份分别涉及立场与方向、模型伙伴、协作关系、实践环境和修订方式。选定的观点和六份描述可以放进语言模型的全局提示词，用于配置软件和工具，再随实践修订。具体做法见[实践指南](docs/references/docs/creation-method.zh-CN.md)。

<!-- reading-cover:end -->

<table>
<thead><tr><th width="480" align="left">想做什么</th><th width="480" align="left">从这里开始</th></tr></thead>
<tbody>
<tr><td>在网站阅读</td><td><a href="https://boluopai.net/yinyang/">文集</a> · <a href="https://boluopai.net/repositories/prometheus/">附录</a> · <a href="https://boluopai.net/yinyang/resources/">资料与建议</a></td></tr>
<tr><td>下载带图电子书</td><td><a href="docs/yinyang.zh-CN.pdf?raw=1">中文 PDF</a> · <a href="docs/yinyang.en.pdf?raw=1">English PDF</a></td></tr>
<tr><td>GitHub 仓库说明</td><td><a href="#集合里的-skill">Skills 目录</a> · <a href="README.en.md">English README</a></td></tr>
</tbody>
</table>

## 使用中的问题

<table>
<thead><tr><th width="480" align="left">想弄明白的问题</th><th width="480" align="left">对应文章</th></tr></thead>
<tbody>
<tr><td>材料相互矛盾时，哪些结论还有根据？</td><td><a href="docs/references/docs/inconsistency-tolerant-semantics.zh-CN.md">容纳不一致语义</a></td></tr>
<tr><td>我先提出一个直觉，模型可以怎样帮我检验它？</td><td><a href="docs/references/docs/yinyang-and-taiji.zh-CN.md">阴阳与太极</a></td></tr>
<tr><td>一篇作品、一个伙伴、一套工具怎样支持我持续做一件事？</td><td><a href="docs/references/docs/writing-a-sinthome.zh-CN.md">从个人模型到圣状</a></td></tr>
<tr><td>一次修改怎样让下一次修改做得更好？</td><td><a href="docs/references/docs/literary-recursive-improvement.zh-CN.md">用文学写出自己的递归改进</a></td></tr>
<tr><td>哪些能力值得亲自练习，哪些工作可以交给模型？</td><td><a href="docs/references/docs/economic-personal-rsi.zh-CN.md">经济现实中的个人递归自改进</a> · <a href="docs/references/docs/cognitive-complexity.zh-CN.md">认知分工与负反馈</a></td></tr>
</tbody>
</table>

书中把哲学、心理和工程放在同一项实践里考察：一个人想做什么，怎样参与，需要什么条件才能做下去。文章借用不同传统的概念与意象，在具体论证处交代出处和本文的用法。本文采用异性恋视角，其他经验和材料也欢迎读者提出。

<!-- repository-only:start -->
## 用途与心理健康说明

阴阳的哲学观点用于配置适合人与模型协作的个人环境，包括协作方式、指令和工具。对个人的理解可以为配置提供依据；这套哲学不提供修订心理材料的方法。

阴阳不能用于心理自助工作、自行诊断、心理健康评估或治疗，也尚未经过针对这些用途的系统性实证评估。需要专业评估或照护时，应寻求合格专业人员；项目文字与模型输出不替代这种服务。作品、模型与处境会变化，个人经验或版本历史也不能确立普遍的心理效果。

独立的[心理页](docs/references/docs/psychological-support.zh-CN.md)说明模型如何协助个人材料、量表、计分、统计和实际帮助，保留各自的证据与专业照护边界。
<!-- repository-only:end -->

## 集合里的 Skill

想把书中的方法用于自己的协作，可以选 **yinyang-empty**。包里有形成六份描述的写作指南，个人材料由你自己保存。其余各包按任务选用，所需工具与配套 Skills 见各包说明。它们也可以配合：例如，想核实一段讲座引用的研究，可以先用 **video-subtitle** 定位原话，再用 **paper-retrieval** 找到论文核对。

<!-- repository-only:start -->
### 在 Codex 中安装

首次添加插件市场，再安装需要的包。以 Empty 为例：

```sh
codex plugin marketplace add boluopai-net/Yinyang
codex plugin add yinyang-empty@boluopai
```

安装后开启新对话。安装其他包时，把第二条命令的包名换掉即可。本地带练需要同时安装 **local-teacher** 和 **web-teacher**；设备、外部服务和账号按各包说明配置。个人版材料保存在插件缓存之外。[安装与更新说明](docs/codex.zh-CN.md)
<!-- repository-only:end -->

### 形成自己的方法

<table>
<thead><tr><th width="300" align="left">包与使用说明</th><th width="660" align="left">适合交给它的事</th></tr></thead>
<tbody>
<tr><td><a href="skills/yinyang-empty/README.zh-CN.md">yinyang-empty</a></td><td>把自己选定的材料整理为六份协作描述，形成自己的私人版本。</td></tr>
<tr><td><a href="skills/personal-environment-design/README.zh-CN.md">personal-environment-design</a></td><td>从一件想做的事出发，把所需软件、工具和操作方式接成可以实际使用的环境。</td></tr>
<tr><td><a href="skills/task-inquiry/README.zh-CN.md">task-inquiry</a></td><td>当同一请求有几种解释时，找出哪项分歧会改变下一步，再提出能解决它的问题。</td></tr>
<tr><td><a href="skills/prompt-and-skill-lifecycle/README.zh-CN.md">prompt-and-skill-lifecycle</a></td><td>把指令的含义、维护责任、交付方式和实际使用证据连在一起，编写、审查与维护 Prompt 和 Skill。</td></tr>
<tr><td><a href="skills/prompt-audit-orchestration/README.zh-CN.md">prompt-audit-orchestration</a></td><td>按实际范围审查学习、工作、Web 与自动化的指令和执行关系。</td></tr>
</tbody>
</table>

### 研究、学习与练习

<table>
<thead><tr><th width="300" align="left">包与使用说明</th><th width="660" align="left">适合交给它的事</th></tr></thead>
<tbody>
<tr><td><a href="skills/research/README.zh-CN.md">research</a></td><td>比较一项技术的官方说明、使用记录和反例，说明证据支持哪种选择。</td></tr>
<tr><td><a href="skills/paper-retrieval/README.md">paper-retrieval</a></td><td>核对题录、版本与全文，把搜索结果交付为可验证的学术材料。</td></tr>
<tr><td><a href="skills/video-subtitle/README.md">video-subtitle</a></td><td>取得带来源与时间线的视频讲话文本，再回到原视频核对。</td></tr>
<tr><td><a href="skills/web-teacher/README.md">web-teacher</a></td><td>提供课程材料、教学方法、学习路径与学习空间的共同方法。</td></tr>
<tr><td><a href="skills/local-teacher/README.md">local-teacher</a></td><td>在本地环境中讲解、复习、练习，并通过真实工作发展理解。</td></tr>
<tr><td><a href="skills/singing/README.zh-CN.md">singing</a></td><td>准备伴奏、录音与参考表演，把听辨和音频证据用于练唱。</td></tr>
</tbody>
</table>

### 组织模型与浏览器协作

<table>
<thead><tr><th width="300" align="left">包与使用说明</th><th width="660" align="left">适合交给它的事</th></tr></thead>
<tbody>
<tr><td><a href="skills/agent-orchestration-master/README.zh-CN.md">agent-orchestration-master</a></td><td>把可独立完成的工作分给合适的模型，约定交接内容，再合并结果。</td></tr>
<tr><td><a href="skills/model-conversation-relay/README.zh-CN.md">model-conversation-relay</a></td><td>回到指定的模型对话，确认上一条请求的结果，再接着提问。</td></tr>
<tr><td><a href="skills/browser-relay/README.md">browser-relay</a></td><td>选择 Chrome、Ego Lite 或 Linux 无头浏览路线。</td></tr>
<tr><td><a href="skills/model-upgrade-check/README.zh-CN.md">model-upgrade-check</a></td><td>核对可用模型、用途分配与实际消费者，让升级保持一致。</td></tr>
</tbody>
</table>

### 维护设备与日常使用

<table>
<thead><tr><th width="300" align="left">包与使用说明</th><th width="660" align="left">适合交给它的事</th></tr></thead>
<tbody>
<tr><td><a href="skills/android-control/README.zh-CN.md">android-control</a></td><td>通过 ADB 与原生界面操作自己的安卓设备，并核实实际效果。</td></tr>
<tr><td><a href="skills/chezmoi/README.zh-CN.md">chezmoi</a></td><td>把要保留的主机配置写回源文件，发布后核对实际设置。</td></tr>
<tr><td><a href="skills/obsidian-sync/README.zh-CN.md">obsidian-sync</a></td><td>维护多个 Obsidian 库的共同配置、云端复制与同步。</td></tr>
<tr><td><a href="skills/network/README.zh-CN.md">network</a></td><td>通过本机证据排查 DNS、代理、网站连接和路由问题。</td></tr>
<tr><td><a href="skills/clash-auto-switch/README.zh-CN.md">clash-auto-switch</a></td><td>维护 Clash 节点选择、地区回退与 DNS/TUN 保护。</td></tr>
<tr><td><a href="skills/shopping/README.zh-CN.md">shopping</a></td><td>比较商品、价格、优惠与二手选择，保留实际证据与条件。</td></tr>
<tr><td><a href="skills/random-wheel/SKILL.md">random-wheel</a></td><td>把截图或明确给出的选项变成可调速的动画转盘，以等概率随机抽选。</td></tr>
</tbody>
</table>

## 反馈与许可

欢迎通过 [Issues](https://github.com/boluopai-net/Yinyang/issues) 提出设计改进的建议、推荐值得引入的技术，或讨论其他问题。自己的作品可以独立发表。本仓库通过 Issue 接收建议，不接受 PR。

阴阳文集与 Empty 方法包中的原创材料采用[个人与内部使用许可证](LICENSE)，允许私下使用、修改和辅助有偿工作；再分发材料，或将材料及其修改版作为产品或服务提供给他人使用，需要另行许可。其他 Skill 包采用 MIT。仓库基础代码、第三方作品及各包的许可范围见[仓库许可](LICENSE)。
