# Yinyang

Yinyang is a form of personal recursive self-improvement (RSI): improving a piece of work can also improve the method that produced it. This repository pairs a book about that practice with **22 individually installable Skills** for research, learning, environment design, and device use.

<!-- reading-cover:start -->
## Choosing how to read and use the collection

This collection explores a method of personal recursive self-improvement. A language model draws on a selection of personally appealing philosophies and views, together with personal material, to develop a model of the person. That model can guide changes to tools and collaboration. What happens in practice gives grounds for revising the model and improving the method.

The [Core views](docx/references/docs/core-views.md) offer a starting point. A few views of interest can be followed into the corresponding essays, where their reasons and examples invite comparison with views already held. Some may be worth keeping. Other works may offer further views worth seeking out.

Here, **personal philosophy means articles that express personal views**. Existing articles can be used directly. Developing scattered thoughts into new essays is a matter of interest in writing. Exploring and adopting views can be worthwhile in its own right.

When the aim is practical use, the selected philosophies and views can be brought together with personal material to form a model of the person. This is one of [six working accounts](docx/references/formation/overview.md). The others describe orientation, the model as counterpart, the working relationship, the practical environment, and the revision method. The selected views and six accounts can guide software and tool configuration through a language model’s global prompt and be revised through use. See the [Practice guide](docx/references/docs/creation-method.md).

<!-- reading-cover:end -->

<table>
<thead><tr><th width="480" align="left">Purpose</th><th width="480" align="left">Start here</th></tr></thead>
<tbody>
<tr><td>Read online</td><td><a href="https://boluopai.net/yinyang/en/">Essays</a> · <a href="https://boluopai.net/repositories/prometheus/en/">Appendices</a> · <a href="https://boluopai.net/yinyang/resources/en/">Resources &amp; Advice</a></td></tr>
<tr><td>Download the illustrated book</td><td><a href="docx/yinyang.zh-CN.pdf?raw=1">Chinese PDF</a> · <a href="docx/yinyang.en.pdf?raw=1">English PDF</a></td></tr>
<tr><td>Repository</td><td><a href="#skills-in-the-collection">Skill catalog</a> · <a href="README.md">简体中文</a></td></tr>
</tbody>
</table>

## Questions the book explores

<table>
<thead><tr><th width="480" align="left">Question</th><th width="480" align="left">Essay</th></tr></thead>
<tbody>
<tr><td>Which conclusions hold when the evidence conflicts?</td><td><a href="docx/references/docs/inconsistency-tolerant-semantics.md">Inconsistency-tolerant semantics</a></td></tr>
<tr><td>How can a model help me test an intuition?</td><td><a href="docx/references/docs/yinyang-and-taiji.md">Yinyang and Taiji</a></td></tr>
<tr><td>How do a work, a counterpart, and tools sustain an activity?</td><td><a href="docx/references/docs/writing-a-sinthome.md">From personal models to a sinthome</a></td></tr>
<tr><td>How can one revision improve the next?</td><td><a href="docx/references/docs/literary-recursive-improvement.md">Writing recursive improvement through literature</a></td></tr>
<tr><td>Which abilities are worth practising, and which work can I delegate?</td><td><a href="docx/references/docs/economic-personal-rsi.md">Economic reality</a> · <a href="docx/references/docs/cognitive-complexity.md">Cognitive complexity</a></td></tr>
</tbody>
</table>

The book brings philosophy, psychology, and engineering to bear on the same activity: what a person wants to do, how they take part, and what conditions let them continue. The author uses imagery from several traditions and writes about relationships from a heterosexual perspective. Readers can contribute other experiences and sources through Issues.

<!-- repository-only:start -->
## Intended use and mental health

Yinyang's philosophical ideas guide the configuration of a personal environment for cooperation with models: working arrangements, instructions, and tools. Personal understanding can inform that configuration; the philosophy does not supply a method for revising psychological material.

Yinyang must not be used for psychological self-help work, self-diagnosis, mental-health assessment, or treatment. It has not been systematically evaluated for those purposes. When professional assessment or care is needed, seek a qualified professional; the project's texts and model outputs do not replace that service. The work, models, and circumstances change, so a personal experience or version history does not establish a general psychological effect.

The separate [Psychology guide](docx/references/docs/psychological-support.md) explains model-assisted organization of personal material, questionnaires, scoring, statistics, and practical support within their own evidence and professional-care limits. It does not derive psychological exercises from the philosophy or make the working accounts a self-analysis program.
<!-- repository-only:end -->

## Skills in the collection

Start with **yinyang-empty** if you want to build a personal edition of the method. It supplies writing guides and a structure for your own material. Choose the other packages according to the task. Each package guide lists the tools and companion Skills it needs. For example, to check a claim in a recorded lecture, use **video-subtitle** to locate the passage and **paper-retrieval** to find the paper it cites.

<!-- repository-only:start -->
### Install a package in Codex

Add the marketplace once, then install the package you want. For Empty:

```sh
codex plugin marketplace add boluopai-net/Yinyang
codex plugin add yinyang-empty@boluopai
```

Start a new chat after installation. Substitute another package name in the second command to install it. For local teaching, install both **local-teacher** and **web-teacher**. Device access, external services, and credentials are configured separately. Keep personal material outside the plugin cache. [Installation and updates](docs/codex.md)
<!-- repository-only:end -->

