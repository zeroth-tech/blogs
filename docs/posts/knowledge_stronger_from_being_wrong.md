---
authors:
  - jamescbury
date:
  created: 2026-04-30
  updated: 2026-10-06
draft: false
categories:
  - Agentic AI Research
tags:
  - knowledge management
  - context engineering
  - cxu
  - cortiq
  - pyrana
  - antifragile
  - epistemology
comments: true
---

# Knowledge That Gets Stronger From Being Wrong

We've come to equate knowledge with wikis, and most wikis are wrong - or at least they will be eventually.  That's not a knock on wikis, it's a knock on the assumption underneath them: that the stuff we wrote down is correct.  This post is my attempt to argue for a different starting assumption (that it probably isn't) and to explore what a knowledge system looks like if you build it that way from the beginning.

<!-- more -->

!!! abstract "TL;DR"
    Every knowledge management system I've ever worked with assumes the knowledge inside it is right.  I think that's backwards.  If you assume it's wrong and build the system to get a little better every time it gets caught, you end up with something that improves with age instead of rotting with it.  That's what we've been building with Context Units and CortIQ - but the argument stands on its own.

!!! pyrana "About us"
    Zeroth Technology builds [Pyrana](https://pyrana.ai/), a governance layer for agentic AI.  The two pieces of it that show up in this post are **Context Units (CxUs)** - our atomic unit of enterprise knowledge - and **CortIQ**, the learning loop that sits around them.  I'll try to keep the product talk to a minimum, but fair warning, it's kind of the point of the post.

## How wikis go bad

I've had a front row seat to this more times than I'd like to admit.  Somebody (often me) stands up a wiki, or a SharePoint site, or a "knowledge base", and for about six months it's great.  Then the workflow it was written for changes, the person who owned it moves on, and the page that says "single source of truth" at the top was last touched in 2019 (by someone who no longer works there, naturally).  There's a folder in there somewhere named *FINAL_v3_USE_THIS_ONE.xlsx*.  You know the one.

But here's the part that actually bothers me: the wiki doesn't stop working.  It keeps answering questions.  Nobody gets an error message that says "this page is probably wrong now"... they just get the page.  A knowledge base that fails loudly would be fine; the problem is that ours fail while still serving traffic, and the people asking have no way to tell the difference.

I've spent a good chunk of my career on the other side of this too, helping write guidance for an entire industry through the GAMP work within ISPE.  It took me a while to work out why that felt like the same problem, because on the surface it isn't; industry guidance is reviewed to death, every word gets cited and argued over for years, nobody is going to leave a *FINAL_v3* in there.  The tension is different.  It's that knowledge changes, and guidance has to be applied with judgement.  You can't write a document that anticipates every situation, so you end up with layers:

1. **Policy** - the things that must be true, full stop.  These change rarely and when they do it's a big deal.
2. **Procedure** - how we actually do it today.  These change all the time (or should), and the moment they stop changing you should get a little suspicious.
3. **Guidance** - how to think about it when the procedure doesn't quite cover your situation.  This is where the judgement lives.

The interesting stuff happens at the decision points - the places where a person has to look at the policy, look at the procedure, and decide that this situation is a little different.  That's where knowledge actually gets *made*, and it's exactly the part that never gets written down.  We capture the policy and the procedure and we lose the judgement.  So the wiki problem and the guidance problem turn out to be the same problem after all.  We are pretty good at recording what we decided and pretty terrible at recording why, and the "why" is the only part that tells you when the answer has stopped being true.

## A quick word on the two authors I keep leaning on

I'm going to lean on two writers for the rest of this, so a proper introduction is in order (I've read both of these books more than once and I'm still not sure I've gotten everything out of them).

David Deutsch is a physicist at Oxford, one of the fathers of quantum computing, and the author of *The Beginning of Infinity*[^1].  The book is nominally about the nature of explanations, but the part that stuck with me is his view of what knowledge *is* - not a thing you have, but a process you run.

Nassim Taleb is... harder to summarize.  Former options trader, professional contrarian, and the author of *Antifragile*[^2], which is the book that gave us the word.  He's abrasive and he repeats himself and I think he's right about most of it.

They come at this from completely different directions (one from philosophy of science, one from risk and markets) and they land on the same design constraint.  That's usually a sign worth paying attention to.

## What knowledge actually is

Deutsch's move is to stop treating knowledge as a possession and start treating it as a process: we propose an explanation, we test it, we keep the ones that survive and toss the ones that don't, and we never actually arrive at a final answer.  He calls this *fallibilism*: every claim might be wrong, and the test of a knowledge system is not whether it contains true things but whether it can correct itself when it doesn't.

