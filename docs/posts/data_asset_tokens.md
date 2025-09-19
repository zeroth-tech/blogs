---
authors:
  - jamescbury
date:
  created: 2024-10-18
draft: false
categories:
  - Supply Chain
tags:
  - tokenization
  - supply chain
comments: true
---

# Data Asset Token vs. Product Token

I’ve recently been thinking a bit about data as an asset and the concept of data asset tokens.  Much of my thinking was influenced by [Michael Clark](https://www.linkedin.com/in/futureofmichael/) whom I had the pleasure of meeting at the recent Filecoin Uncharted event (thanks [Porter](https://www.linkedin.com/in/porterstowell/)).  This post is probably more about vocabulary than content, but vocabulary is important (at least that's what I tell my kids).

<!-- more -->

We talk a lot about the importance of owing our own data, but what does that really mean?  The concept of ownership has been defined and redefined 1000 times over, I try to ground myself in a simple view - ownership is one form of relationship between an entity and an object; a simple test of ownership is: if I own an object I can destroy the object.  The common word to describe this type of relationship is a ‘Right’ and (just to round out our vocabulary) when you want to declare that you have a right you are making a ‘Claim’.  Often we need to make a 'Claim' before we can evoke an action allowed to us by our 'Right'.

Of course the right of ownership also gives you the ability to assign other rights (custody, seizure, liens) either to yourself or to another entity; all these rights describe different relationships between entities and the object.  

If this sounds familiar, then thank you for reading my blogs… We have been trying to articulate the nuanced role of rights and claims against physical assets for years.  In supply chain we call the objects ‘products’ and some people call them ‘assets’.  In a network we represent them as ‘tokens’.

So when I heard the term ‘data asset token’ it made me think… could data be an object? Well of course we have object oriented programming (OOP), where we define a data structure to include the object's attributes or properties and we define the method (wether you call them functions or procedures) that dictate how that object behaves (I like to think of these as rules).  Central to OOP is the concept of encapsulation which lets us put a nice wrapper around the object, it's properties, and it's rules. At any point in time that encapsulated object has a state - but often this state is only valid within the application that enforces it's rules.  Blockchains have changed this by letting a protocol enforce the rules and thereby letting everyone trust the state.  But this starts to get a little wonky when we have states that change more rapidly than blocks being produced, or if that same object if governed by different rules over the course of it's lifecycle.

If we are dealing with a physical object we can visualize state, and state changes, as transitions while the object moves through its life cycle. Relative to most things digital, a physical object’s state changes very little.  Making, moving, and consuming products (minting, transferring, and burning tokens) happens in (mostly) discrete steps. And there are a finite number of “states” that we need to manage.

On the other hand natively digital data can change A LOT.  And they generally have poorly defined or amorphous states.  To even begin getting our heads around this we have to start thinking in terms of static and dynamic data.  And we also need to account for references and pointers… often the ‘data’ does not stand on its own - other data is needed to give it context.

So to treat data (like your personal medical records) as an object (that is to say tokenize it) we need a strong hierarchy and an understanding of context.  We also need a clear definition of what the token is supposed to do - if the token is a pointer to a dynamic data set then it’s really just a gateway.  If, as we tend to think of it in NFT land, the token contains a hash of the data - or is a CID like in IPFS, then the token is possibly a snapshot of the state at some point in time.  These are two very different things.

## a compromise

I would propose a blend of the above.  A token can be defined that represents the attributes of the data set - these being the characteristics that, if changed, you would have a different object.  On this ‘Data Token’ we can assign rights and manage claims like we do for physical product tokens.  We can combine data tokens by burning and minting like we do for raw materials consumption.  We can associate data by placing the tokens in the same wallet ([wallets as containers](https://zeroth-tech.github.io/blogs/2024/07/22/contract-wallets-as-containers/)). However, these tokens can also have a pointer to a dynamic data set that, at any point in time, is the state.  The claims one has on the data token define how (or if) they are able to access the referenced data.  We can get creative with how to manage the state of the referenced data, but I don’t think that needs to be over engineered - though we always need to consider that it is the responsibility of the data steward to make the referenced data available when a claim is proven… if they fail in that duty it doesn’t matter what rights you have, you can't get your data.  Unless everyone is willing to self custody their data (which is probably the worst idea I can think of…) data stewardship should be a service you pay for.  —> there is a reason I am a big fan of Filecoin and still hopeful for Eigen DA (not just because I run an EigenPod…)

In summary, I think the momentum is still gathering.  Data Asset Tokens offer much better control over data and a clear definition of rights - as well as a way to prove and/or transfer those rights in the form of claims.  When I write about supply chain I talk about the shift from process oriented data to product oriented data - perhaps we need to reframe that as a shift to asset oriented data or identity oriented data (though I’m still uncomfortable thinking of identity as an asset…)

<!-- BLOG_GIT_METADATA START -->

<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> 2024-11-01</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> 2025-09-19</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> 3</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">1d716422bbb8475a...</code></p>
      
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
              <td style="padding: 0.25rem;">2024-11-01</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">Update data_asset_tokens.md</td>
            </tr>
            <tr>
              <td style="padding: 0.25rem;">2024-11-01</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">posting data asset tokens blog and updates to BLT</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <p style="margin-top: 1rem; margin-bottom: 0;">
        <a href="https://github.com/zeroth-tech/blogs/blob/d8b1cb6671276034987e8ed4c379922236f926e8/docs/posts/data_asset_tokens.md" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
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

