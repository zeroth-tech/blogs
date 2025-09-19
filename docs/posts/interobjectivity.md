---
authors:
  - jamescbury
date:
  created: 2024-05-10
  updated: 2024-05-20
draft: false
categories:
  - Supply Chain
tags:
  - autonomous worlds
  - supply chain
comments: true
---

# Interobjectivity... ?

I love a good buzz word, especially one that sounds smart; could this be a new narrative that helps us express our intents in a digital world?  In exploring where this came from it helped me crystalize my understating of the difference between rules and laws in autonomous virtual worlds.  Even though that sounds like a stretch, this is gong to effect the way we do things in the real world sooner rather than later.

<!-- more -->

Let me share with you a fun little rabbit hole I jumped into the other weekend around "Interobjectivity".  This peaked my interest after hearing the word thrown around on a couple of podcasts and me realizing that my assumed definition based on the context clues of how it was used was conflicted.  Because "interobjective" kind of sounds like "interoperable" I had assumed it meant some sort of common ground where multiple *objectives* could be met with minimal trade-offs.  Turns out that is not correct, but it's not completely wrong either.  Into the hole we go...

First of all the word interobjectivity is a very rarely used outside of social sciences, and there seem to be several formal definitions of it.  From my limited research, the word first popped up in 1996 by the French philosopher [Bruno Latour](https://en.wikipedia.org/wiki/Bruno_Latour)  His paper “On Interobjectivity”[^1].  Which is a fascinating foray into the mating habits of baboons and a drawn out example of him talking through a metal grate in order to buy postage stamps.  But within the 20 pages of philosophical prose there is a theorem there - humans (unlike other species) have a special kind of relationship with objects, we can use them to execute our intent even when we are not around.  Latour uses an example of a shepherd that builds a fence.  Previously the shepherd would need to constantly roam around and herd his sheep to keep them in position, now instead of the shepherd needing to interact with the sheep directly the fence does it for him and he can take a nap.   The relationship between the shepherd and the fence is interobjective, because of the fence's permanence it allows the shepherd to extend his influence on the actions of others (in this case the sheep) even while he is asleep, or (depending on how well he built the fence) long after he is gone.

Oddly enough, though the paper is titled "On Interobjectivity" Latour does not actually define the term (or perhaps he did in the original French)... Later a grad student contributing to the "Human Geography Knowledge Base" gave interobjectivity the definition of: "the common world of experience and meaning which is shared by groups of people *and* objects. "[^2]

There is a 2016 book "On the Existance of Digital Objects"[^3] where Bernard Stiegler contributed a chaper "The Time of Technical Systems" where he uses the word *interobjectivity* in the context of information systems - I've ordered the book and added it to my summer reading list. The most official publicly available definition I could find was in the Encyclopedia of Critical Psychology and states that "The concept of interobjectivity has been introduced and developed in the social sciences to account for the non-conscious engagement in the course of social interaction that occurs within a social field that is phenomenally objective for subjects and that includes interactions with objects." [^4] A full write up of this definition can be found [here.](https://www.um.edu.mt/library/oar/bitstream/123456789/82869/1/Interobjectivity_2014.pdf) This probably makes sense to psychologists, but was a little murky for me.  Though it is pretty clear that the root of the word (objective) is referring to being able to sense something physical.

Unfortunately I don't think the existing definition extends very well into how we've been trying to use the word in the crypto space - which is mostly digital.  When I think of Latour's paper the part that sticks with me was the ability to use objects to express intent and the lasting effect that it has on others to convey that intent.  The shepherd intended for the sheep to stay corralled, in his mind he made a rule stating “thou sheep shall not pass” and he built a fence to enforce that rule.  Therefore my layman's definition of interobjectivity would be “the way a human can use a non-human object to express their intent to other humans".  Or given the state of technology today perhaps a more apt definition is "the way an *intelligence* can use a non-intelligent object to express their intent to other intelligences".

This flows nicely from the definition of intersubjectivity which is a word and has been well defined and discussed in many sociology journals. The short definition is "the intersection or relation between the cognitive perspectives of individuals".  Interobjectivity places an object in between the individuals.

!!! info
    Recently intersubjectivity made an appearance in crypto circles in EigenLayer's white paper describing the EIGEN token as an “intersubjective work token” basically saying that you can post some EIGEN as a bond to do some work that isn’t particularly easy to measure. Later, if two or more reasonable people agree that you didn’t do said work, you can lose your bond.  Thus widening the aperture of what a work token can be used for the current objective measures.

    *This really has nothing to do with what we are discussing here, but it is an interesting reference.*

To stretch this into the digital we need to take the leap that objects are not just physical things.  In a pure coincidence of words, developers have been using "object-oriented" programming languages since the 60's for their ability to encapsulate code and extend functionality. So instead of the shepherd building a physical fence, a game developer could create an instance of an object class of fence and give it attributes such as height and length.  When a digital sheep encountered such an object it would be programmed to take some action such as turn around.  Whenever someone is playing that game the developer's intent conveys by the attributes of the object they define and how that object interacts with other objects within the game.

But now the slope gets slippery... Intent is a difficult thing, if someone needs to interpret your intent it is by nature subjective and we are trying to build an interobjective world.  In the physical world intent often differs from the outcome, or causes unintended outcomes.  While the fence may keep the sheep in, it also might keep others out. In software development we do our best to be explicit with expressing intent in the form well defined requirements, but even this gets tricky because of unintended outcomes or the vast array of interactions with other objects.  The best way to avoid slipping down the slope is to use a language that is explicit and universal where all possible outcomes are deterministic - such as math.

!!! Note "Autonomous Worlds:"
    Here we are going to take a bit of a shift into digital or virtual worlds.  I'm not talking about the metaverse, I'm referring to worlds as an all encompassing container.  Back in 2022 [ludens](https://twitter.com/l_udens) started writing about "Autonomous Worlds" as fully on-chain rulesets in the [0xparc.org blog](https://0xparc.org/blog/autonomous-worlds) and later went on to build entire frameworks and toolsets for creating virtual worlds on-chain with [Lattice](https://lattice.xyz/).  In the spirit of standing on shoulders - many of the concepts I discuss below have been more fully fleshed out by the Lattice team (I'm a big fan of their work).

## Expressing Intent: Rules vs. Laws

In the physical world the transition from expressing intent to getting others to take a specific action is a matter of how well the object is designed and applied.  If the shepherd used a piece of string to corral the sheep, it is a weak form of expression, if he built a 10 foot wall it’s a strong form.  But even the strongest wall can be breached if you had really determined sheep… though this is drifting away from our interobjective rant a bit, it’s important to note that we don’t always need a physical or digital object to express intent, we can simply create a rule and enforce it through some sort of social construct or norm.  In fact we often need to do this to account for weak forms of interobjective expression when strong forms are not practical.  The shepherd could hang a sign on the string fence to let the sheep know we don’t want them to cross… and we could decide to strengthen the rule by making it a law and apply stiff penalties if violated. But alas, rules and laws are made to be broken (and most sheep can't read)...

But not all laws can be broken… we live in a universe that is bound by physical or natural laws.  These are concise descriptions of natural phenomena that have existed long before us humans and will likely be intact long after we are gone.  Through the scientific process we have observed and tested these descriptions and to the best of our knowledge they cannot be broken.  These include constants like the speed of light, or the gravitational constant, but concise descriptions are often formulas that relate these constants to other things we can measure like $E=MC^2$.  Because we don't know a reality where these constants don't exist we take them for granted and in many cases don't even recognize them - but they are always there.  The existence of natural laws shape our reality, they become our basis for establishing truth *and there is an inherent belief that they will continue to operate in the same way in the future.* My kid tried to ignore gravity once - that didn't end well... I doubt he's going to try that again.

I find it interesting that in the study of physics the most concise way to describe a natural phenomena is through the use of a mathematical formula.  Math is the universal language and can be both explicit and deterministic.  There is a popular saying in crypto that "code is law" and as catchy as this saying is, if we want to apply it to natural laws as opposed to social norms we need to add a few conditions.

## Establishing Natural Laws in an Interobjective Autonomous World

I was playing Minecraft with my son the other day and there were a few blocks of land suspended in the air.  It felt weird because I'm used to real-world physical laws, but that is how the developers designed the game - only certain blocks fall.  Accepting that reality is a kind of informal player contract that I agree to when playing the game.  Part of the fun is experimenting and discovering just what you can and can't do.  But it's only fun because Minecraft's physics are deterministic - once you understand the parameters they operate the same way all the time.  Sure there is randomness in how the worlds are laid out, but there is no randomness in how each block interoperates with each other.  If sometimes blocks fell up, and sometimes blocks fell down or some just randomly vanished, the game play would be completely different - it would be very frustrating...

!!! IMPORTANT
    Interobjectivity relies on natural laws in a digital world, and those laws must be deterministic

Deterministic natural laws set the foundation for how the digital world operates, they form the basis for that informal player contract which is elected into each time you play.  Their consistency allows players to make predictions about how their actions will effect the world and will effect other players or will allow a player to use an object to express their intent to other players.  If the world is to have some permanence (i.e., your actions effect others even when you are not playing) it is reliance on the natural laws that create an interobjective experience.

Being deterministic also implies that things are rigid.  The art of designing a good game rests in finding the right balance between deterministic laws and rules which players opt into.

!!! IMPORTANT
    Deterministic laws should be simple and basic - if done well they aren't even noticeable.

What's not fun in Minecraft is when you've been grinding away for hours looking for diamonds and your kid turns on creative mode when your not around just to fills up his inventory.  The ability to turn on creative mode (unlimited inventory) or peaceful mode (you can't get killed) can add a lot to the experience, but when one or just a few people have "God-Mode" powers it really disincentives other players.  Just like in real life, changing the rules should not be arbitrary and requires some form of governance.

!!! IMPORTANT
    Rules and laws are different.  Rules can be changed and require governance; laws are immutable.

But both the law and the rules are just code running on some computer.  One cannot claim to have immutable code if they control the hardware and the technology stack - if the game is contained within a world that runs on a computer (which might be running multiple worlds), then whoever can turn off the computer has God-Mode over the universe!  Right now the majority of all digital worlds run on servers that are controlled by just a handful of enterprises.  It's easy to "trust" them when the stakes are low but they are most certainly looking out for their own interests (and the interests of their share holders).  Chris Dixon points this out in his fantastic book "Read, Write, Own". [^5] He says the only way to prevent this is through protocol networks, or more specifically by thinking of blockchains as virtual world computers *(not to be confused with individual computers running virtual worlds)*.  The "protocols" enforce the natural laws of the network across a vast array of computers (I.e., nodes in a decentralized network), it becomes very, very hard to break them.  There is no Universal-God-Mode only coordination among node operators.

The other point that Dixon repeatedly makes (and I think is the most important aspect of blockchain in the context of interobjective autonomous worlds) is the unique ability of blockchain to make grantees about future execution of rules - only in a decentralized blockchain can you know that the laws and rules that exist today today will run the same way tomorrow - which makes them uniquely suited for enforcing natural laws.  In the context of interobjectivity this cannot be understated.  In the physical world I can build a fence to keep the sheep in, and I know that because the sheep can't defy gravity they are going to be bound by the fence.  In my digital world I need a guarantee that gravity is going to remain constant if I'm to use the same concept of an object (the fence) to control the sheep.

And it's not just constants (which are the parameters) it's the actual execution of the math.  Different computers do math differently - mostly because of the difficulty in handling floating-point precision and various short cuts that computers can take to perform frequently used functions.  If you are looking for another rabbits hole to jump into, [this old reddit thread](https://www.reddit.com/r/askscience/comments/1oqxfr/how_do_computers_do_math/) is pretty fascinating.  Most of the time these differences are minute, but they can stack up.  Well designed blockchains execute on a wide array of hardware and software clients so there are always multiple nodes "checking the math".

!!! abstract "Interobjective Autonomous World needs 3 things:"
    1. A set of deterministic natural laws enforced via protocols

    2. A set of rules that can be opted into by players and maintained through governance

    3. Guarantees about the consistency in future execution of 1 & 2

## A Physical World Bound by Virtual Laws'...'

I usually write about supply chains and enterprise blockchain use cases.  So far this rant has been about obscure sociology papers and video games… is there a connection?

Yeah, absolutely.  We shouldn't be surprised that gamers are leading the charge in pushing the role of networks for global coordination.  This could be another long post on it's own, but I think it comes down to the fact that we willingly suspend our concept of reality and accept the laws and rules defined by the game designers when we choose to play a game.   In the "real-world" game of supply chain (for example) it's not that easy.  There was no mastermind in designing global trade routes, there is no God-mode that can override the laws of nature, we are lucky if we can agree upon a governance structure for enforcing our man-made rules!  The reality is that enterprises exist in silos today and are primarily responsible for keeping their own house in order.  In some ways enterprise systems are like individual worlds that are trying to coordinate with other worlds, but there are no deterministic protocol level rules that give them a foundation to build on.  So every "object" they create to express their intent (a contract, a data standard, a packet of business logic) needs to be completely replicated in the other worlds.  And there is no guarantee that those other worlds will A) do it right in the first place, or B) continue to do it right in the future - so we have to jump through all kinds of hoops to "prove" our systems to each other.  

>**supplier:** "I built a fence that keeps the sheep in.  It's 4.54 ft tall and surrounds 1.26 acres"
>
>**customer:** "ok, I'll build the exact same fence, but I can only go to 1 decimal place so its 4.5 ft tall and 1.3 acres"
>
>**supplier:** "hmm... well that's not exactly the same.  Lets just keep checking to see if the sheep can get out"
>
>**customer:**  "sounds good, I'll go hire an auditor"

Think about how different global supply chain would be if for certain business transactions the settlement was occurring in an interobjective autonomous world?  The areas of friction could be eliminated because the double checking that needed to occur between systems (or that requires an intermediary) could be eliminated.

Just to be clear - I am not proposing a global platform (just the thought of that gives me an upset stomach).  For all the reasons stated above this does not work if there is a God-Mode.  What we is a way to break down business transactions into a series of deterministic natural laws and use a blockchain (or multiple blockchains) to execute those laws the same way for everyone for all time.  Participants can opt-in or opt-out for higher level "rules" which help manage their specific supply chains, but they can't break the laws.

!!! Tip
    **Example Supply Chain Law:** If I have custody over 10 units of inventory I can only transfer custody of 10, or fewer, units of inventory.
    **Example Supply Chain Rule:** If I want to destroy a unit I must have both custody and ownership of the unit.

Both rules and laws are deterministic and can be described mathematically.  This is the subject of our supply chain work over at Zeroth.Technology.  We are working on a method to allow for confidential settlements with embedded rights for physical products leveraging protocol networks.

## Tying It All Back Together

The notion of interobjectivity is exciting in the context of autonomous worlds, but it requires some work. In the physical world we use objects to express our intent with various degrees of permanence, but even these need the support of societal norms and governance to be effective in the long run.  Applying this to the digital realm in a trustable, sustainable way challenges the underpinnings of existing networks and systems but is completely doable with well designed  blockchains that can execute deterministic laws at the protocol level and allow for better governance around participation rules..  

## References

[^1]: Latour, B. (1996), On interobjectivity. In: Mind, culture and activity. Volume 3, number 4. Retrieved from Scribd.com, Friday May 31st 2024. <https://www.scribd.com/document/277023110/Bruno-Latour-On-interobjectivity-Mind-Culture-and-Activity-1996>
[^2]: Hui, Y. (2016). The Time of Technical Systems. In On the Existence of Digital Objects (pp. 151-186). University of Minnesota Press. https://doi.org/10.5749/minnesota/9780816698905.003.0005
[^3]: Human Geography Knowledge Base. (2012). Interobjectivity. Retrieved June 10, 2024, from https://geography.ruhosting.nl/geography/index.php?title=Interobjectivity
[^4]: Sammut, G., Moghaddam, F. (2014). Interobjectivity. In: Teo, T. (eds) Encyclopedia of Critical Psychology. Springer, New York, NY. <https://doi.org/10.1007/978-1-4614-5583-7_158>
[^5]: **Dixon, Chris.** Read Write Own: Building the Next Era of the Internet_. Random House Publishing Group, 2024.

<!-- BLOG_GIT_METADATA START -->

<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> 2024-06-15</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> 2025-09-19</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> 7</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">78d39d14b0135524...</code></p>
      
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
              <td style="padding: 0.25rem;">Added the github "Content Provenance" onto each...</td>
            </tr>
            <tr>
              <td style="padding: 0.25rem;">2024-06-21</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">Update interobjectivity.md</td>
            </tr>
            <tr>
              <td style="padding: 0.25rem;">2024-06-15</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">added a bunch of old blogs...</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <p style="margin-top: 1rem; margin-bottom: 0;">
        <a href="https://github.com/zeroth-tech/blogs/blob/ec5c1a2c349fc4ab14165cffc3542996b70b2911/docs/posts/interobjectivity.md" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
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

