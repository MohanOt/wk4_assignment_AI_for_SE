# Part 1 — Theoretical Analysis (30%)
# Q1 — How AI-driven code generation tools reduce development time; limitations

Answer:
AI-driven code completion (e.g., GitHub Copilot) reduces development time by:

Auto-completing boilerplate (CRUD handlers, config, tests) so developers don’t type repetitive patterns.

Providing contextual suggestions based on surrounding code and comments, accelerating implementation and prototyping.

Speeding up learning by showing idiomatic usage patterns and library calls.

Generating tests and documentation snippets, reducing time spent on ancillary tasks.

Limitations:

Context errors: suggestions may not match project-specific invariants, leading to subtle bugs if accepted uncritically.

Security risk: suggested code may include insecure patterns (e.g., unsanitized inputs).

Over-reliance / loss of craft: developers might accept code without understanding it.

Licensing issues: suggested code could resemble copyrighted content.

Limited long-term design: LLMs are best at short snippets, less effective at architectural decisions.

# Q2 — Compare supervised vs unsupervised learning for automated bug detection

Supervised learning:

Uses labeled examples (bug/no-bug, bug severity).

Good when you have historical issue labels (bug/feature, severity).

Models (e.g., logistic regression, random forest, transformer classifiers) can predict bug likelihood and prioritize triage.

Pros: Clear evaluation (accuracy, F1), actionable predictions.

Cons: Requires labeled data; labels may be noisy.

Unsupervised learning:

Uses unlabeled data to find anomalies or clusters (e.g., outlier code changes, unusual metrics).

Useful for novel bug detection or discovering unknown failure modes (e.g., cluster commits that later correlate with failures).

Pros: No labels required; finds unexpected patterns.

Cons: Harder to interpret; needs human validation.

In practice: combine both — unsupervised anomaly detection for novel issues, supervised models for triage when labeled history exists.

# Q3 — Why bias mitigation is critical for UX personalization

Answer:
Personalization affects what content and features users see. If training data under-represents groups, personalization can:

Reinforce stereotypes (e.g., showing lower-quality suggestions to some groups).

Create unequal experiences (reduced discoverability, accessibility).

Produce feedback loops where certain groups are ignored, further skewing data.

Bias mitigation ensures fair exposure, equitable performance, and compliance with legal/ethical standards. Techniques (reweighing, fairness-aware training, A/B testing with fairness metrics) reduce harmful outcomes and maintain user trust.

# Case Study: AI in DevOps — Automating Deployment Pipelines

Question: How does AIOps improve deployment efficiency? Provide two examples.

Answer:
AIOps improves deployment efficiency by automating routine decisions, predicting issues before they occur, and accelerating incident response.

Example 1 — Predictive rollback & canary promotion:
AIOps can analyze historical deployment telemetry and automatically promote canary releases or rollback when predictive models detect an increased probability of failure (based on metrics drift), reducing manual monitoring and time-to-recover.

Example 2 — Automated root-cause triage & alert prioritization:
By correlating logs, traces, and metrics, AIOps can surface the most probable root cause and prioritize alerts. This reduces noisy alerts and helps engineers focus on the highest-impact issues, shortening mean time to resolution (MTTR).