---
authors:
  - jamescbury
date:
  created: 2025-07-22
draft: false
categories:
  - Fundamentals
tags:
  - cxu
  - context windows
  - knowledge density
comments: true
---
# Context Efficiency

It's funny I've spent years talking about tokens in all of my blockchain work. Whether it be NFTs or stablecoins, it seemed like tokens were everywhere.  Now that we're diving in deep and trying to fix some problems with context in AI, it seems the topic of tokens (albeit a very different kind) is still center stage.  The phrase "tokenization of the world" has taken on a new meaning to me.
 <!-- more -->

!!! note "crypto tokens ≠ AI context tokens"
    Just to be clear - these are not the same thing, but they do share some commonalities.  For example, both tokens were created as a way of driving efficiency in interactions with the underlying systems.  

    In the case of blockchain, it's more straightforward - tokens represent something of value or utility, and and the amount of them available is meant to drive an economy that will incentivize certain behaviors (Unfortunately, those behaviors are not always the greatest... But that's a different blog post.) 
    
    In modern large language models (and AI in general) tokens are the way that we communicate with the model. Tokenization is simply a text-segmentation strategy that turns bytes/chars into sub-word units so models can operate efficiently. It's easy to think of each word we include in a prompt as being a token, though it's worth understanding that that is a very rough analogy.  Words are not always efficient in conveying context. So oftentimes many filler words can be combined into a single token, whereas very unique words may require several tokens. The order in which those words are fed to a model help the model predict the order of tokens that it should respond with (mapped back to words of course).  The number of tokens fed to a model in a given prompt is referred to as the amount of context in that prompt.  And the amount of context that the model is capable of handeling is referred to as the "context window".

    To give you a sense of token size this side note is 267 words and can be represented in 319 tokens.

## Size Matters

The size of context window is important.  Transformer-based LLMs only remember what you can cram into a fixed-size window. The bigger the window, the more it costs to run — and the more chances you have to break something during prompt gymnastics. **Large** language models with **large** context windows require **lots of** compute.  We live in a world where:

1. Teams want richer, auditable knowledge injected into every AI interaction, *and*
2. Compute is limited - meaning costs can add up fast.

That tension demands a smarter way to package knowledge.

## Enter Context Units (CxUs)

A **Context Unit** is a bite-sized, immutable packet that captures exactly one statement you believe to be true, plus the evidence and metadata that back it up. Think of it as the atomic “fact card” in your personal knowledge deck. Each CxU is hashed, version-controlled, and reference-able, so you can trace any answer back to its source.  A complete collection of our CxUs could be said to represent our knowledge or our *worldview*.  I don't want to make it sound as if this were an easy thing to do.  Individual worldviews are messy and not easy to share - see my previous post on [distributed knowledge systems](https://zeroth-tech.github.io/blogs/2025/06/18/the-role-of-content-addressability-in-context-units-building-distributed-knowledge-systems/) - but CxUs are the place to start.

The context unit engine is a key part of what we built with [pyrana.ai](https://pyrana.ai). 

### Key Properties

| Property | Why It Matters |
| --- | --- |
| **Immutable** | If the content changes, so does the hash. No silent edits. |
| **Self-contained** | Claim, support, and metadata travel together — no loose ends. |
| **Composable** | Multiple CxUs chain into a worldview you can inspect or share. Cryptography helps us create and re-use CxU sets|

!!! pyrana "One truth per hash"
    A CxU should read like a sentence on a sticky note. If you can split it into two independent truths, you probably should.

## Context & Knowledge Density

“More context” isn’t always better. What we actually need is **higher knowledge density** — the maximum useful information in the minimum number of tokens. CxUs raise that density by stripping out narrative fluff and keeping only the parts of knowledge that an LLM can reason with.

Picture a 3,000-word white paper boiled down to ten or so CxUs. You’ve compressed the signal without losing proof or provenance. The result? Your prompt stays small, the model stays focused, and you *still* get traceability back to the source.  Reverse prompting the white paper based on the CxUs can help us measure the completeness of the extracted CxUs.

### Efficiency in the Prompt Pipeline

1. **Authoring** – Write or extract CxUs from docs, meetings, or code.
2. **Selection** – Query the CxU store for the subset relevant to your task.
3. **Packing** – Inject those CxUs (or even just their claims and IDs) into the prompt.
4. **Auditing** – Associate a set of cxu_ids to your prompt so you can prove where the answer came from.

Each step is deterministic, inspectable, and cheap compared to shoving the whole document into the model every time.

## CxUs vs. Common Knowledge Artifacts

| Artifact | Typical Form & Pain Points | What It Looks Like as CxUs |
| --- | --- | --- |
| Traditional notes | Free-form paragraphs, personal shorthand, hard to merge | Atomic claims + explicit metadata; query-able and deduplicated |
| Academic papers | 10-30 pages of dense prose, citations buried in footnotes | Each key claim distilled into a CxU linked to its source; higher knowledge density |
| Company policies | Legalistic language, versioned by filename, diff-unfriendly | Each clause hashed; version chain + audit-friendly diffs |
| Slide decks | Bullet points & images; meaning lost without presenter | Each slide broken into one or several claims with references to each other|
| Meeting minutes | Chronological logs; action items buried | Action items extracted as requirement-type CxUs; searchable by tag |
| Email threads | Nested replies, tangents, mixed topics | Relevant statements distilled into CxUs with references to message IDs |

## Practical Example

Imagine you’re building an AI assistant for supply-chain compliance. Instead of pasting entire regulations into every prompt, you create a library of CxUs such as:

> *“In the EU, a shipped product must include a Declaration of Conformity before customs clearance.”*

- **Claim**: In the EU, a shipped product must include a Declaration of Conformity before customs clearance.
- **Supporting context**: This requirement is defined in EU Regulation 765/2008, Article 30, to ensure product safety and compliance.
- **References**: [EUR-Lex 765/2008 Article 30](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32008R0765)

Tag it `supply-chain`, `eu`, `regulation`. When a user asks about exporting to Germany, the retrieval engine surfaces that specific CxU (and maybe five others) — **not** the entire regulation text.

## Takeaways

!!! success "**Key Points**"
    1. CxUs maximize knowledge density per token.
    2. They make LLM reasoning traceable and auditable.
    3. They turn messy documents into modular, query-able facts.

We’re just scratching the surface here. In the next post we’ll roll up our sleeves and explore the nuts and bolts: schemas, version control, tagging strategies, and the engine that makes CxUs tick.

<!-- BLOG_GIT_METADATA START -->

<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> 2025-07-23</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> 2025-07-23</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> 1</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">3be38a2157d3a738...</code></p>
      
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
              <td style="padding: 0.25rem;">2025-07-23</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">Added CxU posts and custom Admonitions</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <p style="margin-top: 1rem; margin-bottom: 0;">
        <a href="https://github.com/zeroth-tech/blogs/blob/b9419ce5299242a41df9572414a7e2e6dd8eecf8/docs/posts/CxU_context_efficiency.md" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
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

