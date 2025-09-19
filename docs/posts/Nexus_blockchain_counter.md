---
authors:
  - jamescbury
date:
  created: 2024-09-21
draft: false
categories:
  - Identity & Authenticity
tags:
  - digital truth
comments: true
---

# Nexus: A counter argument to blockchain's "Achilles heel"

Often we have books by great thinkers that shape the way we view the world and influence our outlook on the future.  For me Yuval Harari is one such thinker.  In this post I share my reaction/counterpoint to a statement that Prof. Harari makes in his new book "Nexus: A Brief History of Information Networks from the Stone Age to AI".
<!-- more -->

Let me start this post by saying that I am a huge fan of Prof. Harari.  Sapiens is one of the most influential books I have ever read - it opened my mind to the concept of intersubjective reality and the power of the stories we tell  - both how those stories can rule our lives and make our species capable of great things.

I just finished reading Nexus and it too is a great work, I tell my friends that part 1 is a history lesson and perhaps a bit of a slog, but just as Prof. Harari does in Sapiens and Homo Deus his thorough historical perspective sets the foundation for his later arguments.  Yes the book is a bit alarmist, but I don't think it is due to an algorithm instructing him to use outrage to sell copy... What he shares (in my opinion) is an alarm that needs to be heard.

I am not a book critic, but I think this work can be as influential as Sapiens and therefor I need to correct something that is near and dear to my heart.  In chapter 10 Prof. Harari discusses the view of using blockchain to as a "technological check on such totalitarian tendencies" and goes on to describe why blockchain is not a good fit for this:  “In a blockchain system, decisions require the approval of 51 percent of users. That may sound democratic, but blockchain technology has a fatal flaw. The problem lies with the word “users.” If one person has ten accounts, she counts as ten users.”  The sources he references for this statement are legitimate, but are actually referring to voting systems built on top of blockchains - or as in the case for “Estonia—the Digital Republic Secured by Blockchain”, the [i-voting system](https://en.wikipedia.org/wiki/Electronic_voting_in_Estonia) is more accurately described as a secure digital voting infrastructure that incorporates some blockchain-inspired elements rather than being built on a specific blockchain platform.

He then shares a short story of Roman emperor Caracalla who murders his brother Geta and then attempts to erase him from history through some pretty extreme measures.  And also of Stalin who attempted to purge unfavorable facts from all historical records.  Using these stories he makes the statement “This degree of erasure demanded a huge manual effort. With blockchain, changing the past would be far easier. A government that controls 51 percent of users can disappear people from history at the press of a button.”

This is simply not true.

As a caveat to my following statements Prof. Harari does not state which blockchain(s) he is referring to in his examples.  His sources site several blockchain-like systems and private networks that could allow his statements to be correct.  But his conclusions about the "achilles heel" and the ease of erasure do not apply to nearly any modern decentralized public blockchain networks.  What Prof. Harari is referring to is what we would call a 51% attack and if such an attack were successful, then executing a finality-reversion - these are in effect two different issues.

In one of my other favorite books, "Read Write Own" by Chris Dixon, describes a 51% attack as something that:
> "...can disrupt transaction processing or enable attackers to “double spend” the same money in multiple places. These attacks are known as 51 percent attacks because their conspirators must gain control of more than half a system’s validators to be successful.  Feeble systems, like Ethereum Classic and Bitcoin SV, have succumbed to 51 percent attacks. Successfully attacking a major blockchain, like Bitcoin or Ethereum, would, in comparison, be so prohibitively costly as to be infeasible.”

To put that in context, to control the Ethereum network would require one to gain 51% of the stake which can be measured in Total Locked Value.  As of today (9/21/24) that would require you to hold over 20M Eth which would cost you upwards of $52B USD.  But this assumes the entity already controls that amount of stake.  If they had to acquire it, this would drive the cost significantly higher and it would be obvious what was going on.  In a public network things are, well, public... Part of the genius of blockchain is how the incentives are stacked such that it will cost you far more to attack then network then you could gain from corrupting it and that the community always has the ability to fork it away from you (of course this is much easier said than done).

Which leads me to Prof. Harari's second statement about erasure.  Erasing anything is never easy - even the historical examples he uses to make his point have survived erasure.  If one entity were to gain control of a networks they would only be able to manipulate the current state, and any future states while they have control.  A blockchain, by definition, does not allow you to rewrite previous states.  We call this "finality-reversion" and the deeper something is committed into the chain the more difficult this becomes.  To "erase someone" you would not only need to gain control, but you would need to convince the entire network (100%) to resync their validators back to the point that you wanted to change.  Nothing is impossible, but this is far more difficult than "pushing a button".

For what it's worth, the more likely risk of someone gaining 51% control is their ability to exclude, or censor, transactions on the network.  For this to be effective they need to maintain the "public trust" in the network while they quietly censor things out. This takes much coordination and stealth on behalf of the corrupt entity.  Back in [July at Eth CC Vitalik Buterin](https://cryptobriefing.com/ethereum-automated-response-plan/) discussed this exact topic. he shared a plan to for Ethereum validators to run software that could automatically prevent such things from happening.

---
I wanted to point this out not to poke holes in Prof. Harari's excellent work, but to strengthen the argument that blockchain is one of out best AI resistant technology.  It is not a silver bullet of course, and we need to design everything with caution, but if done correctly it can be the solid footing on which the truth of us humans can be distinguished from the truth of the AI.

<!-- BLOG_GIT_METADATA START -->

<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> 2024-09-23</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> 2025-09-19</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> 6</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">d4fa7182a93340cf...</code></p>
      
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
              <td style="padding: 0.25rem;">Enhanced landing page - added consistent catego...</td>
            </tr>
            <tr>
              <td style="padding: 0.25rem;">2025-09-19</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">Added the github "Content Provenance" onto each...</td>
            </tr>
            <tr>
              <td style="padding: 0.25rem;">2024-09-24</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">changed to prof. harari</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <p style="margin-top: 1rem; margin-bottom: 0;">
        <a href="https://github.com/zeroth-tech/blogs/blob/d8b1cb6671276034987e8ed4c379922236f926e8/docs/posts/Nexus_blockchain_counter.md" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
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