### Develop personal methods

<table>
<thead><tr><th width="300" align="left">Package guide</th><th width="660" align="left">When to use it</th></tr></thead>
<tbody>
<tr><td><a href="skills/yinyang-empty/README.md">yinyang-empty</a></td><td>Develop six working accounts from materials you choose and keep your personal edition privately.</td></tr>
<tr><td><a href="skills/personal-environment-design/README.md">personal-environment-design</a></td><td>Start from an activity and connect the software, tools, and interactions it needs.</td></tr>
<tr><td><a href="skills/task-inquiry/README.md">task-inquiry</a></td><td>When a request has competing interpretations, identify the difference that would change the next step and ask about it.</td></tr>
<tr><td><a href="skills/prompt-and-skill-lifecycle/README.md">prompt-and-skill-lifecycle</a></td><td>Connect instruction meaning, ownership, delivery, and evidence of use when authoring, auditing, and maintaining Prompts and Skills.</td></tr>
<tr><td><a href="skills/prompt-audit-orchestration/README.md">prompt-audit-orchestration</a></td><td>Audit instructions and execution relationships across learning, work, Web, and automation within the requested scope.</td></tr>
</tbody>
</table>

### Research, learning, and practice

<table>
<thead><tr><th width="300" align="left">Package guide</th><th width="660" align="left">When to use it</th></tr></thead>
<tbody>
<tr><td><a href="skills/research/README.md">research</a></td><td>Compare documentation, observations, and counterexamples to see which option the evidence supports.</td></tr>
<tr><td><a href="skills/paper-retrieval/README.md">paper-retrieval</a></td><td>Reconcile bibliography, editions, and full text to deliver verifiable scholarly material.</td></tr>
<tr><td><a href="skills/video-subtitle/README.md">video-subtitle</a></td><td>Retrieve source-linked, timed spoken text and check it against the original video.</td></tr>
<tr><td><a href="skills/web-teacher/README.md">web-teacher</a></td><td>Provide shared methods for course material, teaching, learning paths, and learning spaces.</td></tr>
<tr><td><a href="skills/local-teacher/README.md">local-teacher</a></td><td>Explain, review, and practice in a local environment, developing understanding through real work.</td></tr>
<tr><td><a href="skills/singing/README.md">singing</a></td><td>Prepare accompaniment, recordings, and reference performances for evidence-based singing practice.</td></tr>
</tbody>
</table>

### Coordinate models and browsers

<table>
<thead><tr><th width="300" align="left">Package guide</th><th width="660" align="left">When to use it</th></tr></thead>
<tbody>
<tr><td><a href="skills/agent-orchestration-master/README.md">agent-orchestration-master</a></td><td>Divide independent work among models, define the handoffs, and integrate the results.</td></tr>
<tr><td><a href="skills/model-conversation-relay/README.md">model-conversation-relay</a></td><td>Resume a specified model conversation, confirm the last result, and continue the exchange.</td></tr>
<tr><td><a href="skills/browser-relay/README.md">browser-relay</a></td><td>Manage task-owned browsers, authenticated sessions, target ownership, and cleanup.</td></tr>
<tr><td><a href="skills/model-upgrade-check/README.md">model-upgrade-check</a></td><td>Reconcile available models, purpose-specific selections, and actual consumers.</td></tr>
</tbody>
</table>

### Devices and everyday tasks

<table>
<thead><tr><th width="300" align="left">Package guide</th><th width="660" align="left">When to use it</th></tr></thead>
<tbody>
<tr><td><a href="skills/android-control/README.md">android-control</a></td><td>Operate your Android device through ADB and native interfaces, verifying actual effects.</td></tr>
<tr><td><a href="skills/chezmoi/README.md">chezmoi</a></td><td>Capture host settings in their source files and verify the applied configuration.</td></tr>
<tr><td><a href="skills/obsidian-sync/README.md">obsidian-sync</a></td><td>Maintain shared configuration, cloud copies, and synchronization across Obsidian vaults.</td></tr>
<tr><td><a href="skills/network/README.md">network</a></td><td>Diagnose DNS, proxies, website connectivity, and routing from host evidence.</td></tr>
<tr><td><a href="skills/clash-auto-switch/README.md">clash-auto-switch</a></td><td>Maintain Clash node selection, regional fallback, and DNS/TUN protection.</td></tr>
<tr><td><a href="skills/shopping/README.md">shopping</a></td><td>Compare products, prices, offers, and secondhand choices with inspectable evidence and conditions.</td></tr>
<tr><td><a href="skills/random-wheel/SKILL.md">random-wheel</a></td><td>Turn screenshot choices or named options into a speed-adjustable animated wheel with equal-probability random selection.</td></tr>
</tbody>
</table>

## Feedback and license

Bring corrections, suggested technologies, and questions to [Issues](https://github.com/boluopai-net/Yinyang/issues). Publish your own work independently. The project accepts feedback through Issues and does not accept pull requests. [Contribution guide](CONTRIBUTING.md)

Original material in the writings and the Empty package is covered by the [Yinyang Personal and Internal Use License](LICENSE). You may use and modify the material privately, including to assist paid work. Redistribution or offering it to others as a product or service requires separate permission. The other Skill packages use MIT. See [collection licensing](LICENSING.md) for infrastructure and third-party materials.
