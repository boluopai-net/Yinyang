# Inconsistency-tolerant semantics: repairs, priorities, and answers

[Home](../../README.md) · [Preference Harness](preference-harness.md) · [Reasoning](reasoning.md) · [简体中文](inconsistency-tolerant-semantics.zh-CN.md)

Suppose one report places Ada in the park and another places her in the library at the very same moment. Both places are on campus, but she cannot be in both at once. A separate report says Ben signed in. The disagreement about Ada should not erase what is known about Ben, nor should it prevent us from asking whether Ada was on campus. **Inconsistency-tolerant semantics** gives this question a precise form. In ordinary classical logic, the contradictory records together have no model and entail every query; selecting consistent parts lets an answer mean something again.

The account turns on two choices: **which consistent selections are eligible**, and **what support a query needs across those selections**. The formal case makes the difference clear enough to carry into ordinary reasoning.

## Fixed rules and maximal consistent repairs

The rules in the example say that being in either place means being on campus, and that the same person cannot be in both places at that moment. The reports say where Ada was and that Ben signed in. In description logic, the rulebook is an **ontology** $T$, and the finite collection of recorded facts is an **ABox** $A$; together they form a knowledge base $K=(T,A)$. We assume $T$ itself is consistent. A query follows from $T$ and a selected set of records $R$, written $(T,R)\models q$, when **every classical model** satisfying both also satisfies $q$. One model merely allowing $q$ is not enough.

A **repair** is a subset $R\subseteq A$ that is consistent with $T$ and inclusion-maximal within $A$: no further assertion from $A$ can be added without inconsistency. Maximal means that no assertion can be added, not that $R$ has the largest number of assertions. Let $SRep(K)$ be the family of all repairs. It is nonempty for a finite $A$ and consistent $T$, even when $A$ as a whole is inconsistent.[^formal]

Using $a$ for Ada and $b$ for Ben, the same example becomes

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

$Park(a)$ and $Library(a)$ conflict, while $SignedIn(b)$ is unaffected. The two repairs are $R_{Park}=\{Park(a),SignedIn(b)\}$ and $R_{Library}=\{Library(a),SignedIn(b)\}$. Each is consistent, and neither can be enlarged using $A$. In both, $Campus(a)$ follows, though from a different premise. The shared assertions are only $R_{Park}\cap R_{Library}=\{SignedIn(b)\}$, from which $Campus(a)$ does not follow. This example keeps the rules fixed while it compares the reports; changing the rules would pose a new question.

## Two choices, not one scale

The park and library reports form a **minimal conflict**: together they violate a rule, while either report alone does not. The **repair-selection** choice identifies a nonempty eligible family $F$. Plain semantics uses $F=SRep(K)$. A priority relation $\succ$ can instead select preferred repairs. In the framework used here it is acyclic and relates only assertions occurring together in a minimal conflict; it need not compare every such pair.[^formal] Three established notions of optimality yield nested families:

$$
CRep(K,\succ)\subseteq GRep(K,\succ)\subseteq PRep(K,\succ)\subseteq SRep(K).
$$

| Family | Selection condition |
| --- | --- |
| $SRep$ | All inclusion-maximal consistent subsets. |
| $PRep$ | Pareto-optimal repairs: no consistent replacement adds an assertion preferred to **every** assertion it removes. |
| $GRep$ | Globally optimal repairs: no **different** consistent replacement makes every removed assertion lose to **some** added assertion. |
| $CRep$ | Completion-optimal repairs: globally optimal under at least one acyclic extension of the priority relation that compares every pair occurring together in a minimal conflict. |

These conditions concern replacing assertions, not maximizing a numerical score. In particular, **P** in P-Brave or P-AR names the Pareto-selected repair family. It is not the answer test, nor a general name for any expressed preference.

More precisely, a candidate replacement $R'\subseteq A$ must be consistent with $T$. It Pareto-improves $R$ if some added $\beta\in R'\setminus R$ is preferred to **all** removed $\alpha\in R\setminus R'$. It globally improves $R$ if $R'\ne R$ and **each** removed $\alpha$ is outranked by **some** added $\beta$. A completion extends $\succ$ without a cycle and compares every pair sharing a minimal conflict; a C-repair is globally optimal for at least one such completion. These different placements of “some” and “all” are why P-, G-, and C-repairs need not coincide.[^formal]

The **answer-acceptance** choice fixes one family $F$ and asks the *same* query $q$ of it. For a yes/no (Boolean) query, or for a fixed candidate answer to a query, the three tests are:

| Test | The query is accepted exactly when… |
| --- | --- |
| Brave | $\exists R\in F:\ (T,R)\models q$. At least one eligible repair entails it. |
| AR (ABox Repair) | $\forall R\in F:\ (T,R)\models q$. Every eligible repair separately entails it. |
| IAR (Intersection of ABox Repairs) | $(T,\bigcap_{R\in F}R)\models q$. Their common assertions already entail it. |

