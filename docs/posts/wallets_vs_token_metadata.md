---
authors:
  - jamescbury
date:
  created: 2023-06-15
draft: False
categories:
  - Supply Chain
tags:
  - tokenization
  - supply chain
comments: true
---
# Wallets vs. Token Metadata

With product tokens we generate a bread crumb trail of metadata that is specific to a given product.  In combination with the minting, transferring, and burning of claims on that token the metadata rounds out the full record of the products lineage and data.

<!-- more -->

The way it works is an individual (a person or an entities) who has a claim on a token (I.e., the token is currently mapped to their wallet address in the latest state of the network) can post a transaction referencing the token id and typically including a CID or some other pointer in the transactions URL.  The CID is a hash of the content of the metadata set and (if using IPFS) is also used to locate the metadata.  Posting the hash on-chain is one way that we later prove the data was not changed.

Currently we think of metadata sets by use case, for example - I want to produce a “digital product passport” so i need the metadata to contain certain data elements required within the DPP.  If I want to use the token as collateral for a loan I need to include certain metadata that details the attributes necessary to assess the value of the asset. There may even be several different metadata sets signed by the by the same wallet to against the same token at the same time to support multiple use cases.

!!! Question
    Maybe we need a universal identifier at the top of a metadata set indicating what schema it is following in support of which use case - kind of like a multihash

But sometimes we need to return information about the wallet that is holding the product token, and not just the product token.  For example if I am a manufacturer minting tokens for each product I produce and my wallet is registered to the physical establishment of my manufacturing plant.  There may be additional information about that establishment that I want refrenceable by each token it produces - such as address or facility name.  I may even hold a credential in my wallet stating that this establishment of licensed to produce this product for a given time period.

In these cases it would not make sense to repost wallet level metadata each time a new set of product level metadata is signed. It would be better to simply be able to retrieve the wallet level metadata when querying the product token.  So the way this would work for say a digital product passport is that the end consumer would use TCDA to access the metadata about a given token for a given transaction.  It would also look to see if there were wallet level metadata that was applicable at the time of the transaction and return that as well.  

Of course this adds a layer that f complexity in that the wallet level data is relevant to product level data only at a specific point in time.  If the wallet level data is updated there needs to be some version control to roll it back.

But this approach unlocks another capability through the use of verified credentials.  We want the ability to have a VC issued to a wallet by a trusted institution that qualifies the wallet to do something.  This implies that when an end consumer is accessing metadata using TCDA they would be able to return the VC data as well - so having wallet level data (maybe held on a VC of sorts) is not really any additional work and carries with it the efficiency on only posting wallet level data once.

Can we place a soul bound nft in a wallet that has establishment level  - could this be a credential?  This would remove a ton of duplicate metadata from the token.  If you change wallets later the old tokens would be mapped to the old wallet. Data availability might be an issue.

<!-- BLOG_GIT_METADATA START -->

<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> 2024-06-15</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> 2025-09-19</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> 3</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">5d954b279b7b3e0c...</code></p>
      
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
              <td style="padding: 0.25rem;">fixed tags</td>
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
        <a href="https://github.com/zeroth-tech/blogs/blob/d8b1cb6671276034987e8ed4c379922236f926e8/docs/posts/wallets_vs_token_metadata.md" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
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

