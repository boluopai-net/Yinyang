# 实践指南

[首页](../README.zh-CN.md) · [工作模型的形成与修订](design-and-revision.zh-CN.md) · [阴阳的日常协作](https://github.com/boluopai-net/Yinyang/blob/main/skills/yinyang-empty/SKILL.zh-CN.md) · [English](creation-method.md)

**想用阴阳做自己的个人递归自改进（RSI），可以跳过哲学正文。** 观点可以自己写，也可以请语言模型读取[基本观点](core-views.zh-CN.md)，挑出想采用的几条，再添上自己的判断。已有的文章和个人材料中，同样可以提炼出值得单独保存的观点。

另外，让语言模型从你的文章和个人材料中凝练个人模型，写成六份工作文件：取向、个人、伙伴、关系、环境、修订。观点与个人模型各自独立。六份文件需要说明某项安排的理由时，只引用相应观点，并用你自己的材料说明它怎样适用于你的处境。材料里反复用到的方法，还可以提炼成工具或 Skills。以后有新材料，可由语言模型自动或协助更新相应的观点、工作描述和工具。

日常把采用的观点和六份描述注入模型的全局提示词，让它据此逐项配置和调整你的软件环境，包括自制的 Skills。人的练习也从这里开始：自己察觉问题，用日常语言提出解释，请模型给出反例，再回到实际情境中试一试。把发现的不合之处带回个人模型和软件设置，改变下一次怎样做。这就是负反馈怎样进入生活，也是在使用环境的同时培养直觉、具身推理和日常语言推理的一种办法。

## 哲学与个人环境相互修订

从一件正在做的事入手。让模型照六份描述调整环境，实际用一次，再判断哪处理解需要改。如果问题反复出现，就修订以后发现和处理它的方法；在下一件事中检验新方法能否更早发现问题、更容易做出有效改变。这一步关系到强 RSI。[《用文学写出自己的递归改进》](https://boluopai.net/repositories/prometheus/source/skills/yinyang/references/docs/literary-recursive-improvement.zh-CN.html#从改写文字到改变下一轮活动)展开它的实现，[同篇的阅读例子](https://boluopai.net/repositories/prometheus/source/skills/yinyang/references/docs/literary-recursive-improvement.zh-CN.html#一次阅读怎样改变改善阅读的方法)展示怎样检验方法本身的改进。

<a id="choose-2x2"></a>

## 从 Empty 开始

公开提供的阴阳 Skill 是 **Empty**。作者的哲学文章与图示继续作为阅读材料；你的个人版本形成自己采用的理解。

**Empty 提供递归自我改进的方法。**用自己的目的、经验、材料和判断形成个人内容，再通过实际工作持续修订。

六份描述使这项方法取得工作形式：方向、实际参与者、双方合作、实现条件，以及方法怎样改变自身。
联系阅读它们，理解一项活动，展开候选改变，比较后果，并把选定修订带入使用。
[RSI 文章](https://boluopai.net/repositories/prometheus/source/skills/yinyang/references/docs/literary-recursive-improvement.zh-CN.html)展开论证，
[六份写作指南](design-and-revision.zh-CN.md#基于实际材料形成情境化版本)说明怎样从自己的材料形成描述。

[**Empty 的方法源码**](https://github.com/boluopai-net/Yinyang/tree/main/skills/yinyang-empty)是自己的实践入口。

## 为同一方法选择辅助方式

### 模型直接写作

把自己的哲学理解、Personal 材料和已有描述交给当前使用的语言模型，按
[六份形成指南](design-and-revision.zh-CN.md#基于实际材料形成情境化版本)直接压缩、整理和修订。
随着模型能力迭代，也让新模型重新理解材料、改善凝练。
正文保存在私人 `references/situated/` 的六份文件中，用私人 Git/GitHub 保留版本。

### 可选的记忆与综合辅助

在从 Empty 形成的个人版本上，配置辅助记忆与模型形成的社区项目。本项目已使用
[Hindsight](hindsight.zh-CN.md)：它保留来源、整合观察，并按问题形成持续维护的正文。
模型承担配置、检查和修订，将采用的结果交回六份描述。
[Hindsight 配置指引](hindsight.zh-CN.md#配置所选原生实现)是这条路线的操作入口。

依据实际检索、整合和维护工作能获得什么改善来选择辅助方式。两种实现保留同样的六个问题、
有归属的根据、整体检查，以及使用向方法的返回。材料、模型能力与维护成本变化时，工具选择也可以改变。

<a id="六份文件让实践取得可用形式"></a>
<a id="从形成指南到六个工作模型"></a>

## 六份描述放在哪里，怎样使用

六份描述是取向、个人、伙伴、关系、环境和修订，位于私人 `references/situated/`；
[文件与更新约定](package.zh-CN.md#公共内容与情境化内容)列出具体文件名。
个人材料、可读主题文章与来源索引放在 `references/personal/`。
原生实现也可通过私人索引连接六份完整正文。

实际任务中，模型联系阅读六份描述，理解本人的方向、双方及其关系、可用环境，以及这份安排怎样改变。例如，帮助一个人接续阅读时，它可以找回原文和本人当时的问题，准备方便理解的视图，再根据反馈修订支持方式。

形成与修订时，模型读取采用的哲学和有关新来源，纠正 Personal 理解，综合六份描述并联系阅读，
再把所选改动落实到工作环境，从实际使用中继续修订。
[形成与修订](design-and-revision.zh-CN.md)展开写作方法，
[日常协作](https://github.com/boluopai-net/Yinyang/blob/main/skills/yinyang-empty/SKILL.zh-CN.md)说明怎样读取和运用当前描述。

<a id="哲学与模型共同发展"></a>

## 从自己的现有材料开始

已有哲学、个人经验、偏好、作品或工作环境，都可以成为起点。模型帮助形成缺少的联系；
实际工作也能使你重新考虑哲学与合作方式。对进一步写作有兴趣时，
[从采用、组合到自己的创作](https://boluopai.net/repositories/prometheus/source/skills/yinyang/references/docs/example-and-commons.zh-CN.html)通向个人文章与不同作品。
