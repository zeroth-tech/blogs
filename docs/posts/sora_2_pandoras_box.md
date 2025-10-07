---
authors:
  - jamescbury
date:
  created: 2025-10-07
draft: false
categories:
  - Identity & Authenticity
tags:
  - deepfakes
  - ai
  - identity-verification
  - sora
  - security
comments: true
image: images/vero.svg
description: The barrier to creating convincing deepfakes has vanished. Sora 2's cameo feature makes identity fraud easier than ever. Here's why we should be concerned and what Vero is doing about it.
---

# We've Opened Pandora's Box: Why We Should be Concerned About Sora 2

Even though we've seen this train coming, seeing it in action still gives me pause - the moment something becomes "easy," it also becomes dangerous. Over the weekend I started playing around with Sora 2 from OpenAI, and let's just say — this thing is equal parts miracle and nightmare fuel.

The “cameo” feature alone is so good it’s unsettling. What used to take teams of visual-effects artists and GPU clusters now happens on a laptop — or worse, on your teenager’s iPhone. While you have to admit the tech is amazing - if we put a malicious bent on things, we have to consider that when the technical barrier drops, the attack surface explodes. And Sora 2 just dropped that barrier to the floor.

<!-- more -->

## What Makes Sora 2 Different

Text-to-video has been rapidly advancing, and Sora 2 is just the next step.  What stands out to me is the ease of enrollment. You take a quick selfie, look left, right, up, down, and read a few numbers out loud. Thirty seconds later you've got a photo-realistic avatar you can insert into just about any video scene you can imagine.  OpenAI built Sora 2 to be a social app and included a "Cameo mode" so you can share your avatar with others - it's no surprise that they are dealing with the backlash of copyright infringement right now, but I'm sure they will figure it out. I would say they took minimal steps to let people know the videos are generated; they added some watermarking, and they make it kind of clunky to move the videos outside of their platform - but that's like holding a vault door shut with paper tape.

⸻

## The Problem They're Not talking about on X

OpenAI has been getting slammed on social media about their content restrictions and strategy for IP, but I haven't heard anyone talking about the effect that Sora will have on identity fraud.  If I can make a convincing digital version of myself that easily… what’s stopping someone else from doing it for me?

To prove the point, I created a short video using my own and Sam Altman’s likeness (he made it available for cameos while promoting Sora). In the clip, “Sam” talks about identity fraud and how Sora makes it easy.

<div style="float: right; margin: 0 0 1em 1em; max-width: 50%;">
  <video width="100%" controls>
    <source src="../../../../sora_2_pandoras_box/sora_sama_interview.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

!!! warning "disclaimer"
    obviously this video is fake. I don't know Sam Altman, and he didn't say a word of this. But he made his likeness available — so I used it to illustrate the problem.

The fact that I could do that in minutes, with consumer tools, should make everyone pause. If I can impersonate Sam Altman, someone else can impersonate you.  Just to be clear - I'm not explicitly directing this concern at OpenAI.  In reading their ["launching responsibly" section on Sora 2](https://openai.com/index/sora-2/) they do discuss how they approached user authentication and the ability for someone to share, or remove, their avatars and clearly their algorithms are cranking away at flagging "content violations".  And I did have to agree *not* to upload images or likenesses of others without their consent *(as if some people were not already thinking about doing this)*.
<div style="text-align: left;">
    <img src="../../../../sora_2_pandoras_box/Sora User Agreement.png" alt="Sora Media Upload Agreement" width="50%">
</div>
However, these legal requirements are very weak forms of protection. Given their popularity, I would expect all of the other generative video platforms to have cameo's shortly.

## The Numbers Game Just Changed

Deepfakes aren’t new — they’ve just been hard. Until now. Historically, the effort required kept them niche: high skill, expensive compute, limited targets.
That barrier was our accidental defense.

But Sora 2 annihilates that. Which means fraud is about to trickle down.

The first wave won't even be about money. It'll be about believability:
 • Fake messages "from" family members
 • Manipulated local news clips
 • Fabricated interviews or confessions
 • Cheap chaos at scale

Again - if you've been following this space (like we have) this is not surprising - we've always said it's just a matter of time.  Well, the time is here; and now time matters.

## What are we doing about it: Why Passive Defenses Won’t Work

Here's the uncomfortable truth - even if we could stop the technology, people wouldn't want to.  Sora (and others) let people create viral content - and in our current society that is highly prized.  Once we accept this more broadly, the same technology that lets me deepfake Sam Altman for comedic purposes could — in theory — let him delegate his presence to AI. If he wanted to give a thousand simultaneous interviews tomorrow, why shouldn't he? What influencer wouldn't want their exposure to be 1,000x? It's for this reason that we will not be able to regulate the problem away, or rely on platforms (who seek to profit from viral feeds) to suppress it.

