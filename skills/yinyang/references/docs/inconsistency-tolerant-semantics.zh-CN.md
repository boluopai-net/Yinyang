# 容纳不一致语义：修复、优先关系与答案

[首页](../../README.zh-CN.md) · [偏好 Harness](preference-harness.zh-CN.md) · [推理](reasoning.zh-CN.md) · [English](inconsistency-tolerant-semantics.md)

一份记录说，Ada 在某一时刻身处公园；另一份记录说，同一时刻她在图书馆。两处都在校园内，但她不能同时身处两处。还有一份无争议的记录说 Ben 已签到。关于 Ada 的分歧，不该抹去 Ben 的记录，也不该使「Ada 是否在校园」这个问题失去意义。**容纳不一致语义**为这样的问题提供精确的问法：如果把相互矛盾的记录一起交给经典逻辑，所得知识库没有模型，会推出任何查询；从记录中选出相容的部分，答案才重新具有区分力。

这里有两个分别的选择：**采用哪些相容的记录组合**，以及**一个查询需要获得怎样的支撑**。形式例子把区别说清，日常推理也可以据此辨认自己的判断。[YY-00](core-views.zh-CN.md#yy-00)把这项语义与阴阳辩证法、圣状与三位一体、个人递归自改进并列，沿四条主线中各自保留的读法以 P-AR 检验共同主张；本章展开其中第一条主线的形式语义。

## 固定规则与极大相容修复

例子中的规则说：在公园或图书馆，都意味着在校园；在这一时刻，同一个人不能同时身处两处。记录则分别说明 Ada 的位置和 Ben 的签到。在描述逻辑中，规则构成**本体** $T$，有限的事实记录构成 **ABox** $A$，两者合为知识库 $K=(T,A)$。这里假定 $T$ 本身相容。若查询 $q$ 从规则和所选记录 $R$ 推出，写作 $(T,R)\models q$，意思是**每个**满足 $T$ 与 $R$ 的经典模型都满足 $q$；仅有一个模型容许 $q$ 还不够。

**修复**是 $A$ 中与 $T$ 相容、且按包含关系极大的子集 $R$：再添入 $A$ 的任何一条记录，都会产生不相容。「极大」指不能再添记录，不是记录数目最多。$SRep(K)$ 表示全部修复构成的族。当 $A$ 有限而 $T$ 相容时，这个族非空，即使整个 $A$ 不相容。[^formal]

用 $a$ 表示 Ada、$b$ 表示 Ben，同一个例子可以写为：

$$
\begin{aligned}
T=\{&Park\sqsubseteq Campus,\\
&Library\sqsubseteq Campus,\\
&Park\sqsubseteq\neg Library\}.
\end{aligned}
$$

$$
A=\{Park(a),Library(a),SignedIn(b)\}.
$$

$Park(a)$ 与 $Library(a)$ 冲突，$SignedIn(b)$ 不受影响。两个修复分别是 $R_{Park}=\{Park(a),SignedIn(b)\}$ 和 $R_{Library}=\{Library(a),SignedIn(b)\}$。各自相容，也都无法再从 $A$ 中添入断言。两者都推出 $Campus(a)$，但各有不同的依据。它们共同保留的断言只有 $R_{Park}\cap R_{Library}=\{SignedIn(b)\}$，单凭它不能推出 $Campus(a)$。此处比较记录时保持规则不变；若修改规则，问题也随之改变。

## 两项选择，并非一条尺度

公园与图书馆的两条记录构成一个**极小冲突**：它们合在一起违反规则，单独保留任何一条却都可以。**修复选择**先确定一个非空的可用修复族 $F$。普通语义采用 $F=SRep(K)$。优先关系 $\succ$ 则能从中选出较受支持的修复。在这里，它是无环关系，只能连接同属一个极小冲突的断言，不必比较每一对这样的断言。[^formal]三种已有的最优性条件给出相互包含的修复族：

$$
CRep(K,\succ)\subseteq GRep(K,\succ)\subseteq PRep(K,\succ)\subseteq SRep(K).
$$

| 修复族 | 选择条件 |
| --- | --- |
| $SRep$ | 全部按包含关系极大的相容子集。 |
| $PRep$ | 帕累托最优修复：不存在另一相容集合，使其中*至少一条*新增断言优于*每一条*移除断言。 |
| $GRep$ | 全局最优修复：不存在一个*不同的*相容集合，使*每一条*移除断言都被*至少一条*新增断言超过。 |
| $CRep$ | 完备最优修复：在至少一种无环的优先关系补全下全局最优；补全需要比较同属一个极小冲突的每对断言。 |

这些条件比较的是断言的替换，不是数值分数的最大化。因此，P-Brave 或 P-AR 中的 **P** 指帕累托最优修复族，不是答案检验，也不是所有偏好的统称。

精确地说，替换候选 $R'\subseteq A$ 必须与 $T$ 相容。若有一条新增断言 $\beta\in R'\setminus R$ 优于**所有**移除断言 $\alpha\in R\setminus R'$，则 $R'$ 对 $R$ 构成帕累托改进。若 $R'\ne R$，而且**每一条**移除断言都被**某一条**新增断言超过，则构成全局改进。补全在不产生环的条件下扩展 $\succ$，并比较共同出现在极小冲突中的每一对断言；C-修复是在至少一种这种补全下全局最优的修复。「存在」与「所有」的位置不同，使 P、G、C 三种修复不必重合。[^formal]

**答案接受**则固定一个修复族 $F$，向其中的修复提出*同一个*查询 $q$。对回答「是／否」的布尔查询，或对查询的某个固定候选答案，三种检验是：

| 检验 | 恰在何时接受查询 |
| --- | --- |
| Brave | $\exists R\in F:\ (T,R)\models q$。至少一个可用修复推出它。 |
| AR（ABox Repair） | $\forall R\in F:\ (T,R)\models q$。每个可用修复分别推出它。 |
| IAR（Intersection of ABox Repairs） | $(T,\bigcap_{R\in F}R)\models q$。共同保留的断言已经足以推出它。 |

普通 Brave、AR、IAR 取 $F=SRep$；P-Brave、P-AR、P-IAR 取 $F=PRep$。G 与 C 变体则分别代入 $GRep$ 和 $CRep$。每个名称都组合了修复选择与答案条件。在经典单调蕴涵及非空 $F$ 下，**IAR 蕴涵 AR，AR 蕴涵 Brave**。若把修复族缩小为 $F'\subseteq F$，AR 和 IAR 可能增加答案，Brave 则可能失去答案。实际变化还取决于查询和所选修复族，不能从另一个坐标的名称直接推断。

这已经是一张二维地图：$X\in\{S,P,G,C\}$ 选修复族，$Y\in\{IAR,AR,Brave\}$ 选答案检验；组合记作 $X$-$Y$。下面的有界支撑与击败集检验，在答案坐标上补出更多位置。

## 为什么逐个修复与共同部分不同

回到 Ada 的例子：两个修复都推出 $Campus(a)$，所以 **AR 接受 $Campus(a)$**；它们的交集只有 $SignedIn(b)$，所以 **IAR 不接受 $Campus(a)$**。两者都接受 $SignedIn(b)$。Brave 在一个修复中接受 $Park(a)$，在另一个修复中接受 $Library(a)$，但没有修复推出 $Park(a)\land Library(a)$。不能把不同修复的答案直接拼成一份相容的视图。

AR 的全称条件允许各修复用**不同的证明**支持同一个答案；IAR 则要求共同断言本身已经足够。从逻辑接受条件看，IAR 更强。逐个说明不同修复的支撑，可能比从已经确定的共同部分继续推理更费解释；这本身并不说明*找出*修复或交集的计算费用。即使实际探究选择较简便的共同根据，也应保留两种检验的区别。

现在假定公园记录有独立核对过的时间戳，因而优先于图书馆记录：$Park(a)\succ Library(a)$。用 $Park(a)$ 替换 $Library(a)$，就能帕累托改进 $R_{Library}$；$R_{Park}$ 没有这种改进。因此 $PRep=\{R_{Park}\}$。在这个特定例子中，P-Brave、P-AR 和 P-IAR 都接受 $Park(a)$ 与 $Campus(a)$。优先关系改变了可用修复族，存在性、全称性与交集检验的意义没有改变。仅仅希望 Ada 在公园，并不足以给公园记录以证据上的优先地位。

## 有界支撑与击败集

AR 与 IAR 之间，还能更细地追问：需要多少组不同根据，才能覆盖全部修复。查询 $q$ 的一个 **$T$-支撑**，是与 $T$ 相容、且使 $(T,s)\models q$ 的子集 $s\subseteq A$；用 $Supp_T(A,q)$ 收集全部这样的支撑。对 $X\in\{S,P,G,C\}$，令 $F_X=XRep(K,\succ)$；当 $X=S$ 时使用 $SRep(K)$。整数 $k\ge1$ 下的 **$X$-$k$-support** 接受 $q$，当且仅当至多 $k$ 个这样的支撑覆盖全部选定修复：每个 $R\in F_X$ 都包含至少一个支撑。

$$
\begin{aligned}
X\text{-}k\text{-support}(q)\iff{}&\exists m\in\{1,\ldots,k\}\\
&\exists(s_1,\ldots,s_m)\in Supp_T(A,q)^m\\
&\forall R\in F_X\ \exists i\in\{1,\ldots,m\}:\ s_i\subseteq R.
\end{aligned}
$$

Ada 的例子在优先关系为空时，没有一组同时属于两个修复的 $Campus(a)$ 支撑，所以等于 IAR 的 1-support 拒绝它。两组支撑 $\{Park(a)\}$ 与 $\{Library(a)\}$ 分别进入两个修复，2-support 接受它，AR 也接受。对于每个固定的有限知识库，只要 $k\ge|F_X|$，$X$-$k$-support 就与 $X$-AR 相同；不存在对所有知识库一律奏效的有限 $k$。[^thesis]

整数 $k\ge0$ 下的 **$X$-$k$-defeater** 从另一侧检验。$A$ 中每个与 $T$ 相容、大小不超过 $k$ 的挑战集 $D$，都必须能够进入*某一个*选定修复，而该修复推出 $q$。令 $Cons_T(D)$ 表示 $(T,D)$ 有模型：

$$
\begin{aligned}
X\text{-}k\text{-defeater}(q)\iff{}&\forall D\subseteq A:\\
&(|D|\le k\land Cons_T(D))\Rightarrow\\
&\exists R\in F_X:\ D\subseteq R\land (T,R)\models q.
\end{aligned}
$$

这里量化的是 $A$ 中**全部**小型相容子集，包括不能进入任何优先修复的子集。当 $k=0$ 时，只检查空挑战，故 $X$-0-defeater 等于 $X$-Brave。增大 $k$ 会纳入更多挑战，只可能减少答案。公园记录被优先选择后，$D=\{Library(a)\}$ 自身相容，却进不了唯一的 P-修复。因此 P-1-defeater 甚至拒绝 $SignedIn(b)$，尽管 P-AR 接受它。这也说明，不能无条件声称 $X$-AR 下逼近优先修复下的 $X$-$k$-defeater；还需要每个大小不超过 $k$ 的挑战都能扩展为一个选定修复。普通 $S$-修复满足这一条件，因为有限 $A$ 的每个相容子集都能扩展为极大相容子集。[^thesis]

固定 $X$，用 $\preceq$ 表示在指定范围内对全部知识库与查询成立的答案包含关系，则内部两条链为：

$$
X\text{-IAR}=X\text{-1-support}\preceq X\text{-}k\text{-support}
\preceq X\text{-}(k+1)\text{-support}\preceq X\text{-AR},
$$

$$
X\text{-}(k+1)\text{-defeater}\preceq X\text{-}k\text{-defeater}
\preceq X\text{-0-defeater}=X\text{-Brave}.
$$

支撑链取 $k\ge1$，击败集链取 $k\ge0$。此外，$X$-AR 下逼近 $X$-Brave；若无刚才的挑战扩展条件，不应在 AR 处把两条链直接接起来。无优先关系的 $k$-support 与 $k$-defeater 语义由 Bienvenu 和 Rosati 的较早研究提出；加上 $X$ 修复选择的变体，以及它们带条件的关系，见作者修订后的硕士论文。[^k-source][^thesis]

<a id="二维语义框架"></a>

## 二维语义框架

现在，每种语义都可以写成一对 $(X,Y)$：$X$ 选修复，$Y$ 规定一个答案怎样经受这些修复的检验。下表定位组合名称；两组答案检验**不是**从左到右的一条强弱链。

| 选定修复 $X$ | 共同支撑族 $Y_{\cap}$ | 挑战／可能性族 $Y_{\cup}$ |
| --- | --- | --- |
| $S$：全部修复 | S-IAR、S-$k$-support、S-AR | S-$k$-defeater、S-Brave |
| $P$：帕累托 | P-IAR、P-$k$-support、P-AR | P-$k$-defeater、P-Brave |
| $G$：全局最优 | G-IAR、G-$k$-support、G-AR | G-$k$-defeater、G-Brave |
| $C$：完备最优 | C-IAR、C-$k$-support、C-AR | C-$k$-defeater、C-Brave |

这里比较的是**全局答案包含**：$X_1$-$Y_1\preceq X_2$-$Y_2$ 指在指定范围内的**每个**知识库、**每个**查询上，前者接受的答案都被后者接受。单个例子上的相等，不等于两种语义等价。修复坐标按 $S\le_X P\le_X G\le_X C$ 排列：向右移动，选定的修复族可能缩小，但不会变大。$Y_{\cap}=\{IAR,1\text{-support},2\text{-support},\ldots,AR\}$ 内部按支撑链排序。$Y_{\cup}=\{0\text{-defeater},1\text{-defeater},\ldots\}$ 内部按击败集链排序，其中 0-defeater 等于 Brave。

**两个乘积序。**这里 $T$「协调」指它有模型，而且所讨论的具名概念和角色相对于它可满足。在有限、$T$ 协调、没有单断言冲突、优先关系无环且只连接同属一个极小冲突的断言、允许任意有限符号集的 DL-Lite 优先知识库上，对包含基实例查询的正合取查询，修订论文在合并等价的端点名称后，证明了以下精确关系：[^thesis]

$$
\begin{aligned}
Y_1,Y_2\in Y_{\cap}:\quad
&(X_1,Y_1)\preceq(X_2,Y_2)
\iff X_1\le_X X_2\ \land\ Y_1\le_{\cap}Y_2,\\
Y_1,Y_2\in Y_{\cup}:\quad
&(X_1,Y_1)\preceq(X_2,Y_2)
\iff X_2\le_X X_1\ \land\ Y_1\le_{\cup}Y_2.
\end{aligned}
$$

两组内部各有一个**乘积格**：共同支撑检验为 $X\times Y_{\cap}$，挑战／可能性检验为 $X^{op}\times Y_{\cup}$。格使每一对元素都有一个*最大下界*（交，$\wedge$）和*最小上界*（并，$\vee$），比较依据是答案包含。后一组把修复坐标反向。按坐标计算，共同支撑族的交取较小的 $X$ 与较小的 $Y$，并取两者各自较大的值；挑战族的交取较大的 $X$ 与较小的 $Y$，并取较小的 $X$ 与较大的 $Y$。因此，第一组中 $\text{P-IAR}\wedge\text{S-AR}=\text{S-IAR}$，$\text{P-IAR}\vee\text{S-AR}=\text{P-AR}$。挑战族中每对元素都有交与并，但因有限 $k$ 没有最大值，该族没有最小元素。

为什么两个乘积序的方向不同？缩小修复族有利于全称检验或支撑覆盖，却可能删去存在性的见证，或使一个小挑战无法进入任何选定修复。固定 $X$ 时，容许更多支撑会增加答案，容许更大挑战则会减少答案。这些事实说明**坐标条件足以推出答案包含**。坐标条件的**必要性**还需分离构造：一个冲突区分 $S/P$，论文另用有限冲突区分 $P/G$ 与 $G/C$。在支撑坐标上，设有 $n$ 条相互不相容的记录，每条分别推出同一个主张；AR 接受这个主张，$k$-support 则恰在 $k\ge n$ 时接受。独立的冲突对同样能够区分击败集参数的各有限界限。论文在所述范围内证明这些严格性结果。[^thesis]这里没有为两组语义合造一个乘积序，这些序也不表示往 ABox 增添数据会保留答案。

Ada 的例子已经能区分一对跨坐标语义。若 $Park(a)\succ Library(a)$，**P-IAR 接受 $Park(a)$**，普通 **S-AR 则拒绝**，因为 $R_{Library}$ 仍是普通修复。若优先关系*为空*，P-修复与普通修复相同：**S-AR 接受 $Campus(a)$**，因为两个修复都推出它；**P-IAR 则拒绝**，因为交集仅为 $\{SignedIn(b)\}$。因此 P-IAR 与普通 AR **全局不可比**：两个可能的答案包含方向分别遇到了反例。这不是说每个固定知识库上两者的答案都不同。修复变少与共同依据检验变强，是两种相反的移动，不能合成一个笼统的「更加谨慎」。

跨两组语义还能得到范围较窄的关系。令修复选择 $X,Z\in\{S,P,G,C\}$、整数 $h,k\ge1$，取任一共同支撑语义 $I_X\in\{X\text{-IAR},X\text{-}h\text{-support},X\text{-AR}\}$。每个这样的 $I_X$ 在全局答案包含意义下都严格低于任意 $Z$-Brave。若 $X=Z=S$，$I_S$ 还严格低于普通 S-$k$-defeater。其他 $I_X$ 与 $Z$-$k$-defeater 的配对则全局不可比：即使每个优先修复都推出主张，一个挑战也可能进入不了任何优先修复；较小的挑战界限也可能接受某个选定修复并不支持的主张。跨组关系要由自己的见证证明，不能仅从两个乘积序推出。[^thesis]

## 自然语言能够借用什么

不用数学符号，也能准确说出量词：「至少一个可用且相容的视图支持**同一主张**」（Brave）；「每个可用视图都支持**同一主张**，理由可以不同」（AR）；「所有视图共同保留的根据就支持它」（IAR）。这些说法要有内容，先须确定共同问题、相关视图、各自根据，以及偏好是否真正适用于视图之间的选择。不同的人、时间或条件下的报告，未必构成冲突。作者在论文自评中还指出，实际思考时，依据选择与答案接受的态度可能交融得难以辨认；形式上的分开，为检视这种经验提供问题，并不证明某种心理机制。[^assessment]

在 [YY-13](core-views.zh-CN.md#yy-13) 中，作者**用自然语言采用 P-AR**，判断个人环境能否系住主体。他的偏好选定八个需要考察的方面；在每种选定读法下，同一个判断都要有根据：环境须让本人接续活动，也让偏离原意的做法可以得到纠正。「作品—伙伴—环境」一行可考察伙伴能否指出作品遗漏了什么、工具能否让工作继续；「网页—生活体验的环境—GitHub」一行可考察表达、使用与留存来源是否使本人能够返回并修订。各行理由不同，所判断的仍是同一件事。八行贯通同一说明的不同面向，不是八个字面意义上的 ABox 修复。要称作描述逻辑中计算得到的 P-AR 蕴涵，还需明确本体、断言、冲突、优先关系、修复与查询。[偏好 Harness](preference-harness.zh-CN.md)进一步讨论偏好怎样参与选择；[推理](reasoning.zh-CN.md)讨论支撑与后来的纠正怎样回应世界。

形式修复语义保持 $T$ 与问题不变，再检验答案。实际探究还可以修订概念、问题、根据与优先关系。当前视图的共同后果与重构旧前提是不同成果；把它们分清，既能在局部可靠推论，也容许理解本身发生改变。

[^formal]: Meghyn Bienvenu 与 Camille Bourgaux，[《Querying and Repairing Inconsistent Prioritized Knowledge Bases: Complexity Analysis and Links with Abstract Argumentation》，第 2–3 节](https://arxiv.org/html/2003.05746v5#S3)，arXiv:2003.05746v5，2026。本文采用该公开来源的修复、优先关系、P／G／C 选择及 Brave／AR／IAR 定义；Ada 的例子和自然语言应用是本文的说明。

[^k-source]: Meghyn Bienvenu 与 Riccardo Rosati，[《Tractable Approximations of Consistent Query Answering for Robust Ontology-Based Data Access》](https://ijcai.org/proceedings/2013/121)，IJCAI 2013。无优先关系的 $k$-support 与 $k$-defeater 语义始于这项研究。

[^thesis]: 刘博，《描述逻辑 DL-Lite 容纳不一致语义研究》，2026 年 10 月 29 日「证明与推断符合形式版」，第 3.1–3.2 节及附录 A。本文把带 $X$ 选择的 $k$ 变体、两个乘积序结果及带条件的跨组比较归属于这份修订论文，不复制原稿。

[^assessment]: 刘博，《硕士论文特色自我评述》，随论文提交的自评，2026 年，「贡献」部分。关于实际推理的观察在这里充当解释动机，不是形式系统的定理。
