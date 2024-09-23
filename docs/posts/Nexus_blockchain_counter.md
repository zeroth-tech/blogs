---
authors:
  - jamescbury
date:
  created: 2024-09-21
draft: false
categories:
  - Fundamentals
tags:
  - digital truth
comments: true
---

# Nexus: A counter argument to blockchain's "achilles heel"

Let me start this post by saying what a huge fan of Yuval Harari I am.  Sapiens is one of the most influential books I have ever read - it opened my mind to the concept of intersubjective reality and the power of the stories we tell  - how they can both rule our lives and make our species capable of great things.

I just finished reading Nexus and it too is a great work, I tell my friends that part 1 is a history lesson and admittedly a bit of a slog, but just as Dr. Harari does in Sapiens and Homo Deus his through historical perspective set the foundation for his later arguments.  Yes the book is a bit alarmist, but I don't think his algorithm instructed him to use outrage to sell copy... What he shares (in my opinion) is an alarm that needs to be heard.

I am not a book critic, but I think this work can be as influential as Sapiens and therefor I need to correct something that is near and dear to my heart.  In chapter 10 Dr. Harari discusses the view of using blockchain to as a "technological check on such totalitarian tendencies" and goes on to describe how blockchain lends itself to democracy but also has a fatal flaw:  “In a blockchain system, decisions require the approval of 51 percent of users. That may sound democratic, but blockchain technology has a fatal flaw. The problem lies with the word “users.” If one person has ten accounts, she counts as ten users.”  The sources he references for this statement are legitimate, but are actually referring to voting systems built on top of blockchains - or as in the case for “Estonia—the Digital Republic Secured by Blockchain”, the [i-voting system](https://en.wikipedia.org/wiki/Electronic_voting_in_Estonia) is more accurate to be described as a secure digital voting infrastructure that incorporates some blockchain-inspired elements rather than being built on a specific blockchain platform.

He then shares a short story of Roman emperor Caracalla who murders his brother Geta and then attempts to erase him from history through some pretty extreme measures.  And also of Stalin who purged would attempt to purge unfavorable facts from all historical records.  Using these stories he makes the statement “This degree of erasure demanded a huge manual effort. With blockchain, changing the past would be far easier. A government that controls 51 percent of users can disappear people from history at the press of a button.”

This is simply not true.

As a caveat to my following statements Dr. Harari does not state which blockchain(s) he is referring to in his examples.  His sources site several blockchain-like systems and private networks that could allow his statements to be correct.  But his conclusions about the "achilles heel" and the ease of erasure do not apply to nearly any modern decentralized public blockchain networks.  What Dr. Harari is referring to is what we would call a 51% attack and if such an attack were successful executing a finality-reversion - these are in effect two different attacks (though the latter requires the first).

In one of my other favorite books, "Read Write Own" by Chris Dixon, he states that:
> "A successful 51% attack can disrupt transaction processing or enable attackers to “double spend” the same money in multiple places. These attacks are known as 51 percent attacks because their conspirators must gain control of more than half a system’s validators to be successful.  Feeble systems, like Ethereum Classic and Bitcoin SV, have succumbed to 51 percent attacks. Successfully attacking a major blockchain, like Bitcoin or Ethereum, would, in comparison, be so prohibitively costly as to be infeasible.”

To put that in context, to control the Ethereum network would require one to gain 51% of the stake which can be measured in Total Locked Value.  As of today that would require you to hold over 20M Eth which would cost you upwards of $52B USD.  But this assumes the entity already controls that amount of stake.  If they had to acquire it would drive the cost significantly higher and it would be obvious what was going on.  In a public network things are, well, public... Part of the genius of blockchain is how the incentives are stacked such that it will cost you far more to attack then network then you could gain before honest people forked it away from you.

Which leads me to Dr. Harari's second statement about erasure.  Erasing anything is never easy - even the historical examples he uses to make his point have survived erasure.  If one entity were to gain control of a networks they would only be able to manipulate the current state, and any future states while they have control.  A blockchain, by definition, does not allow you to rewrite previous states.  We call this "finality-reversion" and the deeper something is committed into the chain the more difficult this becomes.  To "erase someone" you would not only need to gain control, but you would need to convince the entire network (100%) to resync their validators back to the point that you wanted to change.  Nothing is impossible, but this is far more difficult than "pushing a button" 

For what it's worth, the actual risk of someone gaining 51% control is their ability to exclude, or censor, transactions on the network.  For this to be effective they need to maintain the "public trust" in the network which would take much coordination and stealth on behalf of the corrupt entity.  This was recently discussed  back in [July at Eth CC by Vitalik Buterin](https://cryptobriefing.com/ethereum-automated-response-plan/) where he shared a plan to for Ethereum validators to run software that could automatically prevent such things from happening.

---
I wanted to point this out not to poke holes in Dr. Harari's excellent work, but to strengthen the argument that blockchain is one of out best AI resistant technology.  It is not a silver bullet of course, and we need to design everything with caution, but if done correctly it can be the solid footing on which the truth of us humans can be distinguished from the truth of the AI.