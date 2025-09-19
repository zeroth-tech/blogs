---
authors:
  - jamescbury
date:
  created: 2024-12-12
draft: false
categories:
  - Agentic AI Research
tags:
  - process modeling
  - robotic process automation
  - personal AI agents
  - enterprise AI agents
comments: true
---
# Are Enterprise AI Agents just RPA rebranded?

There’s nothing new under the sun… If 20 years of technology consulting has taught me anything, it’s that a good story can be retold forever.  Sometimes we just need to update it with the current buzz words or fit it to current the narrative for it to seem relevant.  Today’s narrative of choice, of course, is AI.  We hear a lot about how enterprise AI agents are going to revolutionize corporate organizations, but when I ask people how, it sounds a lot like the same old story.  

<!-- more -->

 >"First we will find areas of high friction, high cost, or highly repetitive/error prone work.  Then we will model out the process and build an AI agent that can do it for us, but the AI agent will do it better."

In 2018 we would have said "robotic process automation" instead of "AI agent".  In 2002 we might have said "ERP", in 1980 we would have said "computer system".

Just for context, I studied industrial engineering in college, then for a solid five years within my career at EY, I focused on Business Process Modeling and Automation (BPMA).  I moved on to blockchain before we started calling it Robotic Process Automation (RPA) which sounds much cooler.  I always viewed this type of work as the systematic breakdown of a process into it's functions and a way to define business rules that govern those functions.  Once we do that we can use some software to essentially duct tape those functions together in a way that made more sense.  Prior to BPMA I wrote *a lot* of Excel macros to pretty much do the same thing.  

RPA, BPMA, Excel Macros... they were all a ways to bridge the gaps between disconnected processes and the underlying systems that governed them.  When things were too broken we would rip out and rebuild the underlying system (ERP implementation) - but it was usually easier to apply bandaids.

If we are not careful Enterprise AI Agents are going to do the same thing over again.  I'm quite certain there are some consulting firms dusting off their old RPA pitch decks as I write this.

## we can do better... right?
It doesn't have to be a repeat of our favorite episode. AI Agents are different, or at least they can be.

