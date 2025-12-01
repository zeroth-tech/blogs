---
authors:
- jamescbury
date:
  created: 2025-10-29
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

# CxUs as Prompt "Pre-conditioners"

## The Precursor: Curated Training ⇒ Curated Inference

We accept that high‑quality training demands curated, labeled datasets. Inference should follow the same rule. CxUs bring that discipline to runtime: the same clarity, labeling, and provenance we require for training data—applied to the context we feed the model when it answers.

<!-- more -->

## A Simple Reframe: CxUs as Preconditioners

A preconditioner is a step that happens before you start working with data sets - it helps us make sure the data that you are feeding into a model accurately represents what we think it represents.  A lot of times it's thought of as an annoying data clean up exercise - and part of the "magic" of LLMs is their ability to sort-of do this for us when we dump in large unstructured data sets. This is fine for exploratory exercises, or in these early days when we are still critical of model outputs.  But for business critical systems and important decisions it isn’t a nice‑to‑have; it’s a step that puts inputs into a state where the core system performs reliably. In LLMs, the “core system” is the transformer—the part that does self‑attention and pattern finding ([Attention Is All You Need](https://arxiv.org/abs/1706.03762)).  Even after the model is fully trained, applying preconditioned prompts that let the model better understand your inferences is important.

CxUs are small, structured packets of knowledge: one clear claim, its supporting context, and helpful metadata (tags, links, version). When you assemble a prompt from sets of CxUs, you’re not dumping raw text into the model—you’re feeding clean, well‑labeled context. That pre‑aligns attention, reduces guesswork, and moves correctness onto the critical path instead of hoping the model infers relationships from noise. It's a way to hard wire truths into the inference process that has the side benefit of making that inference less computationally intense for the LLM.

## What Changes When You Precondition

- Clarity: One claim per CxU raises knowledge density and cuts filler.
- Control: You choose the exact set of units relevant to the task.
- Traceability: Each CxU is immutable and referenceable, so you can audit results.
- Consistency: The same CxU set can be reused across prompts and projects (a set of "mandatory CxUs can enforce guardrails")
- Comparability: The same CxUs can be applied across different LLMs, which is helpful for quality measures and for model evaluations.

The idea of "pre-processing" data is not new, so are we just rebranding old solutions? Not quite, LLMs are different animals when comapred to traditional data analysis.  Because we can easily throw both structured and unstructured data at them and *generally get good results* we have a tendency to just pile on more data.  Using CxUs as pre-conditioners help us address the garbage in/garbage out issue - I believe this shift is critical: it addresses prompt bloat, prompt injections, improves repeatability, and restores trust.

## How It Works (In Plain Terms)

We've coverd this in other posts, but just to recap the basic CxU process is:

1. Authoring: Distill sources into atomic CxUs (one claim, short support, metadata, version control).
2. Selection: Pull only the CxUs that matter for the question at hand.
3. Packing: Insert the claims (and, if needed, IDs or short support) into the prompt.
4. Auditing: Save the set of `cxu_id`s used so you can prove where the answer came from.

Under the hood, the transformer still does its job—tokenizing, attending, and generating. But because you preconditioned the input with CxUs, the model starts with clearer relationships and fewer distractions. Less effort goes into “figuring out what relates to what,” and more into reasoning with what you’ve already said is important.

## What CxUs Are Not

- They’re not model‑specific tokens. Every model has its own tokenizer; you should still pass text, not precomputed token IDs.
- They’re not magic. CxUs don’t remove the need for good prompts; they make good prompts dependable and reproducible.
- They’re not brittle. Because CxUs carry versions and links, your knowledge can evolve without losing history.

## Why This Scales

From enterprise policies to product specs, teams can author once and reuse everywhere. CxUs travel well: they’re immutable, content‑addressable, and easy to compose into sets. If you’re using a context engine like [Pyrana](https://pyrana.ai), you can even save sets with proofs (Merkle roots) and fetch only the fields you need (just `claim` for ultra‑lean prompts).

## Takeaways

- Precondition with CxUs to raise signal and cut prompt size.
- One claim per unit keeps attention focused and reasoning clean.
- Versioned, linkable units make answers auditable and teams aligned.
- Shared CxU sets let you compare LLMs fairly, apples‑to‑apples.

In my experience, this is the simplest way to get better results without throwing more context (and money) at the problem.

## What This Means for You

If your prompts keep growing but clarity doesn’t, try this: pick a single workflow, extract 8–12 CxUs, and run them through two different LLMs. Did quality go up? Did answers get easier to trust? There’s your signal.

<!-- BLOG_GIT_METADATA START -->

<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> 2025-10-29</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> 2025-10-29</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> 1</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">e31008219dc7a5b1...</code></p>
      
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
              <td style="padding: 0.25rem;">2025-10-29</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">added the CXUs as Preconditioners post</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <p style="margin-top: 1rem; margin-bottom: 0;">
        <a href="https://github.com/zeroth-tech/blogs/commits/main/docs/posts/CxUs_as_preconditioners.md" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
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