The sharper test (and the one I find more useful day to day) is whether an explanation is *hard to vary*.  A good explanation is one where all the details are doing work - change any of them and it stops explaining the thing.  A bad explanation absorbs any change you throw at it because none of the pieces are load bearing (myths, just-so stories, most vendor slide decks...).

Let me put that in terms of something I've actually watched happen.  "We store this product at 2 to 8°C because that's what the label says" is a true statement, and it's useless as knowledge.  Change the number to 2 to 10 and the sentence still works... nothing in it tells you *why*.  Compare that to "we store it at 2 to 8°C because the stability study showed a 4% potency loss after 72 hours at 12°C, so the excursion limit is 48 hours above 8" - now every number is doing a job.  If somebody comes to you with a temperature excursion you can actually reason about it, and (this is the important part) if the stability data gets updated you know exactly which claim needs to change.  That's the bar.  The first statement is a citation; the second is an explanation.

And notice what this rules out.  A pile of evidence is not an explanation.  Deutsch's big break with a few centuries of empiricism is that knowledge doesn't come from stacking up observations - it comes from good explanations, which we then test the observations *against*.  You can hold every quote, citation, and data point in the world and still never have said why the claim is true.  IMO this is the single biggest thing wrong with how we build knowledge bases today; they are citation piles.

Taleb sits next to this with the systems vocabulary.  His triad: *fragile* things hate volatility, *robust* things tolerate it, *antifragile* things *gain* from it.  Bones get denser when you load them; immune systems sharpen on exposure.  Put the two authors together and you get the constraint: if knowledge is fallibilist by nature (Deutsch), then the system that holds it has to be antifragile by construction (Taleb).  It has to *want* the corrections, because they are coming whether you want them or not.

Most of our KM tools are robust at best.  They tolerate updates without breaking.  None of them gain from being wrong.

## Why our knowledge systems are so fragile

They're built on the assumption that the knowledge is correct.  That's really the whole diagnosis, but it's worth walking through how it shows up, because it shows up in different costumes.

**The wiki** assumes correctness by default; a page is "true" until someone bothers to edit it, and there is no signal that tells you which pages are overdue.  I had a client whose SOP for a critical process was, by everyone's admission, not how anyone did the job... but every new hire was trained on it, and every audit checked that they had been.  The document was correct in the only sense the system cared about: it existed and it was approved.