I think a lot about what an "AI Agent" actually is; I haven't quite made my mind up yet.  I'm about 50% through the excellent book "Making Sense of Chaos" by J. Doyne Farmer.[1]  Usually I like to finish a book before commenting on it, but I think some of his work is very relevant for this topic. The first few chapters gave me an appreciation for the role of "agents" in modeling complexity economics and introduces the concept of "bounded rationality".  I think that Farmer's "agents" are a close approximation of what "AI Agents" really are.  Except that his agents run within models that operate in controlled environments, are trained on carefully curated data, and simulate the outcome of various scenarios that are used to help humans make better choices in the the real world.  I feel like AI Agents (at least the ones most of us can get exposure to) are getting trained on socially curated datasets (x, telegram, discord, websites in general) which have the convenient effect of telling us what we want to hear, or what we can observe as a trend, but isn't necessarily true.  Now that the tools for launching agents have become widely available (I was playing with virtuals.io(https://virtuals.io) over the weekend) we are taking an "f* around and find out approach" as opposed to Farmers more disciplined and scientific method.

Farmers book also re-enforces one of my observations about traditional process improvement: We make the assumption that business processes are deterministic.  The minute you draw a process map or a decision tree you are defining a set of valid end states and making the assumption that rational actors will always cause the process to end in a valid end state, if that doesn't occur then the model was wrong --> go back to your brown paper lined conference room and start drawing on the walls again (ahh the memories...).   Farmer's work points out the limiting effect that the "assumption of equilibrium" has had on traditional economic models. And how a few simple heuristics, the use of boundaries instead of rules, reenforcement learning, and a bit of randomness can generate very accurate predictions of future events.  

## which way do we go?
This brings me to why I think we are at an inflection point, where agents which were previously the in the realm of data science and predictive analytics are beginning to interact with **the real world**.  I have deep concerns with this, because the "social data" that these agents are being trained on is in fact generated, or influenced by other agents.  I will try not to turn this post into that particular rant, but suffice it to say self-fulfilling feedback loops are dangerous.

To keep it practical (at least in my optimistic opinion) this should be the goal of AI Agents:

1. The agent should have a straight forward objective and a time horizon on which they should achieve it.
2. The agent should have a world model that lets them understand what is going on in context of their objective.
3. We should provide boundaries to keep the agent from making harmful mistakes.
4. The agent should make predictions based on their world model and learn from their mistakes.
5. Finally, we should give them *agency to act* on those predictions in efforts to achieve their objectives *within their boundaries*. 

Much easier said than done I know...  This is just a rehash of the classic AI alignment problem.  I am also resisting the urge to include Asimov's laws of robotics (the zeroth law for which my company is named after).  The only reason I mention these is that I think enterprises are going to choke on that last part. 

## maybe this would work, if not for the humans.
Having grown up in an audit and accounting firm I can appreciate the extent of effort that companies go through in order to maintain control - giving agency to a model (even if it is tightly controlled) is not in their DNA.  But don't worry we've already came up with a cute solution - we will always keep a "human in the loop".  This however has many flaws which all boil down to the fact that humans are, well, human.  Interestingly enough, this is one way to introduce bounded rationality into a deterministic model... but I don't think that is the intent.

Rationality of humans aside, the issue with this approach that I want to draw attention to is the bottleneck it will create.  In my limited experience of building and interacting with AI agents it is their relentless focus on their objectives that I am most impressed with (I am not surprised by this, after all they are programmed to be that way) but impressed to see it in action.  A favorite Einstein quote of mine is "it's not that I'm so smart, I just stay with problems longer".  Concentration and focus, coupled with access to knowledge, is powerful indeed.  Even if AI Agents are not efficient, or if their training is flawed, they can trial and error their way to a desired result far faster than we can because of their relentless 24/7 focus - putting a human in the loop takes away that advantage.

We used to say that a well designed controls were like breaks on a car.  A car with brakes can get from point A to point B much faster and more reliably than one without them.  The shortened version was that "breaks let the car go faster".  Human in the loop is not a break, it is speed limiter that can cut your throttle when you need it most.

In traditional process modeling "human in the loop" was usually referred to a "procedural control" meaning it wasn't programable logic, but was left to the discretion of the operator to what they thought best - there were rules of course, but someone had to decide to follow them (or break them).  This is what gave process models the flexibility to adapt when the unexpected occurred.

If we just let AI Agents run business processes that we've already defined (traditional process modeling with some AI pixie dust sprinkled on top) we will probably get the same results we got every other time we tried to do this.  "Continuing to do exactly what you have done in the past is exactly good enough to get you exactly where you are" (that's another one of my favorite consulting phrases).

## a pivot and a proposal
Of course I hate long posts that complain about a problem and don't offer any tangible solutions, so here is my latest - only partially tested out - thinking...

Large enterprises will not have the stomach to let AI Agents represent them in any meaningful way like the social AI agents that are currently taking over X.  They will not be given "agency" to do much other than advise management what to do (this time it's "leadership in the loop"... even worse!).  As excited as I am, as a start up, about using AI marketing agents this is not going to fly for large companies who already have a brand.  Their customers are their most valuable asset, they are not likely going to give that up (though every time I have to "chat with an online representative" about my wireless bill it makes me think otherwise...)

So I see two paths:  Personal AI Engagement and Employee Productivity

### 1) Personal AI Agent engagement
>Where a corporation should be hesitant to let an AI agent represent them to their customers, customers will jump at the chance to let AI agents represent them to their providers (the corporates).  If I could ask my Personal AI Agent (PAIA) to interact with my cellular provider and get an explanation as to why I'm being charged for the equipment I returned months ago, I would do it in a heartbeat!  PAIAs are going to be the next wave of "customers" that enterprises need to market to.  Corporations have spent decades marketing to humans, humans with short attention spans and who lack relentless focus on objectives.  Their PAIAs won't care if "there is an unusually high wait time" or if they need to try 50 different coupon codes before they get one that isn't expired; they won't forget to cancel after that 3 week free trial is up either.  But that's just the easy stuff... the PAIA will try to negotiate with providers over *everything*, and they will be willing to agree to more complex terms and conditions (which they will actually read) than the typical consumer - *and they will follow through with their end of the bargin and hold you to yours*

> Enterprises need to be ready to negotiate back!  But you won't be able to do this through a customer service chatbot... you will need a "counter PAIA" that has the objective of an optimal outcome for both you and your customer.  The enterprise won't advertise this (or at least they don't have to) but they need to make it the first thing that a PAIA interacts with.  Over time, I believe, those enterprises that do this well will build up a reputation within the PAIA networks and will find ways to capitalize on that.

> This is a world in which personal AI agents abstract away all the tedious, frustrating, onerous activities that us humans waste our time on today.... I like that world.

### 2) Enterprise AI Agents to increase employee productivity
>Another way to think of this is "Enterprise AI Agents to Decrease Employee Frustration".  This is a similar line of thought as the personal AI agents above, but with more of a focus on how the employee operates within the organization.  Where RPA set out to duct tape systems together and automate "procedural controls" it only made the lives of *some* employees easier. 

>An Employee AI Agent (EAIA) would share in the responsibilities of the employee.  It would have all the same access to all the same systems that the employee does and over time it would likely have the same decision making authority.  I would be surprised if enterprises aren't training these agents by analyzing employee network activity, emails etc.  Now that nearly all our conference calls are recorded, there isn't much left to complete the "data set" of what an employee actually does.  Don't bother fighting this, in time it will seem perfectly normal...

## where does this leave us humans?
And I guess this brings me to the point of writing all these words... bare with me for a few more, I will get there I promise... 

We are already living in two different worlds - the physical world where our meat bag bodies have been evolving for thousands of years and the digital world which has unfolded in the last few decades.  Our physical world is complicated, it is governed by rules we can't control (natural laws); it is very difficult to get to the bottom of everything - I personally am very bad at fusing atoms; and the things we value are a complex mix of emotions, experience, environment, and probably some randomness. But the digital world is more definitive, in fact we can boil it down to two precise elements: 1 and 0 (at least until quantum throws a wrench into things).  At the very bottom of everything in our digital world are bits - and more importantly the combination of those bits that make data.  Data is created, exchanged, transformed, and deleted.  Humans interact with their data via computers and over the years we've built increasingly complex systems and networks to help us interact with and control our data.  In the early days system design was dominated by the business process and resource management.  Today our system design is dominated by the User Experience (UX).  Tomorrow our system design will be dominated by AI Experience (AIX).  Our PAIAs and our EAIAs will be our interface to our data.  This will have a profound impact on computer systems as we know them.  

For starters all of the complexity we've created to optimize the UX or the business process will become irrelevant.  At first that EAIAs will take a page out of the RPA playbook and help to bridge the gap across multiple disparate systems.  But it won't belong before they will bypass the systems and just interact with the rule sets and the data.  Which brings up the second important point.

Blockchains are good for this (come on you knew I would go there...).  We need networks that can enforce rules which are very hard to break in order to settle the state of our data.  It doesn't matter if that data is representing an asset in the real world (like nearly every other post I written here) or if it is a photograph of your dog.  Who's data it is and what can be done with it needs to be clearly defined and controlled.  We don't have this level of control often today because it's very hard, but either our PAIAs or our EAIAs will abstract the complexity and inefficiencies away from of our control systems to make this level of granular data contol common practice.  Our systems will devolve into rulesets that the AIs are asked to adhere to while trying to achieve their objectives which (hopefully) are aligned with our intent.  The AIs will take care of connecting all the dots and the humans will provide the "bounded rationality" and the "lil-bit-o-randomenss" needed to make the digital world evolve.

## thanks for reading, I'll shut up now
Ok, that was a bit heavy and a tad dystopian, but I don't think it's a far stretch.  And at the rate we are advancing technology this could be here before we know it.  To bring this post to a conclusion and answer the question we set out to discuss.  Are Enterprise AI Agents (EAIAs) just Robotic Process Automation (RPA) rebranded?  Sure - they could be, and in many cases probably will, but not necessarily. At least I gave you a few new acronyms to include in your deck...

If you were wondering what Zeroth Technology is doing about all this, we're working on it.  We see this push as the convergence of our three pillars - Zeroth Agents, Zeroth Attest, and Zeroth Settlement Solutions.  With Zeroth Agents we are helping enterprise prepare their internal rule sets (typically buried in procedual documentation) to help interact with both EAIAs and their customers PAIAs.  Zeroth Attest is launching the Vero device to help distinguish between a real human and an imposter.  And Zeroth Settlement Solutions is working to use blockchains to settle object state in a way that is both trusted and confidential.

## Bibliography

[1] Farmer, J. D. (2023). Making Sense of Chaos: The Modeling Revolution in Economics. Little, Brown Spark.

<!-- BLOG_GIT_METADATA START -->

<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> 2024-12-12</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> 2025-09-19</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> 4</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">4529d47a89f97364...</code></p>
      
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
              <td style="padding: 0.25rem;">2024-12-13</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">title change</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <p style="margin-top: 1rem; margin-bottom: 0;">
        <a href="https://github.com/zeroth-tech/blogs/blob/d8b1cb6671276034987e8ed4c379922236f926e8/docs/posts/enterprise_AI_agents_vs_RPA.md" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
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




