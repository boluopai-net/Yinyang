# 阴阳的来源与私人更新

本页说明作者公共写作源与私人实例的关系。公开提供的 Skill 是
[Empty](https://github.com/boluopai-net/Yinyang/tree/main/skills/yinyang-empty)，
使用者的安装与更新由 Empty 自己的包说明负责。

[首页](../../README.zh-CN.md) · [English](skill-package.md)

公开的 `docs/` 目录维护文章、图示与共同形成方法。
实际私人入口与个人模型保留在各自来源。读者可以阅读哲学，或从 Empty
形成自己的实践；这个写作源目录不再作为 Full Skill 分发。

## 公共内容与情境化内容

六份中英文形成指南规定取向、人、伙伴、关系、环境与修订的完整问题及阅读职责。
每项综合指引从全部六份完整指南与有关实际根据形成。[形成与修订](../design-and-revision.zh-CN.md)
维护不同对象、相连范围与六份整体融贯。

共同写作、网站阅读版、六份处境描述与工作环境通过同一套工作本体相连，内容和私人边界各不相同。
来源可能与当前描述不一致；保留归属与根据，由模型结合实际使用判断是否需要修订描述或其实现。

[静态参考与实践方法](creation-method.zh-CN.md#choose-2x2)说明版本与凝练方式；本页列出私人文件及更新位置：

| 问题 | 私人实际文件 |
| --- | --- |
| 取向 | `references/situated/orientation.md` |
| 个人 | `references/situated/person.md` |
| 伙伴 | `references/situated/counterpart.md` |
| 关系 | `references/situated/relationship.md` |
| 环境 | `references/situated/environment.md` |
| 实际处境中的修订方法 | `references/situated/revision.md` |

进入日常个人协作前，必须把六份完整实际模型注入主模型上下文；这是个人版的必要配置。
通过宿主支持的全局或会话上下文提供个人入口、选定采用的基本观点正文与六份完整实际模型。
已在上下文中的全文直接理解和使用，只有缺失或截断的正文才通过实际 Skill 路线取回。
私人入口写明宿主提供什么，并索引其他材料。模型按当前任务选择[工具使用](getting-started.zh-CN.md)、
[科研与学习](research-and-learning.zh-CN.md)与[心理](psychological-support.zh-CN.md)三个实践入口，
再按需进入 Personal 来源、论证或形成指南。完整上下文与选择性补充取材各有作用，
本人无须逐份寻找并粘贴文件。Empty 的[上下文配置](https://github.com/boluopai-net/Yinyang/blob/main/skills/yinyang-empty/references/package.zh-CN.md#接入个人上下文)
说明使用者怎样配置和核验。

通过实际账号与发布维护者，将需要持久保存的私人源放在 Git 与私人 GitHub 仓库，
核实私有范围、提交内容与读者取得。原件保有维护者，秘密不进入普通仓库文件。公共写作源不包含实际私人描述。

复杂版将核对后的正文投影到同样六路径，或用私人 `references/situated/index.md`
绑定六个问题、原生 ID 与完整正文。配置见 [Hindsight 指引](../hindsight.zh-CN.md)。
六份的内容形成与整体检查由[形成与修订](../design-and-revision.zh-CN.md)维护。

Philosophy 保有写作来源。Personal 在原有四个主题组内保留可读文章、目录与原始来源链接，仍可直接编辑整理。
原生路线可用实质 Knowledge Pages 维护文章，将 Markdown 投影到已有私人阅读路径，Observations 在后台支持。
按修订需要迁移受影响派生文章，保留可读性与独有根据。已纠正的 Personal 理解须影响后续综合；各产物均能返回
原件，不强制串联生成摘要。[Personal 指南](../formation/personal-material.zh-CN.md#保持-personal-便于本人阅读)维护阅读安排。

材料名称使用本人的母语，正文语言按消费者选择，必要时保留量表标识。
`references/personal/` 与 `references/situated/`，包括可选原生绑定和私人生成正文，均为私有。
公共投影保护两个目录，不修改 bank 状态、GitHub 可见性或运行时消费者。独立哲学保有自己的来源。

## 量表与测评材料

个人版已有量表或测评记录时，把这部分特殊的个人证据整理到
`references/personal/questionnaires/`。用其中的 `README.md` 提供清楚的目录，连接
按日期保留的记录与原始来源，并从 `personal/README.md` 和 `personal/sources.md`
接入。按测量场次或量表组织，以便检索；重复填写仍是彼此独立、有日期的观察。

每条记录保留已知的量表名称、语言与版本、完成日期与情境、结果与分数方向，以及
原始作答或报告的入口。区分问卷作答、表现测验、报告写出的结论与后来的解释。
明确保留不同结论和缺失信息；报告没有逐题答案时，不补造作答。已有私人测量系统
和就医文档集合可以继续保存原件，这里保留有用结果与可用链接，不再复制整套档案。
没有日期的材料保持未定日期，直到来源能确定时间。

这样组织，使测量与叙述材料能够一起被使用，不把量表当作完整个人描述，也不因
增添记录而自动改写工作模型。量表选择、计分与解释由
[心理页](psychological-support.zh-CN.md)说明。这个目录和所有填写后的记录保持私有；
分发包只提供组织方法，不带入别人的记录或占位结果。

## 投影公共资源到作者的私人实例

`scripts/sync-common.py` 比较公共写作源与已有私人 Skill；加上 `--apply`
复制公共资源，保留私人入口及智能体元数据、README 阅读版、MODEL 与 AGENTS 文件，
以及 `references/personal/`、`references/situated/` 两棵私人目录。

```bash
python3 /path/to/collection/docs/scripts/sync-common.py \
  --source /path/to/collection/docs --target /path/to/private/yinyang
```

源以形成方法识别，目标以实际 `SKILL.md` 识别。投影器不检查私人目录、
不替新人形成模型，也不发布运行时。公共路径出现多余文件或符号链接时，
由维护者检查归属；已有本地与私人云端发布者交付核对后的私人源，并读回实际消费者。

Empty 使用者按本包自己的约定更新。独立写作的哲学与方法保留自己的来源，
不由作者公共资源的投影覆盖。

## 私人与公开边界

个人描述即使经过形式化或面向模型书写，也仍属于私人内容。私人引文、传记、心理和
健康记录、关系叙述、账户信息、私人路径、对话标识和未发表手稿留在实际维护位置。
一般化抽象不授权公开能够重建私人来源的链接。

只有获授权的可复用认识回到集合。阴阳原创材料采用 Yinyang Personal and Internal Use License 1.0，
其他独立成员保留各自 MIT 许可。权限、署名与来源审查遵循
[集合说明](https://github.com/boluopai-net/Yinyang/blob/main/README.zh-CN.md)及实际发布维护者。私人改编不必公开。
