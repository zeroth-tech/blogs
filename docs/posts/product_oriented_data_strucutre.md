---
authors:
  - jamescbury
date:
  created: 2023-08-20
draft: false
categories:
  - supply chain
tags:
  - tokenization
  - supply chain
comments: true
---
# Product-Oriented Data Structure
  
Where is most of the effort going to be for enterprises to get on board with product tokenization for track & trace?  It’s not the blockchain tech - while that part is cool, if we go with the assumption that any decentralized system worth building on needs to be open source and multi-purpose, it’s not going to be the enterprise’s role to develop or operate that network.  It is however the enterprise’s role to lay out clear business requirements that can be used to build modular software (building blocks) to achieve lofty traceability-related use cases.

<!-- more -->

No, the hard work for the enterprise is going to be in organizing their data and mapping their supply chain events into universally understood buckets.  The good news here is that this isn’t a new issue, standards for communicating between supply chain systems have been around for decades, the EPCIS standard and the acceding Core Business Vocabulary by GS1 is probably the most widely leveraged and for the most parts fits the needs.  My personal experience having implemented blockchain for supply chain solutions for over 5 years now, is that 80% of the effort is in extracting, transforming and loading (ETL) data on an on-going basis. The ‘on-going’ part also implies that enterprises understand the event triggers that start the ETL process that would feed the supply chain data into such a solution.

You might ask: Why is this so hard?  Haven’t enterprises been investing in better data structure for years?  What about my $20M data lake?  

My reply: Have you ever tried to pour a cup of water into a lake and then later scoop out that same cup of water?  Modern data architectures are designed for aggregation, not for granularity.

I blame it on the ERPs.  Enterprises have done everything they can to optimize their business processes, which often starts with the introduction of Enterprise Resource Planning systems (ERPs) and this focus on efficient process has generated a ‘process-oriented data structure’. It’s easy to see why. If you map out your manufacturing and distribution processes for just one plant, you can probably draw some pretty clear demarcations around which system is governing which part of the process - you likely have interfaces where one system hands off to the next.  If you look at how the data is structured within that process, it is generally geared towards records and logs - the data describes what happened over this time period within this process.

If you did the same exercise for multiple plants and distribution processes for the same time period and stacked the maps on top of each other (in a 1980s overhead projector style), you might even see how well they line up - but each individual flow is not necessarily connected to each other - you can actually see the data silos forming.  This is ultimately the result of process-oriented data structures.  Breaking it down properly to a more granular level is a complex matter of mapping and standardization.  An easier solution is to just dump all the data into one bucket - or if you have enough of it, into one large lake…  But now extend that flow out past the manufacturing and distribution that you control - when the data “belongs” to an entirely different set of systems (I.e., that of your customer, or your customers’ customer) the idea of capturing all of their data in your data lake is untenable.

## Enter the product world

In the real-world products behave differently than processes in the sense that if you follow a product “cradle to grave” you cross over several (sometimes many) different processes, and very rarely do any two products follow the same path.  I have written a lot about product tokens and the role that public blockchains will play in detangling this mess - that is a more in-depth discussion.  For the purposes of this post, I just want to focus on the product token as the common thread that connects data across an ecosystem as the product moves through its lifecycle.  If we wanted to be a little technical, you could think of the product token as the digital ID which represents a single product, and is the index against which all various databases containing information about that product can be queried.  Keeping consistent with our GS1 example above it’s easy to picture the product token ID as a Serialized Global Trade Identification Number (SGTIN).

Of course, it’s not as easy as just reindexing databases (as if that were even feasible); we need a mechanism to serve up data about any given product token from any database where it is stored and because this is trustless blockchain land, we want a mechanism to prove that the data has remained unchanged since the time the supply chain event occurred.  Let’s unpack that a bit…

For starters we will refer to product data as metadata - and this is simply to imply that there is a dataset separate of any other information that enshrines everything a process-oriented data structure knows about a given product.  Depending on your use case there are endless “standards” of what data should be included and what format it needs to take., IMHO this will never end, there will always be some new piece of information that is critical to know about a product so that something different can happen somewhere way down the supply chain.  The point is metadata will not be statically defined, and enterprises will need data governance for product data in and of itself.