Ordinary Brave, AR, and IAR use $F=SRep$; P-Brave, P-AR, and P-IAR use $F=PRep$. G- and C-variants substitute $GRep$ and $CRep$. These are combinations of a selection condition with an answer condition. Under classical monotonic entailment and nonempty $F$, **IAR implies AR, and AR implies Brave**. For a smaller selected family $F'\subseteq F$, AR and IAR can gain answers, whereas Brave can lose answers. The precise result depends on the query and the chosen family; neither axis can be inferred from the other's name.

This is already a two-coordinate map: $X\in\{S,P,G,C\}$ chooses a repair family, and $Y\in\{IAR,AR,Brave\}$ chooses an answer test. We write their combination $X$-$Y$. The bounded support and defeater tests below fill in more positions along the answer coordinate.

## Why all repairs and their intersection differ

In the example, both repairs entail $Campus(a)$, so **AR accepts $Campus(a)$**. Their intersection contains only $SignedIn(b)$, so **IAR does not accept $Campus(a)$**. Both AR and IAR accept $SignedIn(b)$. Brave accepts $Park(a)$ under one repair and $Library(a)$ under the other, but no repair entails $Park(a)\land Library(a)$. Answers obtained from different repairs cannot simply be combined as one consistent view.

AR's universal test allows the repairs to supply *different proofs of the same answer*. IAR tests whether the common assertion core is sufficient. In that logical sense IAR is the stronger acceptance condition. Checking each repair's support can require a more elaborate explanation than reasoning from an already identified common core; that observation says nothing by itself about the computational cost of *finding* the repairs or their intersection. The two tests must remain distinct even when a practical inquiry takes a simpler common-ground route.

Now suppose the park report has an independently checked timestamp and is given priority over the library report: $Park(a)\succ Library(a)$. $R_{Library}$ admits a Pareto improvement by replacing $Library(a)$ with $Park(a)$; $R_{Park}$ does not. Thus $PRep=\{R_{Park}\}$. P-Brave, P-AR, and P-IAR all accept $Park(a)$ and $Campus(a)$ in this particular case. Priority changed the eligible family, while the existential, universal, and intersection tests retained their meanings. Merely wanting Ada to have been in the park would provide no evidential reason to prefer that report.

## Bounded supports and defeaters

AR and IAR are endpoints of a finer way to ask how many separate grounds are needed. A **$T$-support** for $q$ is a $T$-consistent subset $s\subseteq A$ such that $(T,s)\models q$; let $Supp_T(A,q)$ collect all of them. For $X\in\{S,P,G,C\}$, write $F_X=XRep(K,\succ)$, using $SRep(K)$ when $X=S$. **$X$-$k$-support**, for an integer $k\ge1$, accepts $q$ when at most $k$ such supports cover the selected repairs: every $R\in F_X$ contains at least one of them.

$$
\begin{aligned}
X\text{-}k\text{-support}(q)\iff{}&\exists m\in\{1,\ldots,k\}\\
&\exists(s_1,\ldots,s_m)\in Supp_T(A,q)^m\\
&\forall R\in F_X\ \exists i\in\{1,\ldots,m\}:\ s_i\subseteq R.
\end{aligned}
$$

With the empty priority in Ada's example, no one support for $Campus(a)$ lies in both repairs, so 1-support, which equals IAR, rejects it. Two supports, $\{Park(a)\}$ and $\{Library(a)\}$, cover the two repairs; 2-support accepts it, as AR does. For every fixed finite knowledge base, $k\ge|F_X|$ suffices for $X$-$k$-support to coincide with $X$-AR. There is no single finite $k$ that gives this equality on all knowledge bases.[^thesis]

**$X$-$k$-defeater**, for an integer $k\ge0$, looks from the other side. Every $T$-consistent challenge $D\subseteq A$ of size at most $k$ must fit inside *some* selected repair that entails $q$. Write $Cons_T(D)$ when $(T,D)$ has a model:

$$
\begin{aligned}
X\text{-}k\text{-defeater}(q)\iff{}&\forall D\subseteq A:\\
&(|D|\le k\land Cons_T(D))\Rightarrow\\
&\exists R\in F_X:\ D\subseteq R\land (T,R)\models q.
\end{aligned}
$$

