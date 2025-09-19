---
authors:
  - jamescbury
date:
  created: 2024-03-30
draft: false
categories:
  - Supply Chain
tags:
  - tokenization
  - supply chain
comments: true
---
# Why hasn’t blockchain solved our supply chain issues yet?

This is a drum I’ve been beating for many years now - In my opinion using decentralized networks to create trusted and controlled visibility into the supply chains that literally affect the lives of billions of people every day is inevitable; but we are not there yet…. In this post I summarize my latest thinking on the topic.
<!-- more -->

It’s hard to believe it was almost 4 years ago when COVID-19 was declared a pandemic by the World Health Organization.  I can remember hearing the horrible news stories about how despite the heroic efforts of our healthcare providers thousands of people were dying because they couldn’t get access to life saving medicines and medical devices - the hospitals didn’t even have enough personal protective equipment to keep our doctors and nurses safe.  The reality of an inadequate supply chain was a major contributor the largest public health crisis of our generation.  It affected all of us - I’m pretty sure my family is still using the toilet paper we stock piled during the pandemic…

COVID put a spotlight on a systemic pervasive issue with our pharmaceutical supply chain - but the issue is far from new.  Back in 2013 the US FDA passed the Drug Supply Chain Safety Act (DSCSA) which put into law requirements around track-and-trace; given the rapid “digitization” of supply chain this the mandate should have been pretty easy - it’s just a matter of data standards and interfaces right? 10 years later only portions of DSCSA are even enforceable...  This is not due to lack of effort! Tremendous strides have been made in untangling a decades old, complex, multi-tiered supply chain.  It’s just that these attempts have fallen short.

I will admit that this post is a bit lengthy and opinionated, but I think that in order to appreciate the magnitude of change that is needed we have to dig a bit deeper into root cause.

## **Addressing the problem: *how supply chains got this way…***

The public health issues due to “lack of transparency” in pharmaceutical supply chain have been documented and discussed at length in recent years. The fact that many government agencies are still citing “Supply chain visibility, monitoring, and data sharing processes and platforms” as a topic that requires research and innovation is conviction enough that current approaches are not working.  To be clear, it is not for lack of approaches, many software platforms solve this issue quite well, it is lack of adoption that prevents them from scaling; but I would argue that **lack of adoption is driven by poor approach**.  Any solution that is counting on pressure from business partners or regulators to drive it’s acceptance is approaching the issue from a point of compliance and is incentivizing participation via the “stick” vs. the “carrot”- they will never be sustainable.

For the purposes of this post I would rather frame the question of “why did it get like this” as opposed to “how bad is the issue”, because in understanding the why we can perhaps identify the core changes that are needed to correct the problem.  This will result (I hope) in a series of foundational methods/techniques that work well all of the time (”always get the little things right”) and transcend any particular system or platform.

So here we go from the ground up… fundamentally **supply chain is the exchange of assets in return for payment.** As complex as our supply chains can be today, they all revolve around facilitating this basic transaction.  The “chain” part of supply chain implies that it is a series of transactions that are required to produce and distribute a product.  At the edges of a supply chain the exchange of the physical good and payment can take place simultaneously.

Think about a farmer selling a harvested wheat crop to a granary on one end of the supply supply spectrum and a hungry person buying a loaf of bread at a bakery - and lets assume these are both cash transactions paid on the spot with no returns for simplicity sake.  This is a simple example of settlement - meaning that one good (wheat or bread) was exchanged for another (money) and there are no residual commitments; the transaction was settled, we are both in agreement with the outcome, lets move on…  But as we work our way either downstream or upstream from the ends of the supply chain the quantities of product and the aggregate amounts paid for them begin to increase dramatically (the value of all the grain in the granary is far greater than the value of the individual harvest - the value of all the flour at the bakery is much higher than the price of one loaf of bread) and this aggregation / disaggregation gives rise to a split in the fundamental transaction.  

If the granary is able to sell their entire stock to a miller it is very unlikely they will be paid the moment the grain leaves their silos, the miller will may only want to pay upon receipt and inspection of the grain; and even then they may ask for a delay in payment (I had a client once who demanded 120 day payment terms!).  As soon as this happens the exchange of the product and the payment are no longer asynchronous – there is a separation between the financial ownership and the physical custody.  This results in two interrelated, but separate transactions that require settlement, and this seemingly small rift allows for a vast complexity of buying and selling arrangements.  This should be intuitive to the reader - there is noting new in this centuries old process, but what is interesting is how we evolved systems to address this.  Lynn Aldren’s recent book “Broken Money” does a fantastic job of explaining the monetary side of this evolution.

