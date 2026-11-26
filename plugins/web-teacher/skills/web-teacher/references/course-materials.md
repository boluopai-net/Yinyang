# Course materials

Use this branch when preparing, revising or validating saved Course material.
The root Skill owns teaching, evidence, actor and State boundaries.
Study companions belong to their respective sources. For a practice
path, use [Learning-path governance](learning-path-governance.md#author-a-practice-path).

When a course combines several source formats, apply
[Course sources and entry](course-sources-and-entry.md) to their selection and
integration.

## Three files for each named study source

Choose the companion set by the source and selected study approach.
Mathematical, scientific and technical study uses three files. Humanities
study such as philosophy or interpretive textual study uses a guide and a
glossary. A bounded request can limit the scope of either arrangement.

1. **Study and research guide** develops the source and connects its units, questions and evidence.
2. **Detailed glossary** explains source-specific terms and distinctions.
3. **Practice file** opens the existing source exercises or experiment
   instructions suited to the selected work. Link available answers separately
   or provide a checked, clearly attributed reference answer. In humanities
   study, develop argument and evidence analysis in the guide.

A course has one companion set in teaching-unit order when its own teaching
materials support one. Continuous prose lecture notes and slides/PPT are
alternative or complementary carriers of that same course content. Keep them
in one course glossary and guide. Each selected textbook, reference book or
paper gets a separate set named for the actual work and ordered within its
selected scope. Independent books stay separate even when they support the
same course units. A coauthored book is a single work. Attribute material used
for comparison or supplementation to its own source. If the course mainly
supplies reading priorities and sequence, link the book and paper sets from
the course entrance. Reuse a maintained set when the source and study scope
match. An experiment taught within a course can have an addressable entry
in its course practice file.

In each file, place direct links to its sibling files immediately after the
title and before the study content. Link corresponding concepts, units and
exercises in the body where the reader needs them. Use the
[module entrance method](course-sources-and-entry.md#prepare-a-reachable-learning-entrance)
for the reader's entry into each source. Before handoff, follow each sibling
link and check that its destination serves the same source and scope.

Choose and combine three writing approaches: mathematics, technical study,
and philosophy. Here technical study is a broad material-organizing category
that includes scientific investigation, methods and tools, and engineering
realization; it does not assert that these disciplines are identical. All three
share source grounding, an independent glossary and relevant learner/research
connections. Preparation supplies support; learning evidence stays with State.

## Select the writing approach

Judge the actual source and current question rather than its folder, title or
department. For substantial saved material, briefly state the primary approach
and any supporting emphasis that materially changes the explanation. A sentence
such as “Mathematics-led, with computational experiments” or “Technical study,
emphasizing empirical modeling and engineering implementation” is enough.
Use the learner's language in the saved material. This is an explanation of
how to read the material, not a score, permanent discipline assignment or new
metadata registry. A clear single approach needs no elaborate classification.

| Approach | What the main guide develops | What supports its conclusions |
| --- | --- | --- |
| Mathematics | Objects, definitions, notation, assumptions, statements and their formal relationships; develop needed derivations, proofs, examples and counterexamples in the guide. Distinguish a definition, a result under conditions and an application. | Valid reasoning under explicit assumptions; computations and examples illuminate or test candidates but do not replace a general proof. |
| Technical study | Connect the problem, representation, model or method, operations and observable consequences. Combine the scientific, methodological and engineering emphases below as the selected work needs. | Evidence appropriate to the claim: empirical comparison, formal properties, computational behavior or actual system performance. A successful run establishes only what it checks. |
| Philosophy | Develop situated concepts, problems, theses, reasons, distinctions, objections, responses and interpretive alternatives under the philosophy branch. | Source interpretation and argument, with factual or formal claims checked on their own grounds. Preserve the source's ambiguity and historical differences where material. |

In mathematics, make domains, quantifiers, dimensions and assumptions explicit
where they determine meaning. Explain which objects a statement connects, what
its conditions permit, and how changing a condition changes the conclusion.
Distinguish necessary from sufficient conditions and an equivalence from a
one-way implication. Develop the proof or derivation needed for understanding
in the main guide, with counterexamples at the relevant boundary; retain only
the precise statement and conditions in the glossary. Applied interpretation
belongs beside the formal result, with the additional modeling assumptions
visible. This supports mathematical understanding without making unaided
proof production or memorization a prerequisite.

Within technical study, distinguish these contributions without creating three
more compulsory document sets:

- **Scientific investigation:** phenomena, measurement and operationalization,
  hypotheses or explanatory models, observations and experimental design,
  uncertainty, competing explanations and limits of generalization. State what
  evidence would distinguish the accounts; a simulation alone does not establish
  a claim about the observed world.
- **Methods and tools:** representations, algorithms, procedures, inputs and
  outputs, applicability conditions, mechanisms, comparisons and failure modes.
  Explain how a method works and what its result means rather than only listing
  commands or interfaces.
- **Engineering realization:** the intended function, requirements, constraints,
  architecture and interfaces, implementation choices, tradeoffs, verification
  and operation of an actual artifact or system. Connect success to the intended
  use and observable acceptance, not merely construction or execution.

These emphases can recur within one unit. An empirical model may need software,
but scientific modeling does not automatically make engineering the main study
object. Using a technique does not require a separate technique course.
Conversely, calling an implemented model “research” does not remove its
implementation and validation needs. Mathematics can supply a formal component
of either work without making its empirical claims mathematical theorems.

For mixed sources, choose the main explanatory progression and bring in the
other approach where it contributes. Philosophy of science can be philosophy-led
with a scientific case; a computational psychology study can be technical,
emphasizing scientific evidence with mathematical and engineering support.
Ontology work may be philosophical clarification, formal semantics, or
engineering a usable schema and reasoner: inspect the actual task. The words
“conceptual engineering” alone do not establish an artifact-building task.
Do not force all material into three repeated sections, split one connected
explanation into competing guides, or relocate corpus folders to enact this
writing distinction. Language learning keeps its own applicable method.

## Required independent glossary

Use `术语与名词解释表` for the detailed glossary in Chinese. The glossary owns
definitions, conditions, distinctions and compact examples.

Maintain one separate `词表` file per learning-path module. Keep the terms and
their source-specific definitions in their respective vocabulary and glossary
files. The module work page links to those files. Use Markdown tables with
`单元` and `词条` columns in Chinese (Unit and Terms in English). Use actual
course and book titles as separate headings, including the actual title of
an adopted textbook or handbook. Give each lecture, chapter or coherent unit
group a row in its own source order. Connect related course units and book
chapters with links.
Under a heading, the Unit cell gives just the unit name. Give each paper and
project one Unit row by default. Use a short recognizable paper name in the
Unit cell. A paper with substantively distinct parts can span several rows,
each naming the paper and the part. The Terms cell lists vocabulary from the
unit in the same row.
Keep bilingual names together in that cell when useful. Show all rows
directly in reading view. Put primary sources first, followed by supplements.
Separate Chinese terms with `、`. Link each term or coherent group directly to
its source-specific explanation.

For substantial saved study material, prepare the relevant glossary scope first.
Keep it as a separate file regardless of length: the user needs it to recognize
and recover concepts, not as an optional appendix after memorization. Begin with
a concept map rendered as a diagram, followed by detailed entries and
verified source associations. The map uses visible concept nodes and connections
with meaningful relations: for example dependency, distinction, representation,
explanation, evidence or transformation. Link its concepts to the maintained
entries where the reading surface supports that navigation. Use Mermaid or
another supported diagram/image format and check its rendered legibility.
A prose outline, bullet list, table of contents or collection of linked names
does not substitute for the diagram. Do not add a separate “conceptual
throughline” section; put needed connected explanation in the main guide.
A short diagram legend may explain a symbol or relation without becoming a
second exposition. The detailed glossary also needs a fitting amount of
explanatory visuals beside the terms whose meaning, conditions or distinctions
they clarify; the opening map does not replace these local visual explanations.
Preserve useful depth and source order. Philosophy
uses its branch's contextual depth; technical material retains the definitions,
symbols, conditions and mathematical statements needed to recognize its objects.

Connect the guide's named concepts directly to their glossary headings or blocks,
and give reciprocal unit/return navigation. Ground a needed term briefly at its
point of use so reading does not require memorization or constant switching;
retain the detailed maintained definition in the glossary. Neither one giant
file nor a page of links substitutes for this relationship. An isolated question
does not require producing a whole book's materials first.

## Mathematics and technical study: three connected documents

Mathematical and technical sources use their actual knowledge and training
structure, with the distinct writing approaches above. Maintain:

1. **Glossary** — the independent recognition support above.
2. **Study and research guide** — integrate the former learning plan and reading
   reference with the learner connections described below in one main document, such as
   `<course-or-source>学习与研究指南.md`. It explains what to understand, the
   useful source order and depth, exact original-reading selections when that
   mode is intended, and relevant connections to the learner's environment,
   interests, prior understanding, and research. Develop the actual
   mathematical relationships, empirical models, procedures, code behavior or
   engineering decisions needed for understanding, according to the selected
   approach. Do not require an author-objection-response structure merely
   because philosophy uses one. Overall personal priorities and scheduling keep
   their existing learning-path owner.
3. **Exercises and experiments** — one training document, such as
   `<course-or-source>习题与实验.md`, with clearly distinct written-exercise and
   experiment/project parts. The guide links to the relevant practice entrance,
   which links back to the unit and its glossary entries.

Prepare reusable testing and evaluation material across the overall knowledge
structure of the agreed book, course, or topic. When the learner's level and
specific needs are not yet known, retain broad coverage rather than guessing
which few points will matter. This is preparation for later selection, not an
assignment to complete every item. A bounded request still bounds the source
scope; broad preparation does not expand one question into an entire curriculum.

For written practice, link directly to an existing question in the book or course
materials. Give the existing answer or solution its own link when available.
The model may write a checked reference answer and attribute it to the model,
with a direct link back to the identified original question. For experiments or
projects, link the actual laboratory guide, course experiment file, or specific
repository instructions and identify the relevant workspace. The saved practice
file uses existing tasks. Leave a part empty when no matching source task is
available. Explanations, worked examples and counterexamples belong in the main
guide or teaching encounter.

Keep the broad prepared material recoverable in this training document. During
practice, remove most of that coverage from the active working set and retain
only the very small subset substantively necessary for the current question and
observed needs. This reduction is required, not merely an option to shorten an
otherwise comprehensive assignment. Strengthen the retained points with diagrams,
worked examples, counterexamples, and existing supporting exercises for the
remaining difficulties. Preserve links from this adapted selection to the base
material, guide, glossary, and sources; selection need not duplicate the whole
document or delete material useful for a later need. Repair errors in the owning
question or answer. These saved materials should support repeating an item,
changing conditions for another check, or returning after forgetting. Record
actual attempts under the existing Course State contract, without treating an
earlier success as permanent mastery. The teaching-method branch owns how to
use this preparation in the encounter.

Develop the training forms that suit the source and scope. If one form serves
the source, develop it fully. Keep agreed reading-only or no-practice modes
when choosing what to assign.
Actual problem wording, solution checks, presentation, attempts and feedback
follow the teaching-method branch. Code, data, notebooks and execution records
stay in their real workspaces; link them rather than rewriting those artifacts.

## Philosophical study

Develop the selected work's arguments, discussions and grounded research
connections in the guide. The [philosophy branch](philosophy.md#book-materials-and-research-connection)
owns question-led explanation and contextual depth. When preparing a practice
file, develop tasks such as reconstructing an argument, comparing interpretations,
or testing a distinction against a case. Give source passages and grounds for
comparing answers. Keep each work's account distinct and keep progress in
the learner's existing records.

## Relate material to the actual learner

For either kind of main guide, use relevant known purposes, current questions,
interests, existing understanding, and actual environment to decide what needs
explanation and how to make its relations intelligible. Inspect the accessible
source, project, workspace, or current research material when a proposed
connection depends on it. Reuse context already supplied; a complete personal
profile, research plan, or new interview is not a prerequisite. Missing context
limits the personal connection, not the explanation of the subject.

Develop these relations where their concepts and reasons become intelligible.
The environment can supply a real tool, arrangement, activity, or lived problem
that the material helps interpret or change, and whose behavior tests an analogy.
Interests and prior understanding can motivate an entry, suggest a comparison,
or expose a consequential disagreement. Research can give a question to which
the source contributes a method, argument, criticism, or limit. Let these
connections affect the selected scope, examples, depth, and applicable training;
do not append the same relevance statement to every unit or create another
mandatory document. The glossary still grounds terms in their sources.

Preserve the object's independent content and the distinction between the
author's claim, a proposed transfer or analogy, and the learner's experience.
A source can change how the learner understands a purpose, interest, or
environment; it need not merely justify an existing project. Philosophical
understanding can revise a way of seeing oneself or the world without immediate
instrumental use. A concept without a supported personal application remains
worth explaining; do not invent one or infer personal facts from a tool setup.

Use the learner's actual questions, objections, intuitions, and responses to
revise the explanation and its material. When a useful connection becomes
clearer or fails, update its affected passage and examples rather than treating
the initial guide as fixed. This is ordinary situated teaching and material
maintenance; it does not create a separate learner profile or authorize changes
to the environment, research manuscript, or psychological model.

## Research relationships across disciplines

Technical books and courses receive the same attention to research connections
as philosophical sources. Where current research is relevant to a substantial
main guide, inspect the recipient-owned direction and pertinent manuscript,
then explain the meaningful
relationship inside its main flow. An overall orientation can state why the
source matters; develop specific connections after the concepts or content on
which they depend. Research relevance remains substantive rather than a fifth
file, a detached list, or a sentence saying that the source is useful.

Compare the source's actual content and conditions with the current research
question: what corresponds, what differs, what can transfer or must change, and
what proof or evidence remains missing. Distinguish established results,
attributable user judgments and model proposals. A methodological contribution,
criticism or absence of a direct connection is a valid result. Missing research
context limits the claimed connection; do not invent applications or repeat the
same relevance label after every section. An isolated question does not require
a fresh whole-research review.

A source-led learning guide, including its research-relevance account, stays in
course. A report primarily developing the user's research belongs with its
existing manuscript project and may integrate its needed source explanation
there. Choose one owner for the complete main document; a research-relevance
section alone does not require splitting it across vaults. Reuse independent
research comparisons at their existing owners: explain the connection needed
here and link deeper work without maintaining a competing copy.

## Connected presentation and economical maintenance

### Explanatory visuals within the existing documents

Include explanatory visuals inside both the
glossary's detailed entries and the main guide, beyond the opening concept map.
Neither a substantial glossary nor a substantial guide should become only
prose and formulas after treating that map as sufficient visual support.
Add a fitting amount of source-grounded diagrams,
figures, plots or visual comparisons at the places whose relationships they
clarify. Select their number and form from the material, without a per-section
quota or decorative illustrations.

For example, mathematics can use geometry or a changed-condition comparison;
scientific inquiry can show a model, measurement or evidence relationship;
methods can show data transformations or an algorithm's behavior; engineering
can show components, interfaces or feedback; philosophy can show a consequential
distinction, dependency or competing argument. These are possibilities to
adapt, not mandatory illustration templates. A table of contents in boxes or
another copy of the glossary map does not fulfill a different explanatory need.

Place each visual near the passage it supports, explain its meaningful marks,
relations, assumptions and omissions, and keep the prose connected. Reuse a
verified source figure with attribution and appropriate rights, or create a
faithful explanatory diagram; distinguish a schematic from observed data.
Preserve figures and tables needed to understand actual exercise questions and
to interpret experimental results. Preparing visuals does not authorize running
learner experiments or inventing measurements. Embed the visuals and ordinary
assets in the existing documents/corpus; no additional required reading file or
separate visual guide is created. Verify the actual reading-mode result.

In glossary entries, use visuals to recover the object, defining relationship,
essential condition or contrast, such as a projection, a distribution's shape
or an interface relationship. A concise visual explanation and its necessary
caption can accompany a definition without turning it into a worked exercise.
Keep proofs, extended derivations and long case discussions in the main guide.
Choose the location by the visual's actual contribution, not a blanket rule
that all figures belong only in the guide.

### Connected explanation and maintenance

Use coherent problem/section order and transitions in the main document, not
repeated mandatory slots for every unit. Keep the explanation self-contained
at its intended depth; links support checking and deeper lookup rather than
sending the reader away for every central connection. Align named units across
the glossary, guide and practice file. Use a shallow contents list
and direct section/block links instead of forcing the user through indexes.
The guide's progression identifies the relevant training entry and return point
without repeating the training specification.

Reduce duplicated introductions, source routes, generic instructions, unused
templates and repeated research summaries. Preserve load-bearing definitions,
conditions, source evidence, conceptual depth and the two distinct training
forms. Prepare the actual requested scope rather than a full-library curriculum;
do not interpret concision as omitting requested book coverage or necessary
practice. Reuse verified source pools and update materially changed sections
instead of regenerating all documents after a lesson.

During the next substantive revision, integrate existing plans and reading
references into the main guide and written/lab preparation into the technical
training document, preserving the independent glossary. Repair incoming and
internal links and retain unique content, learner notes, original sources and
existing State. Retire superseded duplicate bodies through their existing
history/ownership route after integration is verified. Do not bulk rewrite the
library merely because this default changed or maintain old and new files as
competing authorities. Existing filenames remain valid locators until integrated.
Existing Course State owns evidenced exposure, attempts, unresolved questions
and resumption; do not create per-book progress files or duplicate State.

## Authoring and readback

Verify the course material set and review authored companions as separate
checks. Material-companion verification applies at the course level. It checks
registration and the evidence for the actual availability, location, edition
and scope of required materials. Include adopted books or papers as part of
that course inventory where relevant and record the result for the course.
For a standalone book or paper, register its original and review its own
companion notes. Review checks that the actual note meets the current
requirements for its course or named work and selected scope, including its
content and source links. Record the scope, findings and result of that review
in the catalog when one is maintained. Review status follows the observed
note check.

When Dot is the note writer, the collection maintainer first verifies source
identity, selected scope, and the target file. The maintainer diagnoses mixed
source collections, carries out needed splits, moves, renames and link repairs,
and updates the catalog from verified results. Give Dot the actual original,
selected units, exact target file and the content to create, extend or rewrite.
Dot reports written files, covered scope and unresolved problems. The collection
maintainer then reviews the delivered notes and updates the catalog from
that review.

When preparing or revising a main guide, make the root teaching contract's
two commitments concrete for that course: the learner develops modeling through
selected worthwhile intuitive attempts and feedback, with model support
throughout inquiry, and enters concepts through relevant conflicts or explanatory
tensions. Name useful source-grounded comparisons, counterexamples or prediction
gaps and the intuitive contribution they can develop. Apply the root's recurring
question, candidate, distinguishing-check, and revision relation within the subject;
the teacher may supply candidates and formalize fragmentary intuitions without
requiring a complete construction before help. A learner's chosen formal
contribution can also develop and evidence that modeling; the model continues
to carry needed detail.
Keep these as adaptable entries within the selected progression, not mandatory
paradoxes, a fixed lesson script, or additional reading/exercise obligations.
Retain the general cognitive account with Yinyang; the guide owns its subject-specific
application rather than another psychological portrait. Glossaries continue to
state objective source-grounded meanings. A modeling goal also applies when the
current course deliberately limits practice to concept recognition and reading.

Before materially creating or revising a guide, read the affected material with
the applicable path, existing Global/Course State, resolver and source evidence.
Ordinary explanatory prose does not require the Prompt/Skill authoring lifecycle;
use that owner when actually changing controlling instructions. Read
before and after a permitted write; otherwise retain the exact proposal as
unsaved. Read the actual source edition and chapter structure before glossary
work. Incomplete sources limit coverage rather than licensing invented content.
The final rendering checks below belong to the teacher's own document maintenance
under actual host and Course permissions; they do not authorize learner labs.

## Philosophical book materials

For philosophical text study, [the philosophy branch](philosophy.md#book-materials-and-research-connection)
supplies contextual concept depth and the connected argument/discussion method.
Use the same independent glossary plus main-guide arrangement above. The main
guide develops the book's arguments and current-research connections together;
the glossary restores its conceptual structure and detailed meanings. Apply this
branch's source association, Markdown and saved-result checks to both documents.

## Learner glossary

Prepare and maintain the independent glossary in the recipient's chosen teaching language for substantive study as specified above, repairing gaps in the selected scope before using it. An isolated question can receive definitions directly; this does not waive the glossary for sustained study or requested material preparation. Respect
scope, edition, depth, skips and access. In Web, proactively map terms to
verified passages under the rendering section below, preferring corresponding sources in the recipient's teaching language and
honoring explicit learner exceptions. Verify mappings as
part of authoring rather than deferring them to local repair.

Glossaries support recognition and recovery, teaching connected modeling, and
sources full detail. The model retrieves the needed entry and source connection
when recall is costly; difficulty recalling a name does not establish a gap in
understanding its object. The root teaching contract owns the current example
or visual entry and State owns resumption; neither requires another saved
artifact or an expanded glossary. Each entry conveys defining meaning in
the chosen teaching language, with essential qualifications, original terms, abbreviations
and notation.
Formulas and selected explanatory visuals support the meaning. The
visual-support section applies inside detailed entries as well as to the
opening map. Include compact examples when they establish a distinction or
clarify an application condition. Use extended worked examples and expanded
exposition in lessons or the main guide. Philosophy concept tables use the contextual explanation required
by [the philosophy branch](philosophy.md), including a bounded example or contrast
when it is needed to preserve a concept's meaning. Proofs, proof sketches and
assigned exercises still belong outside the glossary. Use enough prose for
recognition and recovery, without a fixed template or length ceiling.

Put an explicit teaching-language role label before each entry's term so the reader can
recognize what kind of thing it is. The following Chinese profile illustrates the roles: 【定义】, 【概念】,
【记号】, 【方法】 and 【算法】. Mathematics retains 【公理】, 【定理】,
【引理】 and 【推论】, with exact definitions, notation, statement conditions and
conclusions. Within mathematics, group other established formal results as
【定理】 rather than 命题/性质, without inventing source numbers; distinguish
definitions from results and keep proofs in the guide.

For other material, choose a meaningful role from the actual entry, such as
【模型】, 【理论】, 【假说】, 【定律】, 【经验结果】, 【机制】, 【指标】, 【工具】, 【协议】,
【组件】, 【接口】, 【设计约束】, 【论点】 or 【区分】. These are examples,
not a required taxonomy or quota. An empirical regularity is not a mathematical
theorem; an author's claim is not an established fact merely because it has a
label. The role states what the entry contributes, while its explanation
preserves evidential status and qualifications. Mixed subjects can use different
roles entry by entry without assigning every term the subject's name.
Use the optional important-entry callouts supported by the rendering section;
ordinary bold labels need no plugin or new callout type.

Select mathematics from the learner's purpose, prior exposure, paths and
inspected sources, including useful applied objects rigorous texts leave
peripheral. Do not copy a proof syllabus or take a mechanical source intersection
or union. Follow verified chapter and section order; when combining sources,
explain a coherent spine and preserve provenance. Keep visible chapter and
section names and shallow organization; label authorized cross-course bridges.

Use actual folders and resolvers; preserve learner content and useful
explanations unless removal is requested. Keep one discoverable glossary entrypoint
(`术语与名词解释表` in the Chinese profile);
it may link named unit tables grouped under a collapsible folder or headings.
The philosophy branch owns their chronological ordering and complementary maps.
Repair links after renames or removals. Retained handbooks are concept expositions
(`概念详解` in the Chinese profile); essential meanings
and conditions belong in the glossary itself. Update for scope or meaning
changes, errors or recall gaps, not ordinary progress.

## Reading-language companions

When preparing or revising skimming materials, proactively translate selected
passages not readable in the recipient's selected language into that language
through the active teacher; reuse adequate editions or translations. Do not defer this preparation to learner reminders or local models.
Save each language companion beside the relevant source under the
collection's configured source category (`书/` in the Chinese examples), using a recognizable source name and selected range.
Keep the original material unchanged and the skimming reference's reading links
pointing only to that original, with its existing page or section coordinates;
do not add a parallel set of translation links.

The companion identifies its source edition and original page or section
boundaries. Put each original-source link in its corresponding translated
section's heading or immediately beside that section, with the actual page or
section destination. Do not collect these links in a separate top-of-file
source-location index that forces the reader to scroll back and match ranges.
It faithfully translates the selected passages, preserving formulas,
code, examples and necessary figure context, rather than replacing them with a
summary or a new lecture. Check coverage and source correspondence, then follow
the rendering section below for saved-result validation. Report any inaccessible or
unfinished portion. Preparing translations does not establish reading progress
or mastery and does not change Course State.

## Markdown format and rendering

Write model-facing instructions, structured State and schemas in English.
Write learner-facing material and Route prose in the recipient's selected language.
Preserve exact source text, learner records, filenames, paths and machine schemas.

Use UTF-8 Markdown with one title, meaningful headings, normal lists and
tables, code formatting for literals, and links for navigation. Give the learner
the material itself. Include edition, coverage or other document-specific
orientation when useful. Keep course rules with their existing owners.

In Obsidian, use `$...$` for inline mathematics and `$$` on separate lines
for display mathematics, with blank lines and any list indentation the block
needs. Use a supported rendered diagram for the required glossary concept map.
Resolve links against the actual vault and source. Escape the alias separator
as `\|` inside a Markdown table and use `|` elsewhere.

### Maintain source-linked reading notes

Use the glossary's source object to choose meaningful passages. Prefer the
course's continuous lecture notes and then its slides for course entries. Link
a book or paper glossary to the corresponding work. Identify supplementary
sources where they contribute a distinct explanation. Prefer the verified
corresponding passage in the learner's language when available and use that
edition's own coordinates. The
[course entrance method](course-sources-and-entry.md#prepare-a-reachable-learning-entrance)
owns presentation of compiled lecture notes and slide decks in the guide.
Verify migrated page or selection coordinates against the exact changed PDF.

Link the meaningful term or concept cluster in the recipient's language directly to its source.
Keep a secondary-language gloss and mathematical notation beside the link as ordinary
text and math, for example `[[source#anchor|根号尺度]]（$\sqrt{n}$）`. Use an
established acronym or readable plain symbol when it is the useful name.
Consolidate redundant bilingual links, preserving any distinct supporting
passage as its own appropriate concept association.

With a configured [PDF++](https://github.com/RyotaUshio/obsidian-pdf-plus) reader, use
`[[vault/path/source.pdf#page=N&selection=beginItem,beginOffset,endItem,endOffset|concept name]]`.
Use the exact PDF's text-layer indexes and UTF-16 offsets or copy its verified
selection link. Use a verified rectangle for figures or unsuitable text
layers. Keep the vault's default highlight style and return backlinks to the
learner-facing explanation so preview recovers its context. Distinguish a
teacher-developed bridge from a source claim and mark unresolved anchors as
unfinished. When selection is
unavailable, use a verified page link and searchable passage locator, and
report the remaining selection or highlight limit.

For reading windows, use links to the verified start page and show the
one-based PDF range as `第 25 页` or `25–28 页`. The same plain one-based
PDF page convention applies throughout saved learner materials. Convert older
numbering against the actual PDF. For Markdown and Web originals use the
available stable heading, block or section link.

Use compact teaching-language type labels for glossary entries. Where configured,
academic callout styles can emphasize important definitions, axioms,
theorems, lemmas, corollaries, concepts, notation, algorithms and methods.
Keep the type explicit. Keep each result's statement, essential assumptions
and defining meaning in the glossary. Put the argument establishing the result
in the guide. A reusable method can have a glossary entry for its purpose,
applicability and central operation.

### Verify changed materials

Reread the saved change. Use current vault tools for affected Markdown
structure and resolved links. When a change depends on rendered formulas,
diagrams or navigation, inspect the affected study path in the configured
reader, including changed PDF++ highlights and backlink context where used. Check
adjacent content where the change affects interpretation or layout. Repair
observed defects and report any rendering or navigation still unverified.

### References

- [Obsidian advanced formatting, mathematics and diagrams](https://obsidian.md/help/advanced-syntax)
- [Obsidian internal links](https://obsidian.md/help/links)
- [Obsidian Linter rules](https://github.com/platers/obsidian-linter/blob/master/docs/rules.md)
