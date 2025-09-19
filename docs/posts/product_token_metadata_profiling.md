---
authors:
  - jamescbury
date:
  created: 2023-10-18
draft: false
categories:
  - Supply Chain
tags:
  - tokenization
  - supply chain
  - machine learning
comments: true
---

# Product Token Metadata Profiling

Often the topic of AI regarding blockchain comes up, often the topic is misguided…

A blockchain is not a learning system, it is not intelligent (smart contracts aren’t even that smart…).  It’s more akin to a data historian, a network that maintains a state, and a record of all previous states.  It does not adapt on its own or self optimize - if it did it would undermine the trusted execution.

<!-- more -->

There are a couple of places where AI and blockchain do meet, I’m sure I’m missing a few here, but these are top-of-mind:

1) Attribution: as far as we know today the robots are not smart enough to crack our private key encryption and sign fraudulent transactions - so taking a piece of data and notarizing it on chain is a good way of attributing that data to a source.  If we also mix in a verified credential, the wallet that signed the data can carry some certification or reputation.  When training machine learning models this level of attribution will be increasingly important to avoid bias or to have a “provably legitimate” training data set.
2) Data profiling:  personally I think this one is much more interesting.  We are envisioning a world where product tokens are accompanied by multiple .json blobs of data specific to that token.  The rest of this post builds off of this idea.

If I am manufacturing a product - say a bottle of water - it’s likely that I will have several different sets of metadata about that product each for different use cases.  For example I may have metadata about the source of the water.  I may have metadata about the global trade information. I may have metadata about the carbon footprint (though that should be captured in an allocated carbon token), I might even have metadata on the label or instructions for use (imagine that… how to use this water…).

Even though all of this metadata is originating from the manufacturer it’s likely that it will be in different .json blob.  The schema of the .json will typically be determined by the use case, common schemas will be needed for interoperability.  If I want to do a source of origin use case for all bottled water, I will need to get some alignment on what data is required for source of origin and in what format am I expecting it.  We cannot fool ourselves that there will ever be a universal data standard for anything, try as we might.

This is where the Machine Learning comes into play.  For any given use case there are a handful of data standards defined by one or more standards bodies.  Those templates can be fed to the algorithm.  Then for each use case specific metadata blob signed to a token that you have a claim on (read that sentence carefully) the algorithm can determine how closely the metadata fits into a known standard. If we switch from ML to AI the algorithm might even be able to do the mapping and fill in any gaps.  At a minimum it should work to catch any abnormalities, at best it should give you real-time feedback on how well your metadata tracks with similar metadata sets.

There are two places that you can run this particular scan - the first being prior to signing the metadata, in which case you can include some level of certification into your signature that the metadata meets some set of requirements or standard (you could even have an audit firm do this for you #newbusinessopportuny).  Or you could profile the data after it has been posted, this is the more likely approach when you are receiving a product token that already has metadata signed to it by another party and you want some level of verification as to the legitimacy of the data; remember that signed data is always attributable back to the signing address, but the the actual data itself can be what ever the signer wants it to be (though once it is sighed we can always tell if it is changed after the fact.)

One last rabbit's hole to jump down here is the possibility of using a zero knowledge proof to profile the metadata before signature - while this is a really intriguing concept it will carry a certain amount of overhead since generating a proof is computationally heavy, and it may provide limited benefit since the metadata is maintained off chain. But the basic premise goes:

1) write a zk circuit that defines the metadata schema including the field names and data types.
2) add any additional data logic rules that might apply on a per element basis (I.e., if a quantity is entered a UOM is required, or only values within a range)
3) Sign the metadata, and ost the roof on-chain making it easy for a third party to verify without actually looking at the data.
An alternative to this is to simply register a schema via EAS and reference that you leveraged that schema in your metadata, though here you loose the data verification checks.  Currently attesting under EAS exposes the data but perhaps doing that under privacy, or in conjunction with a 3rd party will be in the future.

<!-- BLOG_GIT_METADATA START -->

<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> 2024-06-15</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> 2025-09-19</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> 4</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">fc055712c350678a...</code></p>
      
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
        <a href="https://github.com/zeroth-tech/blogs/blob/ec5c1a2c349fc4ab14165cffc3542996b70b2911/docs/posts/product_token_metadata_profiling.md" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
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

