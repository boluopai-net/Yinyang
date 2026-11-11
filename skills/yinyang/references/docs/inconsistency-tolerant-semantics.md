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

## Why all repairs and their intersection differ

In the example, both repairs entail $Campus(a)$, so **AR accepts $Campus(a)$**. Their intersection contains only $SignedIn(b)$, so **IAR does not accept $Campus(a)$**. Both AR and IAR accept $SignedIn(b)$. Brave accepts $Park(a)$ under one repair and $Library(a)$ under the other, but no repair entails $Park(a)\land Library(a)$. Answers obtained from different repairs cannot simply be combined as one consistent view.

AR's universal test allows the repairs to supply *different proofs of the same answer*. IAR tests whether the common assertion core is sufficient. In that logical sense IAR is the stronger acceptance condition. Checking each repair's support can require a more elaborate explanation than reasoning from an already identified common core; that observation says nothing by itself about the computational cost of *finding* the repairs or their intersection. The two tests must remain distinct even when a practical inquiry takes a simpler common-ground route.

Now suppose the park report has an independently checked timestamp and is given priority over the library report: $Park(a)\succ Library(a)$. $R_{Library}$ admits a Pareto improvement by replacing $Library(a)$ with $Park(a)$; $R_{Park}$ does not. Thus $PRep=\{R_{Park}\}$. P-Brave, P-AR, and P-IAR all accept $Park(a)$ and $Campus(a)$ in this particular case. Priority changed the eligible family, while the existential, universal, and intersection tests retained their meanings. Merely wanting Ada to have been in the park would provide no evidential reason to prefer that report.

## What natural language can borrow

The quantifiers do not require mathematical notation to be exact. One may say: “At least one eligible consistent view supports **this same claim**” (Brave); “Every eligible view supports **this same claim**, perhaps for different reasons” (AR); or “The grounds common to all eligible views already support it” (IAR). The phrases are useful only after the inquiry identifies the common question, the relevant views, their support, and any preference that actually selects among them. Reports about different people, times, or conditions need not be conflicting views in the first place.

In [YY-13](core-views.md#yy-13), the author adopts **P-AR in natural language** to judge whether a personal environment holds the subject. His preference selects eight aspects for consideration. Under each selected reading, the same judgment needs a reason: the environment lets him continue his activity and correct departures from his purpose. The work–counterpart–environment row can ask whether a counterpart notices something missing from a work and whether tools let that work continue; the website–experienced environment–GitHub row can ask whether expression, use, and retained sources let him return and revise. These reasons differ, while the judgment under examination stays the same. The eight rows connect aspects within one account; they are not eight literal ABox repairs. A computed P-AR entailment would additionally require a specified ontology, assertions, conflicts, priority, repairs, and query. [Preference Harness](preference-harness.md) develops the role of preference; [Reasoning](reasoning.md) develops how support and later correction remain answerable to the world.

Formal repair semantics keeps $T$ and the question fixed while it tests answers. Inquiry can also revise its concepts, question, grounds, and priorities. A common consequence across present views and a reconstructed premise are different achievements; the distinction leaves room for both dependable local inference and a changed understanding.

[^formal]: Meghyn Bienvenu and Camille Bourgaux, [“Querying and Repairing Inconsistent Prioritized Knowledge Bases: Complexity Analysis and Links with Abstract Argumentation,” §§2–3](https://arxiv.org/html/2003.05746v5#S3), arXiv:2003.05746v5, 2026. The repair, priority, P/G/C selection, and Brave/AR/IAR definitions used here follow this public source. The worked example and natural-language application are this page's exposition.
