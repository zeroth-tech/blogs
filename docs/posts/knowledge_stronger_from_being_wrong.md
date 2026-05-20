---
authors:
  - jamescbury
date:
  created: 2026-04-30
draft: false
categories:
  - Agentic AI Research
tags:
  - knowledge management
  - context engineering
  - cxu
  - cortex
  - pyrana
  - antifragile
  - epistemology
comments: true
---

# Knowledge That Gets Stronger From Being Wrong

We've come to equate knowledge with wikis, and in my experience, most wikis are wrong — or at least they will be eventually.

<!-- more -->

!!! abstract "TL;DR"
    Knowledge bases rot quietly while still serving traffic — not because of bad tooling, but because they're built on a finalist theory of knowledge. Deutsch (fallibilism) and Taleb (antifragility) arrive at the same fix from opposite traditions: a knowledge system has to *welcome* the corrections that being-wrong makes inevitable. This post argues for a different atom — Context Units — and the learning loop around them (CORTEX) that turns each retrieval into a small stress test the corpus grows from.

!!! pyrana "Pyrana → CxUs → CORTEX"
    **Pyrana** ([pyrana.ai](https://pyrana.ai/)) is our governance layer for agentic AI — built around **Context Units (CxUs)**, an immutable atom for enterprise knowledge. **CORTEX** is the newer half: the learning loop around the corpus that turns being-wrong into signal. The forthcoming CORTEX whitepaper covers it in detail.

The wikis aren't full of malicious lies — just decay. A page written for a workflow that no longer exists. A "single source of truth" that was last updated by someone who left in 2019. A SharePoint folder named *FINAL_v3_USE_THIS_ONE.xlsx*. The most insidious thing about a corporate knowledge base isn't that it fails — it's that it *answers questions* while it fails. The wiki rots quietly while still serving traffic.

Over the years I've also been fortunate to contribute to the GAMP guidance within ISPE — and that work has shown me this isn't only an enterprise problem. Establishing a corpus of knowledge on behalf of an entire industry is a real discipline; every word will be cited and challenged for years. And yet the central tension is the same one a rotting wiki faces: pragmatic guidance based on our latest thinking versus long-settled practice that has to stand the test of time. Publishing guidance is a monumental effort, and even careful work goes stale faster than the industry it's meant to govern.

This is not a tooling problem. It's an *epistemology* problem. Our knowledge bases are fragile because they were built on the wrong theory of knowledge — one that treats knowledge as something you *possess*, store, and serve, with the job of a KM system being to find the canonical version of each fact and lock it down. Two of my favorite authors — David Deutsch[^1] and Nassim Taleb[^2] — arrive at the same critique from different traditions: Deutsch from the philosophical side (knowledge is provisional and grows only through error correction), Taleb from the systems side (the systems worth building are the ones that *gain* from disorder rather than merely tolerating it). Together they give us the design constraint that traditional KM violates: knowledge is fallibilist by nature, so the system that holds it has to be antifragile by construction. Pyrana[^3] is the platform we've been building toward that constraint — Context Units (CxUs) as the atomic unit of knowledge, governed and provenanced from the start. CORTEX is the newer half: the learning loop around the corpus that turns being-wrong into signal. The rest of this post is about both.

## What Knowledge Actually Is

Deutsch's move is to treat knowledge not as a possession but as a *process* of conjecture and criticism. We propose explanations; we test them; we keep the ones that survive criticism and discard the ones that don't; we never reach a final answer. This is *fallibilism*: every claim is potentially wrong, and the test of a knowledge system is not whether it contains true things but whether it can correct itself when it's wrong.

The deeper test, for Deutsch, is whether an explanation is *hard to vary*. A good explanation is one whose details all do real work — change any of them and it no longer accounts for the phenomenon. Bad explanations (myths, just-so stories, vibes) absorb almost any modification because none of their pieces are load-bearing. "We file expense reports through System X because that's our process" is infinitely variable; it isn't really an explanation. "Section 4.2 of the SOX-aligned controls policy requires expense documentation in System X for transactions over $5,000" is harder to vary — it has structure, a source, and you can criticize it. That's the bar.

And notice what this rules out. A pile of evidence is not an explanation. Deutsch's sharpest break with centuries of empiricism is that knowledge doesn't come from accumulating observations — it comes from good explanations, which we then test evidence *against*. You can hold every quote, citation, and data point in the world and still not have said *why* the claim is true. That distinction is the one our knowledge atom is built around.

Taleb sits next to this with the systems vocabulary. His triad: *fragile* things hate volatility, *robust* things tolerate it, *antifragile* things *gain* from it. Bones get denser when you stress them; immune systems sharpen on exposure. A fallibilist system has to be antifragile, because it has to *welcome* the corrections that fallibilism makes inevitable. Most of our KM tools are robust at best — they tolerate updates without breaking. None gain from being wrong.

## Why Knowledge Management Systems Are Delicate Snowflakes

Most KM systems were built on the opposite theory: that knowledge has a final, canonical form that can be authoritatively recorded, and the tool's job is to keep that record clean. Finalist epistemology produces fragile systems no matter how much engineering you throw at it. Taleb's vocabulary is useful for diagnosing what goes wrong:

**Iatrogenics** is the harm caused by the cure. In KM, it's the mandatory tagging policy, the platform migration, the "single source of truth" initiative that produces a *second* source of truth and then a third. Most KM rollouts produce more confusion than they remove.

**The Procrustean bed** — forcing reality to fit a pre-built model — is what fine-tuning does. You cut the legs off this quarter's knowledge to fit last quarter's weights. Knowledge that should be provisional gets laminated into the model and shipped.

**Touristification** is the systematic removal of friction. A wiki with one big edit button and no review workflow is easy right up until you realize nothing tells you which page rotted last week. Friction was the immune system; we sanded it off because we believed in finality.

RAG[^4] isn't in Taleb's vocabulary, but it belongs in this diagnosis. Two retrieved chunks that flatly contradict each other both make it into the prompt; the model hedges, synthesizes something plausible, and ships it with no audit trail. The contradiction was the most important signal in the data — exactly where Deutsch would say criticism should *begin* — and the pipeline was built to hide it.

These patterns are not bugs in any specific KM tool. They're properties of the *atom*. If your unit of knowledge is a wiki page or a doc chunk, you cannot escape them — you can only manage them.

## The Atom

A Context Unit is the atom we replaced the discrete pieces of knowledge in a wiki page with. One claim. Some supporting context — ideally an explanation of *why the claim is true*, not just a quote that someone said something. A durable identity that can't be silently edited. And enough metadata to argue with: who wrote it, where it came from, what it pertains to.

That's the whole shape. What matters for this argument isn't the schema — we've shared that in earlier posts and the forthcoming CORTEX whitepaper covers that in detail — it's what the shape lets you do that a wiki page or a doc chunk can't.

**The supporting context is an explanation, not a citation pile.** A quote tells you that someone said something. A rationale tells you *why it's true* — and a rationale is something you can argue with. A claim that doesn't carry that kind of explanation isn't a fact. It's an opinion with footnotes.

**The identity is content-addressed.** Edit the claim and the identity changes. Old versions stay addressable. The trail *is* the truth — and the longer a claim has survived unchanged, the more confidence you have that it's the same claim you trusted last year. (Taleb would call this Lindy at the storage layer; Deutsch would call it the visible record of which conjectures have survived criticism.)

**Contradiction is a first-class object.** When the system sees two claims that disagree, it doesn't pick a winner and bury the loser. It keeps both, and marks the disagreement so anything reading the corpus can see it. A KM tool that flattens contradictions out of view is a tool designed to halt the engine of knowledge growth; CxUs put the disagreement on the schema.

**Not all claims carry the same governance.** Foundational claims — compliance, security, regulated policy — are frozen by design; editing them requires a process. Contextual and operational claims evolve more freely under usage pressure. There is no "kind of important, kind of not" tier, because that's the tier where rot lives. (Roughly Taleb's barbell strategy, though it earned its place by solving a governance problem before we noticed it was a barbell.)

**Provenance is stamped on every claim.** Who wrote it, when it changed, where the source language lives — because criticism can't do any work without it.

| Property                  | Wiki                    | RAG over docs                   | Fine-tuned model          | CxU + CORTEX                       |
| ------------------------- | ----------------------- | ------------------------------- | ------------------------- | ---------------------------------- |
| When a fact changes       | Silent edit             | Stale chunk still retrieved     | Frozen until retraining   | New version; old version preserved |
| When two sources disagree | Edit war or one wins    | Both retrieved, neither flagged | Averaged into the weights | Both kept, disagreement marked     |
| Provenance                | "Last edited by," maybe | None                            | None                      | Stamped on every claim             |
| Failure mode              | Invisible decay         | Invisible hallucination         | Invisible confidence      | Visible decay, audit trail kept    |

## The Body

CORTEX is what happens when you put a learning loop around the atom — the part of the system that turns CxUs from a clever schema into a working error-correction process.

A claim gets scored twice. Once when it's written, against a quality rubric: *is this actually a good explanation?* And again every time it's retrieved, against the world: *did this prove useful?* The first score asks whether the claim is well-formed; the second asks whether it earns its keep. The first is bounded; the second is open-ended, and over time it's what separates the claims that keep paying off from the ones that quietly stopped. This is the one place I want to lean on a Taleb concept, because it's load-bearing: every retrieval is a small stress test, and the small repeated stresses are exactly what tunes the system. Hormesis at the system level — the same logic that says microloads make tendons stronger. The wiki was deprived of stress signal. CORTEX feeds on it.

Claims that prove unreliable are never silently deleted. Their usage scores drift down until they stop surfacing — the information stays auditable, it just loses its voice. Fallibilism with receipts: the system keeps the version of the world that turned out to be wrong, because hiding the error makes the next one harder to spot.

The learning layer also watches for *patterns of failure* — questions the corpus repeatedly can't answer. These aren't logged and treated as signal that knowledge is missing, they can be routed back as a prompt to go find it.

!!! quote "Deutsch on optimism"
    *Problems are inevitable; problems are soluble.*

The realism is the first half; the directive is the second. A wiki goes silent when it doesn't know something, and the silence is invisible. CORTEX raises its hand.

Beneath all of this, two layers accumulate rather than decay. The foundational layer — compliance rules, security policy, the things you don't want to relitigate on every retrieval — is always in context. And the system remembers which combinations of claims worked together on past queries, reinforcing the patterns that produced good outcomes. Time is the friend of the system, not the enemy.

## The Bet

The test of any knowledge system is what time does to it.

Run a wiki for ten years and you get a graveyard with working search. Fine-tune a model on a decade of corporate documents and you get a confidently wrong oracle, frozen at the moment training stopped. Stand up a RAG pipeline and watch it serve increasingly stale chunks with increasingly confident prose. In all three, time degrades the asset and nothing converts the degradation into improvement. The systems were built on a finalist epistemology and they age the way finalist things age: badly.

Run a CxU graph for ten years — corrections compounding into the trail, contradictions kept visible, usage scores climbing on the claims that keep proving useful and decaying on the ones that don't, the foundational layer pinned and the operational layer churning — and the bet is that you have a knowledge base that is *more* trustworthy in year ten than in year one. Not because it has more entries. Because it has been wrong, repeatedly and in public, and absorbed every instance.

!!! success "The wager"
    Knowledge isn't something we possess. It's something we make by detecting and correcting errors. The wiki was a fragility we tolerated because we didn't have a better unit. **We have one now.**

---

[^1]: David Deutsch, *The Beginning of Infinity: Explanations That Transform the World* (Allen Lane / Penguin, 2011).

[^2]: Nassim Nicholas Taleb, *Antifragile: Things That Gain From Disorder* (Random House, 2012).

[^3]: Pyrana ([pyrana.ai](https://pyrana.ai/)) is Zeroth Technology's governance layer for agentic AI — externalizing enterprise knowledge into immutable Context Units so agents can act on organizational context without losing accountability. CORTEX is the agent and learning layer within Pyrana — the part that scores claim usefulness, watches for knowledge gaps, and proposes governed updates back into the corpus. The forthcoming CORTEX whitepaper covers it in detail.

[^4]: Retrieval-Augmented Generation. See also our earlier post, *LLMs Don't Have a Memory Problem — They Have a Provenance Problem*.