But on the supply chain side we should look more closely at the computer systems in manufacturing enterprises.  They were used for financial accounting long before they were used for managing inventory.  As manufacturers required more supplies, they developed procurement processes to facilitate purchasing and to manage their costs.  On the other side of the house as customers purchased more products, they developed sales processes to manage their revenues - the monetary system was (and still is) the primary driver of their development.  Inventory management was (and mostly still is) an input or output of procurement and sales.  ERPs developed to bridge this gap (Enterprise Resource Planning where the resource is many forms of capital - materials, human, knowledge, money, etc) to **create efficiencies within the individual organization, but not across organizations**.  Granted if the organization is big enough it may seem like the ERP is controlling an entire supply chain, but it is always internally focused in the end - **the jurisdiction of the ERP stops at the boundaries of the enterprise**.  But supply chain by definition is bigger than any one enterprise so to make this process more efficient they developed ways to connect their procurement and sales systems with their suppliers and customers.  If those supplier and customers happen to be running the same ERP software this is a bit easier (much to the software providers benefit), and although the proliferation of standard Application Programming Interfaces (APIs) and data standards have made things much better as well, it is still complex and clunky - and in some cases completely broken.  Yet these procurement and sales based interfaces are the best we have and we rely on them today to connect our incredibly complex supply chains.

All of that is to say that, **interfaces between trading partners exist for the primary purpose of settling payments, the transfer of physical inventory is not usually settled, it is just an input or an output** *(IMO this isn’t a bad thing - a single ERP or system can never/should never govern an entire supply chain).*

In addition to the maintenance, complexity, and reconciliation challenges inherent in this web of interfaces (I like the term API spaghetti) there is another nuanced issue.  **Payments are fungible where inventory is not**.  If company A pays company B $6 US dollars for a product, that $6 is (eventually) debited from company A and credited to company B.  There is no requirement (or reason) to determine if company B used that same $6, or a fraction of it, to buy something from company C.  But this is not the case for inventory, even if the individual units of inventory themselves are interchangeable (i.e., one screw in a box of 100) they are identifiable at some level – unit, lot/batch, product, etc.).  So, to transfer this type of knowledge between trading partners the EDI 867 Product Transfer and Resale Report was designed explicitly to pass along product information.  And there is a bit of handshake between the trading partners if they use a corresponding EDI 997 Functional Acknowledgment to show the EDI was received and in good format - but that receipt does not guarantee that the inventory was moved out of one system and into another we still have to rely on a separate system of checks and controls to keep the information in the digital records in sync with the physical movements of inventory.  This manifests itself in the form of something like this:

>Seller: “Upon shipment of *x* units of product *y* in relation to order *z,* I will debit *x* units of product *y* from my inventory system”
>Buyer: “Upon receipt of *x* units of product *y* in relation to order *z,* I will credit *x* units of product *y* to my inventory system (in which I may or may not refer to this product as product *y*)

These statements are only made for the sake of the buyers’ and sellers’ internal inventory management systems which they use for their internal planning.  They are only as strong as their internal processes and controls - **they are not settlements**. Further, just as with the payment, the history of transfers related to that particular product is not inherently tied to the product record, it is buried in the paper trail of the procurement process - and that paper trail usually breaks each time the product is transferred.

The core issue at the bottom of all of this is the lack of a way to “settle inventory transfers” and a way to “log and share a history of those transfers” between trading partners.

### **Past and current attempts to solve (and why they aren’t working)**

Of course, the above description is over generalized and as I mentioned these are not new issues; there are many solutions either available or under development that aim to address inventory settlement - often rolled up into solutions for “supply chain visibility” or “track-and-trace” in response to the current description of the problem.  

Lets also establish up front the fact that **inventory settlements between training partners are confidential transactions**.  Meaning that anyone not involved in the transaction should not be able to infer any information about it.  It might be OK for it to be known that two entities are trading partners (in pharma we have the concept of Authorized Trading Partners already established) but **which products, how many, and how often are trade secrets**.  If a competitor were able to get that information there would be many opportunities to arbitrage the supply chain.

I find that all current solutions fall into one of 3 categories:

1) **Direct peer to peer connections:** These are interfaces that arose from procurement processes and are built and maintained by trading partners that pass information about their product from one system to another through some mutually agreed upon protocol and data standard. These have benefitted greatly over time through better use of Application Programming Interfaces (APIs) and data standards that have developed out of necessity from organizations like [IEEE](https://www.ieee.org/) and [GS1](https://www.gs1us.org/), as well as the EDI standards referenced above. In a multi-tiered supply chain, many peer-to-peer interfaces will need to be “stitched together” to form the complete linage of a given product.

**Primary Benefits:**

- Only requires the coordination of two parties (the buyer and the seller) for any one interface.
- The information exchanged between them is relatively easy to secure (i.e., their transactions are confidential)

**Primary Drawbacks:**

- Difficult to scale, a buyer or seller may need to develop and support *many* discrete interfaces.
- Multiple interfaces often result in significant master data management issues and requires reconciliations and mappings.
- Product data does not “inherently pull-through” when the same product is exchanged multiple times.

2) **Private/consortia-controlled platforms or networks:** A centralized solution that serves as a coordinator, and in some cases a governor for the supply chain. Often referred to as a “control tower” these solutions work well when trading partners can agree upon a common trusted intermediary.

**Primary Benefits:**