The second point is product metadata will not all live in one place. - As a product goes from production to consumption it crosses many governing systems, each of those systems may add some information to the product metadata, but it’s very unlikely that they will ever write that data back to the initial repository.  I like to picture this as a trail of breadcrumbs that a product leaves, but the product itself is the key to linking all the breadcrumbs.

It’s worth noting that I do believe decentralized data storage could be a very good answer to keeping product metadata aggregated and accessible when needed - but I don’t think we can assume everyone will be willing to do that. - it should always be the right of the data owner to deny access to the product data, and while there may be consequences to enacting that right, it should be available…

Whether each ecosystem partner maintains their own product metadata or you choose to use a decentralized solution, the enterprise will still need to produce the product metadata in the first place.  It has become common place for the metadata to be stored in a .json blob.  For those non-technical readers, this is just a structured data set consisting of a key value pair.  The key being the name of the data element (think field name or column header) and the value being the actual data.  Conveying both the key and the value every time may seem like additional overhead, but in the long run it solves sooo many issues by letting the metadata live independently of a fixed the database schema.

The other nice thing about using a .json blob is that we can create a hash of it (a one-way encryption, or a digital fingerprint) that can later be used to prove the metadata remained unchanged since the time it was posted.  I can also have a portion of the .json blob encrypted using a specific public key (say that of a government regulator) who could at a later date decrypt that section and see some information about the product that is available only to them, but have the confidence that it was there all along and has remained unaltered.

Just to reiterate the point.  A Product-Oriented Data Structure consists of a universal product identifier for a specific unique product (or batch of identical products) - this is the token ID - and a series of .json blobs containing data specific to that product and likely stored in several different databases managed by different members of the ecosystem.  Leveraging the product token as the access mechanism for that data is a process that I call Token Claim Derived Authority (TCDA) which you can read all about in some of my other posts.
![diagram](<product_oriented_data_structure/Product Oriented Data Structure.png>)

## So what does this mean for the enterprise?

Over time I’m hopeful that ERPs will begin making it easy to generate a product-oriented data structure for individual products (some claim to do this today, but I think there is still work to do).  In the near-term this is the world of Extract Transform & Load (ETL) scripts, and these can be very tricky…. If you happen to be doing a supply chain transformation, and even if you don’t buy into any of the product tokenization stuff (yet) it still cannot hurt you to develop the product-oriented data structure and the governance processes needed to support it.  Worst case scenario is you begin using this method to archive your product data or transfer it to a buyer when you sell off the part of your business responsible for that product.   Best case scenario, is this becomes second nature to how you collect and store data, tying the data integrity of the product metadata directly to the physical product itself - in this way you begin to limit your liability of providing data on behalf of others in the ecosystem.

???+ info "A short tangent…"

    There is an interesting aspect that comes up when we assume that not everyone will play nicely…. Let’s look at a couple of cases:

    1. You buy materials from a supplier, but they don’t provide you product metadata, or the metadata they do provide is incomplete (I.e., you trust what they give you, but they don’t give you everything you need for your use case).  Here, you would need to fill in the gaps. We already do this all the time today, but we tend to do it at an aggregate-level, and we do it infrequently.  I would propose that enterprises develop a product data profile of what they would expect to receive and in which format (not a bad idea to share this with the supplier…).  Once enough data has been collected from different suppliers, then you can develop estimation formulas (this is one possible benefit of AI) that fill in the gaps for each new product you receive.  It’s really important in this scenario that those estimated data elements be flagged as such.

    2. You buy materials from a supplier, but they include fake data in their product metadata.  Let’s assume they do this maliciously because accidental mistakes should be easier to catch.  This is where the blockchain can hold someone accountable - if the supplier signs that metadata they are in effect attesting to its accuracy.  You as the buyer can definitively point to the source of the data as not being your own (let the legal updates to your purchasing agreements ensue…).  Further, if you have the estimation models from point 1 you can scan the metadata from each incoming product token and look for any outliers (this is why the accidents will be easier to catch).  If over time things look too good to be true, they probably are…. To that point it’s not a bad idea to put something dynamic in the metadata so that your can detect copy/paste records.

Special thanks to my colleague Akhil Patil for some constructive feedback and many grammatical corrections :smiley:  