The challenge ranges over **all** small consistent subsets of $A$, including ones that no preferred repair contains. At $k=0$, only the empty challenge is tested, so $X$-0-defeater equals $X$-Brave. Raising $k$ admits more possible challenges and can only remove answers. With the park report preferred, the consistent challenge $D=\{Library(a)\}$ cannot enter the sole P-repair. Therefore P-1-defeater rejects even $SignedIn(b)$, although P-AR accepts it. This sharp edge prevents an unconditional claim that $X$-AR lies below $X$-$k$-defeater for preferred $X$; that implication needs every challenge of size at most $k$ to extend to a selected repair. It does hold for ordinary $S$-repairs, because every consistent subset of a finite $A$ extends to a maximal one.[^thesis]

For fixed $X$, with $\preceq$ meaning answer inclusion on all knowledge bases and queries in the stated scope, the two internal chains are:

$$
X\text{-IAR}=X\text{-1-support}\preceq X\text{-}k\text{-support}
\preceq X\text{-}(k+1)\text{-support}\preceq X\text{-AR},
$$

$$
X\text{-}(k+1)\text{-defeater}\preceq X\text{-}k\text{-defeater}
\preceq X\text{-0-defeater}=X\text{-Brave}.
$$

Here $k\ge1$ in the support chain and $k\ge0$ in the defeater chain. $X$-AR also lies below $X$-Brave. The two chains should not be joined at AR without the challenge-extension condition just stated. The unprioritized $k$-support and $k$-defeater families were introduced in earlier work by Bienvenu and Rosati; the $X$-selected versions and their qualified relations are developed in the author's revised thesis.[^k-source][^thesis]

<a id="two-dimensional-framework"></a>

## The two-dimensional framework

Each semantics is now a pair $(X,Y)$: $X$ selects repairs, while $Y$ says how one answer survives them. The matrix locates the named combinations; its columns are **families of answer tests**, not a single left-to-right ranking.

| Selected repairs $X$ | Common-support family $Y_{\cap}$ | Challenge/possibility family $Y_{\cup}$ |
| --- | --- | --- |
| $S$: all repairs | S-IAR, S-$k$-support, S-AR | S-$k$-defeater, S-Brave |
| $P$: Pareto | P-IAR, P-$k$-support, P-AR | P-$k$-defeater, P-Brave |
| $G$: global | G-IAR, G-$k$-support, G-AR | G-$k$-defeater, G-Brave |
| $C$: completion | C-IAR, C-$k$-support, C-AR | C-$k$-defeater, C-Brave |

The comparison is **global answer inclusion**: $X_1$-$Y_1\preceq X_2$-$Y_2$ means that every answer accepted by the first is accepted by the second for **every** knowledge base and query in the class. Equality on one example is not equivalence of semantics. The repair coordinate is ordered $S\le_X P\le_X G\le_X C$: moving right can shrink the selected repair family, which never grows. Within $Y_{\cap}=\{IAR,1\text{-support},2\text{-support},\ldots,AR\}$, the support chain gives its answer order. Within $Y_{\cup}=\{0\text{-defeater},1\text{-defeater},\ldots\}$, the defeater chain gives its answer order, with $0$-defeater equal to Brave.

**Two product orders.** Here *coherent* $T$ means that $T$ has a model and the named concepts and roles under discussion can be instantiated relative to it. For finite prioritized DL-Lite knowledge bases with coherent $T$, no singleton conflicts, acyclic conflict-local priorities, arbitrary finite signatures, and positive conjunctive queries including ground instance queries, the revised thesis establishes, after identifying the equivalent endpoint names, these exact comparisons:[^thesis]

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

Each subfamily is a **product lattice**: $X\times Y_{\cap}$ for common-support tests, and $X^{op}\times Y_{\cup}$ for challenge/possibility tests. A lattice gives every pair a *greatest lower bound* (meet, $\wedge$) and a *least upper bound* (join, $\vee$) in answer inclusion. The second product reverses the repair axis. In coordinate terms, on the common-support side the meet takes the smaller $X$ and smaller $Y$, while the join takes the larger of each; on the challenge side the meet takes the larger $X$ and smaller $Y$, while the join takes the smaller $X$ and larger $Y$. Thus, within the first product, $\text{P-IAR}\wedge\text{S-AR}=\text{S-IAR}$ and $\text{P-IAR}\vee\text{S-AR}=\text{P-AR}$. The challenge-side chain has pairwise meets and joins but no least member, since its finite $k$ values have no largest bound.

Why do the product directions differ? Removing repairs helps a universal or support-covering test, but can remove an existential witness or leave a small challenge unable to enter any selected repair. At fixed $X$, allowing more supports gains answers; allowing larger challenges loses answers. These facts establish **sufficiency** of the coordinate conditions in the displayed comparisons. **Necessity** requires counterexamples: a single conflict separates $S$ from $P$; the thesis constructs further finite conflicts separating $P/G$ and $G/C$. For the support coordinate, imagine $n$ mutually incompatible reports, each separately implying one claim: AR accepts the claim, while $k$-support accepts it only when $k\ge n$. Independent conflict pairs similarly separate successive finite defeater bounds. The thesis proves these strictness results for the stated class.[^thesis] No single product order is asserted across the two subfamilies, and none of these orders says that adding ABox data preserves answers.

