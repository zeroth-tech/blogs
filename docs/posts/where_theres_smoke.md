---
authors:
  - jamescbury
date:
  created: 2025-09-18
draft: false
categories:
  - Identity
tags:
  - digital-identity
  - trust
  - authentication
  - vero
  - blockchain
  - security
comments: true
---

# Friction Makes Smoke, and Where There's Smoke...

Eons ago in March 2025 I wrote a probably-too-long paper about the nature of establishing relationships between humans over digital channels. [Digital Identity Verification](digital_identity_verification.md) was an attempt at a framework to categorize how trust is formed between people — and then use that framework to systematically explain how bad actors manipulate that trust to perpetuate identity fraud.

I still think the paper is accurate, though I missed a critical point. I had positioned my argument around people establishing trust with other people via technology. What I overlooked is that the majority of technical approaches today focus on establishing trust between devices and/or software and, by extension, the people using them. These approaches often assume that the identity of the person becomes inherent to the device.

It is this critical gap — between human and technology — that we are looking to bridge with Vero. Building tools to facilitate real-time peer-to-peer authentication inherently creates friction in the process. But our friction is intentional: it’s a demonstration of trust, a clear signal of intent. And that signal is the smoke. In our case, if you see the smoke, you can be confident there is no fire.

<!-- more -->

## Technology, Trust, and Inevitability

Deepfakes have rung the alarm bell (it may not be blaring yet, but it has been rung) and are beginning to cause healthy skepticism in technology trust. Yet time and again it’s proven — and I am a prime example — that even if people don’t completely “trust” the technology, they still lean into it.

Take SMS-based two-factor authentication. It’s well known to be vulnerable to SIM-swap attacks and interception, yet it remains the default option offered by banks, social media platforms, and even government systems. And despite knowing it’s not the strongest protection, most people (myself included) continue to use it. We lean on the herd mentality — if a big platform says “this is secure enough,” and it comes with a little green checkmark, we assume we’re protected.

Personally, I choose to think we are protected — having spent 20 years at an audit and accounting firm, I’ve grown to appreciate the rigor large enterprises put into securing their tech. They do the best that can be done. But as a cryptographer friend of mine likes to say, “given enough time and money, everything is breakable.”

Even if the technology were completely secure, social hacks would still exist. Con men thrived long before computers. When it comes to establishing trust between people, there is no single solution. We need a tool belt: instruments for different situations, integrations across forms of identity and reputation, and the ability to ratchet up security when something feels wrong.

Preventing identity fraud isn’t just about proving who you are — it’s about quickly establishing trust. If done right, the two are inseparable. Trust is king. As I tell my kids: trust is like a sandcastle — it takes effort and time to build, but it can be wiped out very fast.

From a digital perspective, identities can be granted and revoked. Trust, however, requires a track record and reputation. The challenge is making those elements usable for real-time verification. Because trust takes work, the real question is: how much work does it take?  Sometimes it doesn't take any work, but rather just your willingness to do it.

## The Balance of Friction

“Frictionless” was always one of my favorite consulting buzzwords. It implies a magic wand that takes away everything annoying about a process. But in reality, processes are rarely frictionless — at best we just shift the friction to a less painful place (or make it someone else’s problem). And sometimes, introducing friction is the whole point. I knew several CFOs who held the opinion: nothing curbs spending better than a clunky procurement process.

The key is applying friction on a graduated scale — with options. On a perilous slope, you might want more grip the further and faster you slide. Sometimes you need a handhold, sometimes an ice axe. Different situations call for different tools.

So when people say Vero introduces friction to the authentication process, I agree. Nobody wants to flash a blinking light on their face while staring into a webcam. But those who are willing to do it are making a statement: “I want to prove you can trust me.” That willingness itself is a demonstration of intent.

## Behavioral Change and Selective Friction

We also hear: “Vero requires a behavioral shift, and changing behavior is impossible.” I agree — to an extent. If you expect people to change just because it’s better for the system, good luck. If the change doesn’t have an immediate, meaningful payoff for the individual, it won’t happen either.

But when people understand that trust requires doing something extra — and that the extra step only comes into play when it matters — that’s a manageable level of friction. Better yet, if that extra step is tangible and immediately recognized by others as a signal of trust, adoption becomes easier.

