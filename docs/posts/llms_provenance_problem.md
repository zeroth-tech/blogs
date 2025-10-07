---
authors:
  - jamescbury
date:
  created: 2025-08-01
draft: false
categories:
  - Agentic AI Research
tags:
  - ai research
  - context engineering
  - llm
  - enterprise ai
  - provenance
comments: true
---

# LLMs Don’t Have a Memory Problem — They Have a Provenance Problem

*The 2025 **Context Engineering Survey**, which reviewed more than 200 research papers and enterprise pilots, cautions: **“Simply enlarging an LLM’s context window does not guarantee reliable attribution or auditability; we still need explanation systems, audit mechanisms, and governance structures.”** ([Context Engineering Survey 2025 §4](https://arxiv.org/html/2507.13334v1)). Put differently, the problem isn’t raw memory capacity — it’s the provenance of the information we cram inside.*  This is exactly the rationale we followed when designing Context Units for our Pyrana platform.

<!-- more -->

## The New Field of Context Engineering (and What’s Missing)

Reviewing the survey hardened my stance that there are 'those building the models' and 'those using the models'.  for the past year or two the *users* were focused on prompt engineering - how do we ask a model to do something in a way that gets the results I want.  We quickly realized that this is not a one-shot experience and users began iterating with the model, engaging with it (or arguing with it as my colleagues and I like to say) and this little back and forth started to max out the context window pretty quick.  So the *builders* came up with novel ways (mostly short cuts) to cram more content into the context window - hence the term *context engineering*.  These efforts include developing longer context windows, external memory buffers, structured prompts, retrieval augmentation — the list goes on. The current thinking is simple: feed our models more information so they **remember** more. Advanced **Memory Systems** now let LLMs retain persistent information across chats, transforming them from stateless bots into agents with (simulated) long‑term memory. And yes, these systems can be impressive — they page knowledge in and out of an LLM much like a computer’s virtual memory, helping the model carry over facts from one query to the next.

So, more memory should solve everything, right? Not exactly. The survey uncovered a stubborn gap: even as we stuff models with more context, they struggle to **generate** equally sophisticated long outputs. In other words, cramming more into an LLM’s head doesn’t guarantee it can *use* that knowledge effectively. And from a practical perspective, simply increasing the raw amount of context has diminishing returns. **Why?** Because the real world isn’t just about hoarding facts; it’s about trusting them.  

In an enterprise setting, it’s not enough for an AI to recall a policy document from six months ago — we need to know *which* version of the policy it used, who approved that content, and whether the model’s answer can be traced back to a reliable source. **That’s provenance.**

If you’ve ever debugged an AI’s output and wished you could see an itemized receipt of *“here’s exactly what I was fed and where it came from,”* you’re feeling the provenance problem. Sure, memory bandwidth is great, but if an AI’s “memories” are a jumbled scrapbook with no labels, we’re just moving the mess from one place to another.

The missing piece in this context engineering is **governance**. How do we **control** and **track** what goes into these ever‑expanding context windows? The 2025 survey authors stress the need for “explanation systems, audit mechanisms, and governance structures” to keep our context engineering on the rails. In plain terms: we don’t just need bigger memory; we need better memory **management**. Enter **Context Units (CxUs)**.

## Context Units: Packaging Knowledge with Provenance

I’ve written before about Context Units (CxUs) as the “atomic fact cards” of a knowledge base. Think of a CxU as a bite‑sized, immutable packet that captures exactly one idea or fact you care about — plus the evidence and metadata that back it up. Each CxU is self‑contained (claim and context travel together) and **hash‑addressed**, meaning its unique ID is a cryptographic hash of its content. Why go to those lengths? Because it gives each unit a stable identity and tamper‑evidence. If anyone changes a CxU’s content by even one character, its hash (and ID) changes too. No silent edits, no sneaky tweaks. In other words, *truth comes with a checksum*.

Each CxU carries metadata about its origin and status: who created it, when, what version, and even links to source documents or other CxUs it builds on. This built‑in provenance means you don’t just have a blob of text; you have a **verifiable, structured packet of knowledge** with an audit trail. It’s like the difference between a paragraph on a blog site versus a notarized fact on an index card — one is just text, the other is text with a certificate attached. (except for our blog site since we retain a git commit for every post...)

**Concrete example**  
Suppose we have a regulatory guideline: *“In the EU, a shipped product must include a Declaration of Conformity before customs clearance.”* In a CxU form, this would be stored as:

* **Claim:** “In the EU, a shipped product must include a Declaration of Conformity before customs clearance.”  
* **Supporting Context:** “Defined in EU Regulation 765/2008, Article 30, to ensure product safety and compliance.”  
* **References:** [EUR‑Lex 765/2008 Article 30](https://eur-lex.europa.eu/eli/reg/2008/765/oj).  
* **Metadata:** tagged as `regulation`, `EU`, `compliance`, with a version number and timestamp.

Because this CxU is hashed and immutable, if the EU updates their regulation next year, that update becomes a *new* CxU with a different ID (and a pointer back to the prior version). The old fact doesn’t silently morph; it’s versioned like code in Git. We can always trace which version of the rule was applied in any AI interaction. Over time you get a **version chain** – essentially a linked list of how that fact evolved. If an AI answer was based on the 2024 rule and not the 2025 amendment, you’ll know, and you can decide if that’s a problem. This is **context governance** in action.

Crucially, CxUs also let us compress knowledge *without losing trust*. A 3 000‑word policy document might boil down to, say, ten well‑crafted CxUs capturing its key points. You’ve just shrunk the context by an order of magnitude, but each CxU still carries a link back to the relevant source text. You gain **knowledge density** (more signal per token) without sacrificing provenance. The model’s prompt stays focused and efficient, and you maintain an audit trail for every snippet of info included. *More context* isn’t always better; **better‑curated context** is better.

> CxUs aren’t a silver bullet. They’re a design tool — a discipline that enforces trustable context.

### The CxU Workflow in Pyrana

1. **Author / Extract** → draft CxUs from docs, meetings, or code.  
2. **Validate** → schema + rule checks (e.g., conflict detection, required fields).  
3. **Store** → content‑addressable, deduplicated, immutable.  
4. **Retrieve** → query by tags, semantic similarity, or explicit IDs.  
5. **Pack** → inject selected CxUs (or just their claims+IDs) into the LLM prompt.  
6. **Audit** → log every `cxu_id` used so you can reconstruct the chain of thought.

Every step is deterministic and inspectable — a far cry from dumping a PDF into a prompt and hoping the model pays attention to the right parts.

## From Lab to Enterprise: CxUs in Action

Let’s make this concrete. Imagine an AI assistant for supply‑chain compliance. Instead of stuffing it with every regulation PDF, we curate a **library of compliance CxUs** up front. When a user asks, *“Can I ship this product to Germany?”*, our retrieval picks five or six relevant CxUs — the EU declaration rule, a German customs clause, and an internal carrier policy. Those units go into the prompt, and the model replies with an answer that cites them:

> “Yes, you can ship to Germany, but you must include a Declaration of Conformity per EU Regulation 765/2008 Article 30 and use a certified carrier per Internal Policy XYZ.”

Because we logged the CxU IDs, a compliance officer can audit exactly which facts were used. The model isn’t just spouting off — it’s effectively **citing its chain of thought**.

This scale‑up beautifully in agent‑oriented architectures. Multiple agents can pass CxUs (or references) instead of free‑form text, preserving traceability across a complex workflow. Think of it as **end‑to‑end provenance plumbing** for AI.

## Implications and Open Questions for Researchers

*Is this really new?*  
In one sense, no — we’re merging ideas from knowledge graphs, content‑addressable storage, and version control. But the integration is timely. It answers the survey’s call for **explanation systems and audit mechanisms** in context engineering.

**Research frontiers**

* **Memory Architectures:** Can long‑term LLM memories store *provenance‑rich* items (CxUs or indices) rather than fuzzy text blobs?  
* **Selective Forgetting:** With provenance metadata, an agent could decide what to keep or purge intelligently.  
* **Standardization:** Could we define a cross‑org CxU schema so companies share knowledge like open‑source libraries?  
* **Human‑in‑the‑Loop:** What interfaces make authoring and maintaining CxUs painless enough that teams actually do it?

## Conclusion: Toward Trustworthy Context Engineering

More memory isn’t a cure if your memories are a mess. Provenance, versioning, traceability — these boring, hard‑to‑implement facets are what make the difference between a demo and a dependable tool. Context Units bake those facets in from first principles. They force us to decide *what we actually know* and *where it came from* **before** we ever prompt the AI.

**Key takeaway:** Better context beats more context. LLMs don’t need an infinite scrapbook; they need a curated set of facts that carry their own receipts. Focus on provenance, not just persistence, and you’ll end up with AI systems you can trust — and maybe even take to an audit committee without breaking a sweat.

_Tried structured context or CxUs in your own projects? I’d love to hear your war stories or questions. Drop them in the comments!_

<!-- BLOG_GIT_METADATA START -->

<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> 2025-08-03</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> 2025-09-19</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> 5</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">61d7ff01ba63258b...</code></p>
      
      <div style="margin-top: 1rem;">
        <p style="margin: 0.5rem 0; font-weight: 500;">Recent Changes:</p>
        <table style="width: 100%; font-size: 0.85em; margin-top: 0.5rem;">
          <thead>
            <tr style="border-bottom: 1px solid var(--md-default-fg-color--lightest);">
              <th style="text-align: left; padding: 0.25rem;">Date</th>
              <th style="text-align: left; padding: 0.25rem;">Author</th>
              <th style="text-align: left; padding: 0.25rem;">Change</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="padding: 0.25rem;">2025-09-19</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">Added the github "Content Provenance" onto each...</td>
            </tr>
            <tr>
              <td style="padding: 0.25rem;">2025-08-03</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">added LLM Provenance article</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <p style="margin-top: 1rem; margin-bottom: 0;">
        <a href="https://github.com/zeroth-tech/blogs/commits/main/docs/posts/llms_provenance_problem.md" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
          View Full History on GitHub →
        </a>
      </p>
    </div>
  </details>
  
  <div style="margin-top: 0.5rem; font-size: 0.8em; color: var(--md-default-fg-color--lighter);">
    <p style="margin: 0;">
      <em>This metadata provides cryptographic proof of this document's creation and modification history. 
      The SHA-256 hash can be used to verify the document's integrity, while the Git history shows its evolution over time.</em>
    </p>
  </div>
</div>

<!-- BLOG_GIT_METADATA END -->