- Creates a high level of regulatory control over certain industries.
- Transactions *can* be kept confidential between trading partners and the trusted intermediary.

**Primary Drawbacks:**

- Often only provide value when at scale and can be very difficult/expensive to establish.
- Inevitably lead to the centralization of risk and control and are inherently bureaucratic.
- Typically focus on solving one pervasive industry issue – not generally composable with other solutions/business models which lead to limited business value.
- For large multinational organizations or for industries with many small participants and a few large ones these create a barrier to entry.

3) **Public networks:** Attempts to leverage large open networks (primarily blockchains) for supply chain use cases. It is necessary to leverage networks that support code/rule execution within the network (e.g., smart contracts)

**Primary Benefits:**

- Can leverage blockchains for what they are good for (global coordination and management of digital scarcity)
- The “common ledger” eliminates reconciliation issues between systems and the transaction history lets the data “pull through” with a high level of integrity.
- Unique tokens can be used to represent products and track simultaneous claims on them (i.e., ownership vs. custody)

**Primary Drawbacks:**

- Public networks are, well, public… enforcing the confidential nature of transactions as described above often leads to solutions that are built on top of the public network, and those solutions fall into category 1 or 2.
- By their nature the smart contracts (and their business logic within) that would govern supply chain use cases are also public.

There is yet another issue inherent to our current state that is often pervasive across all three of the categories above:  Because we don’t actually settle inventory transactions **most solutions attempt to recreate the paper trail of our current or legacy supply chain systems.**  In this way they leverage the type of data that is already exchanged in a peer-to-peer interface (this is often the easiest source of data to tap into).  As discussed, those systems are designed around the procurement process and digitize documents such as Sales Orders, Purchase Orders, Advanced Shipping Notifications, Bill of Ladings, Goods Receipts, and Invoices; each of **these documents make a *reference* to the product and quantity being transferred** (among other procurement data such as price and payment terms), **but not all of them represent specific claims on the actual product**.  

In the pharmaceutical supply chain, an additional level of detail can be included in the documents which lists the specific serial numbers that are being transferred.  But even if the data in the documents are 100% accurate because the buyer and the seller operate on two different systems this doesn’t equate to settlement - again, **there is no programmatic guarantee that the inventory is debited from one system and credited to another**; while this might be achievable between a small ecosystem of trading partners it is impossible to achieve at scale without leveraging category 2 or category 3 solutions above because trading partners manage inventory on separate books.

### **A new foundational approach to settle inventory transactions is needed**

If instead of focusing on “recreating the procurement paper trail” in a digital fashion we were to focus on a way to fundamentally settle inventory transactions we might be able to build a better mouse trap.  

This starts by thinking about the relationship between supply chain participants (I.e., one side of the trading partners used throughout this post), their products (the asset), and events that occurs at a point in time - the who, what, when (where, why and how are also very important but not as pertinent to the settlement - EPCIS 2.0 does a great job explaining these factors).  That relationship can be described as a “claim” and for any given product there may be multiple claims held my multiple participants and any point in time.

The most common example of claims are ownership and custody.  If your friend borrows your car you are still the owner, but your friend has custody.  Same car, different claim claims.  Further if you happen to lease the car from a bank, then the bank has a claim on the car as well, in the form of a lien.  As the owner you have the right to sell your car, but the bank can impair your right to sell if you don’t clear the lien first, just like your friend can impair your ability to sell if they don’t give it back (or if they wreck it…). There are several different types of claims that describe the rights a participant has on a product, and it is not a standard set - “claims” are a construct that can be defined per product class as and have “claim rules” that describe how those claims effect one another.

Settling an inventory transaction is in effect settling a claim - or rather creating a shared state that maps the claims to participants for a given product at a point in time.  Changes to this state over time in the form of a claim-state log become the history of who, what, and when.  If we also add in the ability for a claim holder to attest to a piece of information about a product then we can round out the where, why, and how components. Basic rules like “a claim for a given product can only be held by one participant at a time” or “you must hold a claim in order to transfer it” can enforce the settlement.  

The last component that is needed is a way to traverse the claims-state log forward and backward for a given product.  This would give us the “track-and-trace” components that we have been seeking, and if we were able to limit that ability to only those participants who hold (or have held in the past) claims on that product we would preserve the confidential nature of the supply chain.  A technique like this would be a method for Confidential Transactions with Embedded Rights (CSER) and is a public good that Zeroth Technology is looking to create for the world.

<!-- BLOG_GIT_METADATA START -->

<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> 2024-06-15</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> 2025-09-19</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> 2</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">a642a55821c2d18c...</code></p>
      
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
              <td style="padding: 0.25rem;">2024-06-15</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">added a bunch of old blogs...</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <p style="margin-top: 1rem; margin-bottom: 0;">
        <a href="https://github.com/zeroth-tech/blogs/blob/d8b1cb6671276034987e8ed4c379922236f926e8/docs/posts/why_isnt_supply_chain_fixed_yet.md" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
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