**The fine-tuned model** assumes correctness at a point in time and then laminates it in.  Fine-tune on last year's documents and you get a very confident model that still thinks the old org chart is current and the old procedure is the procedure.  Worse, you can't ask it which of its answers are stale, because the training set isn't in there anymore - it's been averaged into the weights (I wrote more about this in the [community experts post](community_experts.md) - the short version is please don't train your model to be an expert).

**The RAG pipeline** assumes correctness at retrieval time.  Two chunks that flatly contradict each other both land in the prompt, the model hedges, and out comes something plausible with no audit trail.  The contradiction was the most useful signal in the whole corpus (it's exactly where Deutsch would say the criticism should start) and the pipeline was built to smooth it over.

And then there is the one that's easiest to miss: **stale knowledge that nobody uses.**  This one is sneaky because it doesn't look like a failure.  A claim that hasn't been retrieved in two years is either (a) still true and just rarely needed, or (b) obsolete, and the system has no way to tell those apart because nothing has ever tested it.  Taleb has a concept for the first case - the Lindy effect, where things that have survived a long time are likely to keep surviving - but Lindy only applies to things that have been *exposed* for that time.  A claim that sat in a wiki untouched hasn't survived anything.  It's just been ignored.

These aren't bugs in any particular tool.  They are properties of the unit; if your atom of knowledge is a wiki page or a document chunk, you can't escape them, you can only manage around them.

## The atom

So we changed the atom.  A Context Unit is one claim, some supporting context (ideally an explanation of *why* the claim is true - not just a quote that someone said it), a durable identity that can't be silently edited, and enough metadata to argue with: who wrote it, where it came from, what it applies to.

That's the whole shape.  We've covered the schema in [earlier posts](CxU_blueprint.md) so I won't repeat it here - what matters for this argument is what the shape lets you do that a page or a chunk can't.

**The supporting context is an explanation, not a citation.**  This is the hard-to-vary test baked into the schema.  A claim that can't say why it's true isn't a fact, it's an opinion with footnotes... and the validator will tell you so.

**The identity is content-addressed.**  Edit the claim and the identity changes; the old version stays addressable.  The trail *is* the truth, and a claim that has survived unchanged for three years while being retrieved every week is a claim you can actually trust (that's Lindy done properly - survival under exposure, not survival under neglect).

**Contradiction is a first-class object.**  When two claims disagree the system doesn't pick a winner and bury the loser.  It keeps both and flags the disagreement so anyone (or any agent) reading the corpus can see it.  This felt weird to build (every instinct says resolve it) but flattening the contradiction is exactly how the wiki hides the rot.

**Not every claim gets the same governance.**  This is the policy / procedure / guidance thing from earlier showing up in the data model.  Foundational claims (regulated policy, security, compliance) are frozen by design and changing them requires a process.  Operational claims evolve under usage pressure.  There is deliberately no "kind of important" middle tier, because that's the tier where things go to rot.

**Provenance is stamped on everything.**  Who, when, where the source language lives.  Criticism can't do any work without it.

|                           | Wiki                    | RAG over docs                   | Fine-tuned model          | CxUs + CortIQ                  |
| ------------------------- | ----------------------- | ------------------------------- | ------------------------- | ------------------------------ |
| When a fact changes       | Silent edit             | Stale chunk still retrieved     | Frozen until retraining   | New version; old one kept      |
| When two sources disagree | Edit war, or one wins   | Both retrieved, neither flagged | Averaged into the weights | Both kept, disagreement marked |
| Provenance                | "Last edited by," maybe | None                            | None                      | On every claim                 |
| Failure mode              | Invisible decay         | Invisible hallucination         | Invisible confidence      | Visible decay, with a trail    |

## The body

CortIQ is what you get when you wrap a learning loop around the atom.  It's the part that turns CxUs from a nice schema into an actual error-correction process.

Every claim gets scored twice.  Once when it's written, against a quality rubric (is this a good explanation, does it pass the hard-to-vary test).  And again every time it's retrieved, against the world (did this claim actually help).  The first score is bounded; you can max it out.  The second is open-ended, and over time it's what separates the claims that keep earning their keep from the ones that stopped a while ago and nobody noticed.

This is the one place I really want to lean on Taleb, because it's load bearing: every retrieval is a small stress test, and small repeated stresses are exactly what makes a system stronger (he'd call it hormesis - the same reason a little bit of load makes a tendon tougher).  The wiki was starved of that signal.  CortIQ feeds on it.

It also answers the stale-knowledge question from above.  Claims that stop being retrieved, or that get retrieved and don't help, drift down in score until they stop surfacing.  They are never deleted - the information stays auditable, it just loses its voice.  Fallibilism with receipts: the system keeps the version of the world that turned out to be wrong, because hiding the mistake makes the next one harder to catch.

And it watches for patterns of failure - questions the corpus repeatedly can't answer.  Instead of logging those and moving on, it routes them back as a prompt to go find the missing knowledge.  Deutsch has a line I keep coming back to: *problems are inevitable; problems are soluble.*  The first half is realism, the second half is a job description.  A wiki goes silent when it doesn't know something and the silence is invisible.  CortIQ raises its hand.

## Tying it all back together

The real test of any knowledge system is what time does to it.

Run a wiki for ten years and you get a graveyard with working search.  Fine-tune a model on a decade of documents and you get a confidently wrong oracle frozen at the moment training stopped.  Stand up a RAG pipeline and watch it serve increasingly stale chunks with increasingly polished prose.  In all three, time degrades the asset and nothing turns the degradation into improvement - because all three assumed the knowledge was correct when it went in.

Run a CxU graph for ten years - corrections piling up in the trail, contradictions kept visible, usage scores climbing on the claims that keep proving useful and sinking on the ones that don't, the foundational layer pinned and the operational layer churning - and the bet is that you have a knowledge base that is *more* trustworthy in year ten than it was in year one.  Not because it has more in it.  Because it has been wrong, repeatedly and in public, and it kept the receipts every time.

I don't know that we've got all of this right (that would be a little ironic given the subject)... but I'm pretty confident about the starting assumption.  Knowledge isn't something we possess, it's something we make by finding and fixing our mistakes.  The wiki was a fragility we tolerated because we didn't have a better unit.  I think we have one now - and if you think I'm wrong about that, the comments are open, which is kind of the point.

---

[^1]: David Deutsch, *The Beginning of Infinity: Explanations That Transform the World* (Allen Lane / Penguin, 2011).

[^2]: Nassim Nicholas Taleb, *Antifragile: Things That Gain From Disorder* (Random House, 2012).