The line between legitimate avatar and malicious deepfake is razor-thin. The question shifts from "Is it real?" to "Can we prove who authorized it?"

Platforms are the first filter — sure. If the clip appears on sora and are tagged to users, we kind of believe they allowed it. But content moves. It’s reposted, remixed, re-contextualized.
And once it leaves that verified origin, its identity evaporates.  To post my Sam clip here I downloaded it and re-published via github.  I could have changed many things along the way.

We need a way for identity to travel with the content - and we need a way for that identity to be apparent to the casual viewer.  This is part of the problem we have been working to solve.

## Where Vero Fits In

If you scroll all the way back through all of our postings and white papers we initially positioned Vero as a method for people to prove that their likeness in a video is in fact A) "their" likeness and b) that they approve it.  We call this the "presenter initiated flow" because it requires that a person wishes to prove themselves to anyone watching (either in real time or at a later point in time).  In my fake Sam video above, if he had pulled out his phone and done a verification with Vero, I would be able to prove if he did (or did not) authorize his likeness.

But wait - if I can pretty much generate anything super easily now, why can't I just generate Sam's phone blinking some lights on his face?  That's because it's not just some lights - it's a code.  We embed a cryptographic signature into the video stream - it uses a unique session key that we can prove was generated using Sam's digital ID - in that moment and for that purpose only (I assume he has a world ID given his association there - but any digital ID capable of signing a transaction will work).  So even if I wrote a prompt clever enough to get Sora to blink out a specific code (it's not easy, I tried...) I wouldn't be able to know the code unless Sam generated it and shared it with me.  And oh, by the way, I could have my own avatar do the same thing.  *(disclosure: to make this work in a platform like Sora does require a minor extension to our current design)*.

Once we have that we can integrate with protocols like C2PA to tackle content authenticity post distribution.

## But do you really need the blinking?

As I discussed in my [last post](where_theres_smoke.md) the answer is not always, it's situational in nature.  If I were using my likeness in a video where Albert Einstein gives me a lift to class (keep scrolling :) then no that would take away from the humor.  I would simply embed my proof into the video metadata.  But if I were to have an interview with "the real Sam Altman" I would sure as heck want to prove it was actually him - or if I were to release some breaking news about my company it would be in my best interest for anyone watching to easily be able to verify it was me.

!!! note
    I want to clarify the waters that I may have just muddied with this post... we have been actively marketing Vero as a one-time-biometric and a peer-to-peer authentication approach.  What I just described is *not* that... Avatars don't have biometrics (or do they?).  What I am talking about in this post is an extension of the presenter initiated flow that where I would like to authorize my likeness to be used in a video and where it can be made apparent to many viewers (regardless of the platform) that the likeness was authorized by me.  That is one of the core technical components of Vero.

    When we discuss one-time-biometrics and peer-to-peer authentication we are discussing the "verifier initiated flow" of Vero where a verifier wishes to establish trust directly with a presenter.]

## Closing Thoughts - What This Means for Us

The barrier to creating convincing deepfakes has vanished. The capability is public. The risk is immediate.
We can't regulate our way out of this - and we shouldn't rely on the platform that generates the content to prove the authenticity of *our* likeness.

Instead, we need proof systems that move with the content — proofs that travel, verify, and expire in real time.
Vero is one approach. There will be others. But waiting isn’t one of them.

Because whether we like it or not, Pandora's box isn't closing. The only question is how we keep trust from flying out with it.

And just because I couldn't resist... here's another one


<div style="text-align: center;">
  <video width="50%" controls>
    <source src="../../../../sora_2_pandoras_box/jamey-albert-bike.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

!!! warning "disclaimer"
    *I do not know Albert Einstein, I've never ridden on his handle bars, I did not get permission to use his likeness, but I also did not upload any media of his likeness as per my user agreement.*

<!-- BLOG_GIT_METADATA START -->

<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> 2025-10-07</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> 2025-10-07</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> 1</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">236c466a27ce447d...</code></p>
      
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
              <td style="padding: 0.25rem;">2025-10-07</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">added the Sora 2 article</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <p style="margin-top: 1rem; margin-bottom: 0;">
        <a href="https://github.com/zeroth-tech/blogs/blob/ac6f11cfa42049481ac2f04c7888efaa2d9bdaff/docs/posts/sora_2_pandoras_box.md" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
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