The Ada example already supplies a diagonal separation. With $Park(a)\succ Library(a)$, **P-IAR accepts $Park(a)$**, while ordinary **S-AR rejects it** because $R_{Library}$ remains an ordinary repair. With the *empty* priority relation, P-repairs equal ordinary repairs: **S-AR accepts $Campus(a)$**, since both repairs entail it, while **P-IAR rejects it**, since their intersection is only $\{SignedIn(b)\}$. Thus P-IAR and ordinary AR are **globally incomparable**: each proposed inclusion has a counterexample. This does not say that their answers differ on every fixed knowledge base. The two opposed movements—fewer repairs and a stronger common-core test—cannot be collapsed into one notion of being more cautious.

Across the two subfamilies, a narrower statement is still possible. Let $X,Z\in\{S,P,G,C\}$ and integers $h,k\ge1$, and take any common-support semantics $I_X\in\{X\text{-IAR},X\text{-}h\text{-support},X\text{-AR}\}$. Every such $I_X$ is strictly below every $Z$-Brave in global answer inclusion. When $X=Z=S$, $I_S$ is also strictly below S-$k$-defeater. For all other pairs $I_X$ versus $Z$-$k$-defeater, neither direction holds globally: a challenge may be unable to enter a preferred repair even when all preferred repairs entail the claim, while a small challenge bound may accept a claim that some selected repair does not. These cross-family comparisons require their own witnesses; the two product orders alone do not settle them.[^thesis]

## What natural language can borrow

The quantifiers do not require mathematical notation to be exact. One may say: “At least one eligible consistent view supports **this same claim**” (Brave); “Every eligible view supports **this same claim**, perhaps for different reasons” (AR); or “The grounds common to all eligible views already support it” (IAR). The phrases are useful only after the inquiry identifies the common question, the relevant views, their support, and any preference that actually selects among them. Reports about different people, times, or conditions need not be conflicting views in the first place. In the author's reflection on the thesis, selection of grounds and readiness to accept an answer can feel fused in ordinary thought; the formal separation gives that experience a question to examine, not an established psychological mechanism.[^assessment]

In [YY-13](core-views.md#yy-13), the author adopts **P-AR in natural language** to judge whether a personal environment holds the subject. His preference selects eight aspects for consideration. Under each selected reading, the same judgment needs a reason: the environment lets him continue his activity and correct departures from his purpose. The work–counterpart–environment row can ask whether a counterpart notices something missing from a work and whether tools let that work continue; the website–experienced environment–GitHub row can ask whether expression, use, and retained sources let him return and revise. These reasons differ, while the judgment under examination stays the same. The eight rows connect aspects within one account; they are not eight literal ABox repairs. A computed P-AR entailment would additionally require a specified ontology, assertions, conflicts, priority, repairs, and query. [Preference Harness](preference-harness.md) develops the role of preference; [Reasoning](reasoning.md) develops how support and later correction remain answerable to the world.

Formal repair semantics keeps $T$ and the question fixed while it tests answers. Inquiry can also revise its concepts, question, grounds, and priorities. A common consequence across present views and a reconstructed premise are different achievements; the distinction leaves room for both dependable local inference and a changed understanding.

[^formal]: Meghyn Bienvenu and Camille Bourgaux, [“Querying and Repairing Inconsistent Prioritized Knowledge Bases: Complexity Analysis and Links with Abstract Argumentation,” §§2–3](https://arxiv.org/html/2003.05746v5#S3), arXiv:2003.05746v5, 2026. The repair, priority, P/G/C selection, and Brave/AR/IAR definitions used here follow this public source. The worked example and natural-language application are this page's exposition.

[^k-source]: Meghyn Bienvenu and Riccardo Rosati, [“Tractable Approximations of Consistent Query Answering for Robust Ontology-Based Data Access”](https://ijcai.org/proceedings/2013/121), IJCAI 2013. This work introduced the unprioritized $k$-support and $k$-defeater families.

[^thesis]: Bo Liu, *描述逻辑 DL-Lite 容纳不一致语义研究* [*Inconsistency-Tolerant Semantics in Description Logic DL-Lite*], revised formal version, 29 October 2026, §§3.1–3.2 and Appendix A. The $X$-selected $k$ variants, two product-order results, and qualified cross-family comparisons are attributed to this thesis. The source manuscript is not reproduced here.

[^assessment]: Bo Liu, *硕士论文特色自我评述* [*Distinctive Self-Assessment of the Master's Thesis*], accompanying statement, 2026, “Contributions.” The observation about lived reasoning is an interpretive motivation, not a theorem of the formal system.
