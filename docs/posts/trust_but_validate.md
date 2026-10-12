---
authors:
  - jamescbury
date:
  created: 2026-10-12
draft: false
categories:
  - Agentic AI Research
tags:
  - governance
  - regulated industries
  - gamp
  - agentic applications
  - trust
  - pyrana
comments: true
---

# Trust, but Validate

In my formative years working in audit and risk at EY, mostly within life sciences companies, I never once asked a client whether they trusted their ERP system. It would have been a strange question. Nobody trusts an ERP (people have feelings about their ERP, but trust is rarely one of them). What we asked was whether the system was controlled - or, if it was a GxP system, whether it was validated - it was the standard stuff: who had access to what, whether the audit trail was switched on, and what happened the last time something went wrong.

<!-- more -->

!!! pyrana "About us"
    Zeroth Technology builds [Pyrana](https://pyrana.ai/), a governance layer for agentic AI.  This post was also published on the [Pyrana blog](https://pyrana.ai/resources/trust-but-validate).

So it has been a little odd to spend the last two years listening to smart people ask "Can we trust AI?" as if trust were something easy to define, that you just had or you didn't.

## Trust is a deliverable

In a regulated environment, trust is something you build over time - through testing, control and reputation. You might start with an inclination to trust or distrust a system, but you always had to prove it.

FDA's rule on electronic records has said so since 1997.[^1] Section 11.10 of 21 CFR Part 11 lists the controls a system needs before its records can be relied on: validation, access limited to authorized individuals, authority checks, and a secure, time-stamped audit trail. These are all things you can check to decide if you are going to trust a system or not.

I have been fortunate to contribute to ISPE's GAMP guidance over the years, and one of my biggest takeaways is to never underestimate the importance of critical thinking - and to ask what a system is for before you ask whether it works. Back in 2020, Sion Wyn and I wrote a piece for Pharmaceutical Engineering on applying that thinking to robotic process automation.[^4] The bots were a lot dumber then, but the questions were the same.

## Eight Components of System Trust

There are many frameworks and methods out there, but in my experience, there are eight basic things you need to know before you rely on an actor, a process, a system, or a decision. I did not invent these, and there are several ways to refer to each of them. The right column is what each one turns into when the "actor" is an agent.

| Component | To trust any person, process, system or decision, we need to know... | Translated for agentic AI |
| --- | --- | --- |
| Purpose | What is it intended to do? | Clear input and output requirements |
| Authority | Is it allowed to do it? | Role-based permissions, approved tools, policy gates |
| Competence | Can it do it reliably? | Validation, benchmarked performance, task-specific testing |
| Control | Is it operating within defined boundaries? | Guardrails, deterministic workflow constraints, exception handling |
| Transparency | Can we understand what happened? | Execution logs, a step-by-step trace, source attribution |
| Traceability | Can we reconstruct the evidence trail? | Versioned prompts, models, data, tools, context, and decisions |
| Accountability | Who is responsible for the outcome? | Human-in-the-loop approval, named ownership, track record and reputation |
| Oversight | How are errors detected, reviewed, and corrected? | Monitoring, drift and error detection, CAPA and change control |

Designing and implementing all of this establishes a foundation for trust, but the trust is actually established when you have a track record of doing all the above consistently over time. If there are deviations (there always are) they are observable and explainable.

FDA is already pointing the same way for AI. Its January 2025 draft guidance on using AI to support regulatory decisions is built around a defined context of use and a risk-based view of credibility,[^2] and its September 2025 guidance on computer software assurance takes a risk-based approach to the software a quality system depends on.[^3] I read both as the agency saying what it has always said... show me the control, and the evidence it was effective.

## An agent cannot hold these. An application can.

Here is where most agent projects go sideways. Teams take that list and try to make the agent satisfy it, usually by writing a longer prompt.

Take purpose, authority, and accountability. An agent on its own has no purpose beyond whatever the last prompt asked for. Its authority is whatever tools and credentials somebody handed it, and its limits are instructions it may or may not follow. And accountability is a bit of a grey area - the model providers are pretty quick with disclaimers that push it back onto the user (go ask Claude a legal question), so it lands on whoever wrote the prompt. That's fine for a vibe-coded agent one person built for themselves, but it gets messy fast once that agent is rolled out to an organization.

An agentic application is a different animal. It is a governed process with an agent inside it. People and agents work on the same task under the same roles, the same permissions, and the same record. The application defines the job. It checks every operation against the caller's role before the operation runs. It knows who requested the work, who reviewed it, and who owns the outcome. The agent does part of the work, and it is a participant like any other.

That is the whole reason an application is easier to trust than an agent. Purpose, authority, and accountability are built into the process, where you can inspect them and test them, rather than resting on how a model happens to behave on a Tuesday. And the application doesn't assume that just because I can run a prompt that you wrote, you and I have the same authority.

## Controls are not parameters to be tweaked at run time

Control and transparency work the same way. In Pyrana we built them to live in four distinct layers.

Orchestration runs the process as a fixed sequence of steps and decides when the agent is called and when a person is. The harness runs the model for one step, supplies its instructions and context, caps what it may do, and handles failures. A skill is a method for a kind of work, and it grants no access. A tool is the only way the agent touches a system - every call is checked before it runs, and it is bound by contracts.

Each of those layers writes to the log. None of them can be talked out of its job by a clever prompt, which is more than I can say for most of us. My colleague Sam Merkovitz covers the harness in detail in [Enterprise AI? It's all about the harness](https://pyrana.ai/resources/enterprise-ai-its-all-about-the-harness).

## Competence comes from what you give it

A model does not show up knowing your procedures, any more than a new hire does. I have written before that you [should not train your model to be an expert](https://zeroth-tech.github.io/blogs/2025/12/01/dont-train-your-model-to-be-an-expert/). You give it the knowledge, and you manage that knowledge the way a quality system manages controlled documents: versioned, owned, access-controlled, cited at the exact clause - and with provenance, so that as the knowledge evolves each new version references the one it replaces and the chain back through prior versions is explicit.

We have a small demonstration of why this matters, built on a synthetic inspection report. The task is to propose redactions under a five-rule procedure. One sentence mentions a fictitious lab technician named Amy Hamilton who is running a procedure using a Hamilton syringe pump. In the first run the agent redacts "Amy" and leaves "Hamilton" sitting there, because it read the surname as the equipment brand. In the second run (same model, same document) we add a rule about names that look like equipment, as a versioned Context Unit. This time the agent proposes the full name, flags it at 0.62 confidence, sends it to a person, and cites the rule it relied on.

The model did not get smarter between runs. It got better instructions, and it left a trail. That is competence and traceability in one example, and neither came from the model.

Competence still has to be shown, of course. You test the agent on representative cases before you rely on it, and again whenever the knowledge or the model changes. But it also builds with use - each time the agent asks a similar question and gets a confirmation, its confidence goes up, until eventually the human-in-the-loop control for that kind of decision is no longer needed.

## Oversight is CAPA with better record keeping

Oversight is the component that keeps the others true over time, and for agentic work it has a familiar shape. A reviewer finds a miss. The finding becomes a proposed change to the shared knowledge. The owner of that knowledge approves it. A new version is issued, and the original run keeps citing the version it actually used. The next run, by a person or an agent, starts from the corrected basis.

If that sounds like corrective and preventive action with change control, it should. It is the same loop, and the agent's work improves the same way a regulated process does. I made the longer argument for knowledge that [gets stronger from being wrong](https://zeroth-tech.github.io/blogs/2026/04/30/knowledge-that-gets-stronger-from-being-wrong/) earlier this year.

## How we do this in Pyrana

Pyrana is built to make these eight components properties of the platform. Identity and role-based authorization are checked on every operation. Approval policies hold consequential actions for a named person. Context Units are versioned, owned, and cited. Every run leaves a record of who acted, under what authority, on which inputs, through which steps.

But those are just table stakes. The part we are still building is the evidence for competence over time: systematic evaluation across representative cases and monitoring for drift. Per-run checks and flagged uncertainty exist today, but the longer loop of self-improving knowledge will take time to prove out.

## Before you roll your agent out to your enterprise...

 Ask yourself these questions:

1. What is it for, and where is that written down?
 
2. What is it allowed to do, and what enforces that?
 
3. How do you know it does the job reliably?
 
4. What stops it when it goes outside its limits?
 
5. Can you see what it did, step by step?
 
6. Can you say which version of which rule, data, and model produced a given result?
 
7. Who answers for the outcome?
 
8. When it gets something wrong, what changes, and who approves the change?
 

If you are stuck on these questions, the missing piece is likely the application around the agent.

Asking whether we can trust AI gets us an argument. Asking whether we can govern agentic work to the same standard we already govern regulated work gets us a design plan.

---

[^1]: U.S. Food and Drug Administration, 21 CFR Part 11, Electronic Records; Electronic Signatures, §11.10 Controls for closed systems. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11

[^2]: U.S. Food and Drug Administration, "Considerations for the Use of Artificial Intelligence To Support Regulatory Decision-Making for Drug and Biological Products," draft guidance, notice of availability January 7, 2025. https://www.federalregister.gov/documents/2025/01/07/2024-31542/considerations-for-the-use-of-artificial-intelligence-to-support-regulatory-decision-making-for-drug

[^3]: U.S. Food and Drug Administration, "Computer Software Assurance for Production and Quality System Software," guidance, notice of availability September 24, 2025. https://www.federalregister.gov/documents/2025/09/24/2025-18468/computer-software-assurance-for-production-and-quality-system-software-guidance-for-industry-and

[^4]: Sion Wyn and James Canterbury, "A GAMP Approach to Robotic Process Automation," Pharmaceutical Engineering, May/June 2020. https://ispe.org/pharmaceutical-engineering/gamp-approach-robotic-process-automation
