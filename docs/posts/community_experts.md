---
authors:
  - jamescbury
date:
  created: 2025-12-01
  updated: 2025-12-01
draft: false
categories:
  - Agentic AI Research
tags:
  - content-addressable
  - context-units
  - distributed-systems
  - knowledge-management
comments: true
---

# Don't Train Your Model to be an Expert

Real experts mess up sometimes, admit it, and learn faster the next round. If someone never changes their mind, I assume they stopped paying attention.

Many teams still pitch the same idea: "Grab the latest base model, fine-tune it on our data, and boom—we have an expert." The second you do that, the model stops being current, and worse, it freezes your thinking. Knowledge keeps moving; your model should too.

<!-- more -->

What I learned yesterday is only the starting line for today. Humans get to make leaps, use gut checks, and adjust on the spot. Models make guesses from patterns and need huge compute time to shift. I am not saying people are better; we are just more flexible. And when humans learn our intuition is wrong it doesn't take 10,000 GPU hours to retrain our brains

Large language models are amazing generalists. They can talk about almost anything, like the liberal arts major who reads everything. But when the topic is a regulated pharma process or a finance audit, "good general knowledge" runs out of runway fast.

You *could* send that liberal arts major to business school (aka fine-tune the model). But what happens when an even better graduate joins a month later? Do you pay for school twice? Not if I'm the one paying the bill.

Enter the **CxU Set** (Context Universe).

## The Problem with "The Smart Generalist"

Think about how you onboard a senior engineer. You do not teach them to code, they're supposed to already know that. You teach your stack, your history, your weird edge cases, and all your specific ways of breaking things.

Without a good memory layer, using an LLM is like hiring a genius consultant and making them reread your entire documentation library from scratch every single time they can answer a question.

In the current state of things, you probably:

> Write a prompt the length of a novel.
> Paste in a mess of PDF content.
> Hope the model understands your internal acronyms.
> Repeat this Groundhog Day experience for every new session.

There has to be a better way. (And in my experience, usually the "better way" is just an old way applied to new tech).

## What is a CxU Set? (In Plain English)

Technically, a CxU set is a domain-specific context universe of individual CxUs packaged as a reusable "expert session wrapper," and identified by the merkle root of the CxU set.

Other posts explain single CxUs, so let’s zoom out here. COnsider a CxU Set to be version-controlled knowledge that grows as people use it. It is a community expert made of:

- **CxUs:** Single claims you accept as true right now.
- **Vocabulary:** Shared definitions for domain specific or custom words, including Out-of-Vocabulary (OOV) terms for your base model.
- **Memory:** Notes from past sessions, if you allow it.
- **Constraints:** Guardrails like laws and policies, packaged as CxUs.

!!! Note "Scenario: The Aerospace Deep Dive"
    A space company asks: “Walk through the failure analysis for delamination in spacecraft structures.”

    Without a CxU Set you get a bland note about glue. With the set, the system notices the aerospace signal. It adds the right terms (“mode II fracture toughness”), the SOPs, and the past risk logs.

    The answer now sounds like your favorite veteran engineer. Yes, you could stuff all of that into RAG by hand, but nobody wants to write the same mega-prompt ten times a day.

## It’s Not Static; It’s a Community

Here is the fun part: a CxU Set is a living thing, not a dusty PDF.

Picture your LLM saying, “Correct me if I’m wrong. If I missed something, teach me and I’ll lock it in.” When we correct the set, we file a CxU Improvement Proposal (CxUIP). Sound familiar? It’s similar to open-source governance (think Ethereum Improvement Proposals) pointed at company knowledge. *This does not require fine-tuning the model.*

1) User corrects the CXU. ("Actually in practice we set the temperature to 212℉ not 210℉.")
2) Proposal is created. (“Contrary to the documentation the actual temperature should be set to 212℉ so that it boils”)
3) Governance reviews it. (“All in favor…”)
4) CxU is versioned. (“Our latest collective thinking is that… we changed our mind on…”)

We aren't updating the core model—we are updating the expert wrapper. This allows the "expert" to grow through collective wisdom, not opaque, black-box updates.

## Privacy Matters

To be clear, I am not saying we dump trade secrets into a public pool. You can keep CxUs private, you can make paid experts, or you can mix both (that might be a future post).

## We Have to Be Realistic About Scoping

- Company-Scoped CxUs: These live inside your firewall. They learn from your team, keep your secrets, and never talk to strangers.
- Industry-Scoped CxUs: These are the shared experts based on industry knowledge or sourced from industry groups. They track aggregated metrics—like which reasoning patterns work best—without evolving from your prompts (unless you want them to).

We can rank which CxUs win based on helpful votes. We share the signal, not the private data. When someone files a fix, they decide what to reveal.

## Why This Architecture Matters

The key idea is **decoupling**.

The CxU layer is the driver; the base model is the engine. Today you may run your compliance CxU on GPT-4. Tomorrow you may swap in a cheaper open model for FAQs or a math-heavy model for audits. Over time, certain engines will pair better with certain experts, and CxU Sets can even grade which model handles a topic best.

You can change the engine without retraining the driver.

## What This Means For You

Stop expecting AI models to be perfect from day one. Real expertise is messy, shared, and always changing.

If you run technology, stop asking, “How do we train our model?” Start asking, “How do we capture and govern our context?”

Curate your CxUs. Build private and community experts. Version control your shared knowledge. Let the generalist models do what they do best—sound confident—while your context tells them what to say with purpose.

<!-- BLOG_GIT_METADATA START -->
No Git history available for this post.
<!-- BLOG_GIT_METADATA END -->