As scams grow more common and the fear of being defrauded rises, resistance to that friction will fall; and so people need the tools to be available.

That’s why Vero is designed to be optional. You can be in the middle of a conference call, notice something feels off, and request verification. Or you can use it before sharing sensitive information. Much like selective disclosure, Vero works best when users choose it — when it becomes their tool to show their intent.  The objective is to have the option to be available and to have users aware of its existence, which is why we are planning to build it into existing technology stacks.  Of course there would be nothing preventing users or institutions from requiring its use in certain circumstances, which supports our licensing strategy.

## Layers of Proof

Another common push back is: “If I can prove my identity via a Temporal Identity Proof, why do I need to blink a light on my face?”

Answer: you don’t. Vero is a layered cake — you can consume as much as you want. The one-time biometric (the blinking light) is the icing.  While it may be the most novel part of our design it is not something we intend people to do every time they interact.

This perspective also raises the point that the Temporal Identity Proof (TIP) and its real-time verification is valuable on its own.  To understand why you need to ground yourself in one of our first principles-*Vero does not seek to own your identity*.  We think there are some great (and many not-so-great) identity solutions out there.  We also think the identity space will continue to evolve and that decentralized technologies like DIDs and ZK Passports are the way of the future; but these are generally not in our hands right now and there is still a very long learning curve before they are mainstream.  In the meantime, TIPs let you use the credentials and reputations you already control.

And remember — reputation often matters more than formal identity. A driver’s license might prove I’m legally allowed to drive in New Jersey, but it doesn’t prove I’m the person writing this blog. My GitHub commit history does. Likewise, airport security doesn’t care about my GitHub handle. Different contexts demand different proofs.

That’s why Vero’s model is simple: bring your own identity.

## How You Bring It: Temporal Identity Proofs

We explain TIPs more deeply in our [lightpaper](https://vero.technology/lightpaper), but here's the basic flow:

1. **Identify trust anchors.** These may be reputational (GitHub, LinkedIn, X) or credential-based (Okta ID, ID.me, SpruceID, etc.). You'll need several.
   - Reputation takes time (sandcastles — use sparingly).
   - Credentials come from third parties, often mandated. Even in a DID world, you'll likely juggle multiple credentials.

2. **Select what to use.** You decide which anchors to disclose. Selective disclosure is the rule: you control what you share.

3. **Generate tokens.** Some services issue signed tokens (JWTs, OAuth assertions, etc.) proving account control. Many still don't. At launch, Vero will support only a handful of the common ones.

4. **Set expiration.** TIPs are temporal by design. They're valid in the moment, not forever. You may choose to acknowledge that verification at a future date, but the tokens used to establish it are no longer needed.

5. **Bundle and encrypt.** Packaging multiple tokens together risks deanonymization, so we encrypt — establishing a shared secret with the verifier in the process (read the white paper to understand why this is important).

6. **Verification.** The verifier checks the tokens. If they pass, you've proven control.

That’s it. TIPs are created locally and destroyed after use. No persistent templates. No central store.   There is some design space here where we are exploring tools to assist in the generation of multiple TIPs from a single set of tokens.  We are also evaluating the potential to store 'TIP verified' people in your contact list.

## Where's the Fire?

At the start I said: friction makes smoke. And in Vero, smoke is a good thing. It signals intent. It shows someone is willing to tolerate a little inconvenience to prove trustworthiness.

We flip the proverb on its head:
Where there is smoke, there is safety. And when there is no smoke — that’s when you should look for fire.

---

*What's your take on friction in digital identity verification? Have you found yourself trusting technology more than you probably should? I'd love to hear about your experiences with authentication systems that actually make you feel more secure. Drop me a line or share your thoughts.*

<!-- BLOG_GIT_METADATA START -->

<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> 2025-09-18</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> 2025-09-18</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> 1</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">65670915724e691b...</code></p>
      
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
              <td style="padding: 0.25rem;">2025-09-18</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">Create where_theres_smoke.md</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <p style="margin-top: 1rem; margin-bottom: 0;">
        <a href="https://github.com/zeroth-tech/blogs/blob/b9419ce5299242a41df9572414a7e2e6dd8eecf8/docs/posts/where_theres_smoke.md" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
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

