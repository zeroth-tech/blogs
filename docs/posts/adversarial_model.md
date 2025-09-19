---
authors:
  - ankmister
  - patmac
date:
  created: 2024-07-22
draft: true
categories:
  - Identity & Authenticity
tags:
  - live streaming
  - adversarial
  - deep-fake
comments: true
---

# An Adversarial Model for Trusted Interactions in the Modern Era (TIME)

# PART 1: The Dishonest Presenter Problem

We're at a pivotal moment in human history, and most people don't even realize it. The ability to manipulate reality through digital means isn't just some sci-fi concept anymore - it's here, and it's evolving faster than our archaic institutions can handle.

Historically, impersonation and fraud have primarily occurred through voice channels, such as phone calls. However, the landscape is rapidly changing.

<!-- more -->

## The Adversarial Model

To understand the potential for deception in digital interactions, we will be using what we call an ‘adversarial model’ that considers different combinations of honest and dishonest presenters and watchers. Here is a basic definition of the four:

1. **Honest Presenter**: Someone speaking on video without introducing fake content.
2. **Dishonest Presenter**: Someone speaking on video while introducing fake content.
3. **Honest Watcher(s)**: One or more people watching the content produced by the presenter.
4. **Dishonest Watcher(s)**: One or more people who claim the content they are consuming is different from what the presenter is producing (less common but included for completeness).

|                     | Honest Watcher                                                              | Dishonest Watcher                                                                                                                       |
| ------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Honest Presenter    | No open issues. All content received and given is appropriate and approved. | Providence of Evidence, Testimony, Deposition recordings is compromised. Watcher is the one acting as an adversary. They are misleading |
| Dishonest Presenter | This is where the Presenter is misleading the content they are presenting.  | Both parties are misleading.                                                                                                            |

This model helps illustrate the various scenarios where trust can be compromised in digital interactions.

## Dishonest Presenter <> Honest Watcher

Today we will focus on how someone presenting information can mislead the people consuming that information, may that be a recorded video, a livestream, or even a zoom call. 

Let's break this down:

### **Face swapping? ✅**

Child's play. With enough compute, there are solutions out now where you can modify your face to someone else’s based on a single image of them and stream that out in realtime, including all of your facial features and expressions. Sure, there are some quality issues now, but give it six months. The lag will disappear, and the resolution will be indistinguishable from reality.

https://x.com/fal/status/1813289294414717038

In just a few minutes, I was able to whip up something pretty basic, this is as of July 2024. This tech is only going to get better. 

![Live Portrait video](adversarial_model/liveportrait1.mp4)

### Voice modulation? **✅**

ElevenLabs is already creating convincing voice imitations from tiny samples. Combine that with face swapping, and you've got a recipe for perfect digital impersonation.

!Voice Modulation Example

### Body language?  **✅**

It's not just about faces anymore. We're talking about manipulating the very cues that body language experts rely on to detect deception. The window to the soul is getting tinted, folks.

https://x.com/dr_cintas/status/1813959534651777240

### Video Call tech? **✅**

Using an alternate face, dynamically, as you hop on a zoom call, is soon going to be as simple as selecting a saved face and hitting join…

https://x.com/Mr_AllenT/status/1795109619741679822

## On the Horizon

The different technologies we discussed are rapidly developing today. Imagine them seamlessly integrated. This is Roast AI, a complete deepfake that currently requires a couple of days and about $10-35 for a human to assemble by hand. Available today. But soon, this will not require human intervention, and the deepfake will become an automated, real-time process.

Human intervention currently serves a dual purpose: it allows for moderation, preventing this technology from being used for nefarious purposes (in this case, anything besides some benign roasting). However, as these capabilities become more commonplace, we'll be able to simply prompt and receive an output (similar to [Runway Gen 3](https://runwayml.com/ai-tools/gen-3-alpha/)) for the digital model that we have loaded, with the exact voice of that person, in real-time.

Based on our panel of experts in programming, AI imaging technologies, and current enterprise/open-sourced project development, we estimate that near real-time, photo-realistic digital clones will be accessible to the average consumer within 6-12 months. The ramifications of this accessibility will have unpredictable outcomes across various fields. Proper confidence in real and genuine future media creation will be desired by nearly all impacted fields. We anticipate a cat-and-mouse scenario unfolding between existing proof-of-humanity assurance models and agitators, deceivers, and scammers, leading to a weekly, if not daily, contest.

## Take Away

The old centralized models of trust are crumbling, and those who don't adapt will be left behind.

It's not about stopping the technology - that ship has sailed. It's about evolving alongside it. Those who understand this shift, who can navigate this new landscape are the ones who will thrive in the coming decades.

There are nuances to how this tech can be used. Yes it can be used for deepfakes and assuming an alternate identity, but it is subtle enough to actually help mask your emotions.

! How it looks like you are feeling. 

<Loki Video composed>

! How you are actually feeling.

<Loki Video torn>

! You can only enter the store unless you smile.

All of this tech is publicly available. Today. It's not hidden behind some government firewall or locked in a corporate vault. It's out there, evolving in the open, with countless brilliant minds building on each other's work. Moore's Law is in full effect, and the cost is plummeting.

This tech is a tool, like any other. But we need to wake up to its implications. In a world where seeing isn't believing, where do we place our trust? How do we verify identity in a digital age?

This isn't just about elections or celebrity deepfakes. It's about the very fabric of our digital interactions. How do we conduct business, form relationships, or make decisions in a world where any digital interaction could be artificially generated?

<!-- BLOG_GIT_METADATA START -->

<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> 2024-07-23</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> 2024-07-23</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> 3</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">2f6248cb683c15d3...</code></p>
      
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
              <td style="padding: 0.25rem;">2024-07-23</td>
              <td style="padding: 0.25rem;">AnkMister</td>
              <td style="padding: 0.25rem;">adv model back to draft</td>
            </tr>
            <tr>
              <td style="padding: 0.25rem;">2024-07-23</td>
              <td style="padding: 0.25rem;">AnkMister</td>
              <td style="padding: 0.25rem;">test adv model</td>
            </tr>
            <tr>
              <td style="padding: 0.25rem;">2024-07-23</td>
              <td style="padding: 0.25rem;">AnkMister</td>
              <td style="padding: 0.25rem;">draft adv model</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <p style="margin-top: 1rem; margin-bottom: 0;">
        <a href="https://github.com/zeroth-tech/blogs/blob/b9419ce5299242a41df9572414a7e2e6dd8eecf8/docs/posts/adversarial_model.md" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
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
