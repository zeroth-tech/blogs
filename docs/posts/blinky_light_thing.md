---
authors:
  - jamescbury
  - ankmister
  - patmac
date:
  created: 2024-07-04
draft: true
categories:
  - Identity & Authenticity
tags:
  - live streaming
comments: true
---
# The Blinky Light Thing

The objective of the Blinky Light Thing *(that's the technical term)* is to embed proof that audio and video content is both authentic and contemporaneous with the time at which it is being recorded by introducing elements into the physical environment that are very difficult replicate and are captured by the original recording devices (i.e., camera + microphone).  The intention of BLT is to supply a low-tech solution that is not dependent on specific hardware/software and is easily (and freely) verifiable.

<!-- more -->

## What's the problem with live-streaming video?

It's hard to know what's real these days.  We've all seen deep fake video and CGI actors in the movies.  The ability for humans to detect authentic audio and/or video content from generative content just by "eyeballing" it is rapidly diminishing.  But this is no surprise, and it's not an new issue.  Ever since digital distribution of media became popular in the 80's - 90's we have been introducing more and more sophisticated ways of trying to prove something is authentic - pretty much all of these approaches boil down to some form of watermarking.

Watermarking is a way to imbed something unique into the video and audio components of digital media.  Sometimes they are noticeable by the audience (like a floating tag in a video) and sometimes they are not (like extra embedded data in an audio file).  But **they are almost always something added to the file after it has been created by the presenter** and is then **verified before sharing with the audience**.  Traditionally watermarking has been used to prove that content is authentic and officially licensed from the owning entity that produced it (i.e., not a pirated movie or album).  But when a presenter is addressing an audience directly to convey a specific message - such as Elon Musk discussing Tesla earnings with shareholders, or a witness giving a deposition in a court trial, or the US President addressing the nation - we want a different kind of authentic...

We want to know that what we are seeing and hearing is real - or more precisely that who we are seeing is in fact who we believe them to be, and what they are saying is in fact the words coming out of their mouth.  In many cases we also want to know that when they are saying it is contemporaneous when when the content was created.  That is to say if it is "live-streaming" we want to know that it is happening now.  If the content claimed to be pre-recorded we want to know that the recording date is consistent with what they state it is (consider the impact of back-dating a recorded prediction or a set of instructions such as a last will and testament).

To visualize this it's best to start with the mental model of how we handled all of this before digital content.  Ahh the good old days...

![Face_to_Face](./blinky_light_thing/face_to_face.drawio.svg)

When we are physically present the proof points above are ubiquitous.  The audience sees the presenter, so they know it's them (body doubles and undercover agent theories aside).  They can hear what is being said as the presenter is saying it.  Generally there is no doubt that the message is both authentic and contemporaneous.

In live-streaming we introduce quite a few more variables.  The whole point in live streaming is that the audience and the presenter do not need to be physically co-located.  There is actually a lot more that goes into this, but the most basic form would be something like the graphic below.

![Live_Streaming_Comm](./blinky_light_thing/web_streaming.drawio.svg)

There are of course many ways to secure the capture and distribution of live-streaming media. But they all require control points around hardware and/or network; and most of them require some trusted intermediary to "prove authenticity on your behalf" (just trust the broadcast network and watch their ads in return for them doing this service for you).  While this *may* be ok for large scale productions such as the US President addressing the nation, or live streaming sports, it almost never happens with small scale productions like an individual trying to make a personal statement "on the record".  Or, as has become more common, an individual trying to prove that their statement is **not a deep-fake**.  This post will not go into all the technological advances being made for producing live-streaming deep-fake video, but it's scary.  And just because the presenter says it's not a fake and the word *"LIVE"* is watermarked into the video doesn't cut it anymore.

## What to do about it?

BLT works by introducing detectable messages into the the physical environment where the content is being captured, thereby embedding the message into the raw audio and video of the content stream without relying on any of the capture and distribution infrastructure.  While the messages are detectable, we are going to great lengths to make them not distracting or necessarily apparent.   The light source "blinks" the encoded message and the audio source "chirps" the same message.  Included in the message is enough relevant information for the audience to determine how to decode it (i.e., convert the blinks and chirps back into the original message), but most likely this will be more easily done by the presenter sharing a QR code with the audience which will give them specific instructions.

![BLT_Highlevel](./blinky_light_thing/blinky_light_thing.drawio.svg)

## Design Principles

There are a couple of things necessary for BLT to scale.  

> 1) Mainly that the core concept is available for anyone to use and that messages are transmitted using as broad a standard as possible.  This means that the content of the message is available information to the audience, if the audience is unknown, then that information is publicly available.
>
> 2) The method for interpreting the received message must also be free for the audience to use and ideally there would be several software clients that could independently verify the same message.
>
> 3) The "authenticity" of the presenter (i.e., they are who they say they are) requires a form of digital identity.  There are both strong and weak forms of identity that can be leveraged.  
>
> 4) The presenter must make an "attestation" when beginning their broadcast session to generate the message and irrevocably tie it to their identity.
>
> 5) To prove contemporaneousness the attestation must include a time stamp from an unbiased, highly available, and secure network (i.e., the Ethereum blockchain) and that same network can be used include information that would be impossible for the presenter to know prior to their broadcast attestation.
>
>> 5a) Optionally the presenter can include a termination attestation and the end of their broadcast session which can later be used to verify the completeness of the broadcast.
>
> 6) The broadcast message will be blinked and chirped through out the broadcast session, for longer broadcasts it may be desirable to update the broadcast message periodically.
>
> 7) Because of network latency and unexpected physical environment changes (i.e., a drastic change in lighting or background noise) the broadcast message must be kept as brief as possible and include sufficient redundancy so that a completed message can be received by the audience. HOwever we must also consider the limitations of video transfer and design a message that can be transmitted using less than 30 frames per second.
>
> 8) The format for encoding the broadcast message into blinks and chirps must be widely known and easily verified.  

## What's in the message

 The encoded broadcast message contains the minimal amount of information required by the audience to verify the message.  By leveraging a blockchain service for attestations (specifically the Ethereum Attestation Services) the broadcast message can simply include a link to the broadcast initiation attestation on EAS.  The EAS attestation is an immutable record that is signed by the presenters private key (meaning that only the presenter can sign it).  By accessing the UID a viewer can verify who signed it and when.  The attestation also can carry some additional information such as the blink rate which is important to know for when trying to decode the message. The data included in the attestation is arbitrary and can follow any structured schema chosen by the presenter.  So long as the private key used to sign the attestation is provably tied to the presenter (this can even be done in a custodial manner) all that is needed to meet our proof points is the attestation UID as it is impossible to know before hand and references a timestamp that cannot be modified.

[example Attestation UID: 0x144fec63505680f8f0a6dee7e3b16f0f147715586aa0fe6e7ee65b940d23c570]

The Attestation UID is a 64 character hexidecimal string which represents 256 bits of information (each character is 4 bits). For video the limiter is the frame rate of the of the video feed which is generally a minimum of 30 frames per second (FPS).  For audio files a minimum sample rate (SR) should be twice the highest frequency in the audio signal (Nyquist theorem), so about 40 kHz.  Knowing these values we can calculate the length of time it takes to transmit the message.

**Minimum Video Message Duration (in seconds):**

  > Duration = $(\frac{1}{FPS})$ bits = $(\frac{1}{30})256$ = 8.533 seconds

**Minimum Audio Message Duration (in seconds):**

  > Duration = $(\frac{1}{SR})$ bits = $(\frac{1}{40})256$ = 6.4 seconds

However, we are transmitting sequential bits as either a 1 or a 0 (light on, light off...) and sequential bits of the same value (111000) do not show a detectable difference, so for this reason we need to include a blink rate as part of our message encoding.  Theoretically the blink rate just needs to be greater than the minimum message durations calculated above.  practically it needs to be about 5x longer to give ample time in detecting a state change.  We've been running tests at a blink rate of 0.2 seconds which gives us a message transmission rate of 51.2 seconds.

!!! NOTE
    In designing BLT we tried to account poor audio and video quality since the encoded message is passed via the media stream. At the beginning of a broadcast the presenter must share the configuration of their BLT - the decoder needs to know what color light it is looking for our which amplification frequency to tune into. We also intend for the presenter to share the UID - thus giving the viewer the encoded message it is seeking to verify.  This changes the approach from trying to decode an unknown message to trying to verify a known one and allows us to apply a probability to account for poor transmissions.  To give further redundance the blink rate and the chirp rate (which are the same) are purposely out of sequence so that if one bit is missed it can be inferred from the other stream.  Finally the BLT uses terminators at the beginning/end of each transmission consisting of three blinks from a different light source or three chirps at a different frequency.

## What's special about this?

Our intention is to not just overlay the Attestation UID on top of the raw audio and video files, the BLT imbeds it into the actual media by reflecting the blinking light source onto the face of the presenter, and amplifying their actual voice.  In this way any alterations to the video content after the broadcast, or post capture of the live stream (such as a filter) would obfuscate the encoded message making it indecipherable and hence invalid.  While BLT does require a blinking light and a chirper, we intentionally designed it to work with any camera/microphone to avoid the need for customized hardware.

### How do we make this not annoying?

In some cases the presenter may want both the blinking light and the audible chirp to be heard by the audience in a way that is not too distracting, but noticeable. Most likely they will want both forms of message transmission to be innocuous.  For the blinking light we accomplish this flooding the presenter with a strong white light (similar to a ring lamp or side lit LEDs that are common for web productions) but including the blinking LED in a specific color that becomes very obvious when a common video color correction filter is applied.  Specifically by creating an arbitrarily high gamma and hue for the video.  A similar audio filter is applied to detect the amplified sound waves from the audio transmission. In the end there may be a *tiny* bit of perceptible flickering or distortion to the audio or video file, but nothing noticeable.

### Live-stream Verification

In theory the attestation UID will have all the information needed for the viewer to verify the authenticity of the live stream, but this would require them to watch and listen to the video with a set of filters applied which amplify the encoded message.  Our intention is to have several open source verification tools available for *anyone* to be able to verify the media for free.  Zeroth Technology will offer one such tool as a browser based service for videos watched through our website.  Or as an extension for any videos watched through y our favorite browser.

### Post-stream Verification

We also designed BLT to let presenters prove the content was authentic even after they've completed their broadcast.  This is done by generating a closing attestation in EAS referencing the opening attestation. We are also working on a way to quickly generate a content hash of the raw audio/video file to include in the closing attestation.  From there we plan to leverage the C2PA manifest approach to prevent any further alterations.

### What if there are multiple people broadcasting

Our approach works well in scenarios where there are multiple presenters and audiences such as a virtual meeting.  In these scenarios one facilitator would create a session and generate a UID.  Each participant would reference that UID in their opening attestation linking the participant together.  Each participant is both a presenter and a viewer, so they will individually broadcast their messages while and generate a closing attestation when the session is complete.  Similarly the session facilitator can create a closing attestation that references all participating UIDs as well as a content hash for the entire session.

### BLT in a Closed Network

It's likely there are cases where the public attestation component of the BLT is not desirable (e.g., court hearings, private meetings, etc).  In these instances the presenter's identity can be established through traditional mechanisms by a third party and the the Attestation UID is created on their behalf.  There is an extra step here to encrypt the additional data that is included in the attestation and distributing a key to specific audience members so that they can decrypt that data for verification.  Assuming in this scenario the content distribution infrastructure is also controlled, these aspects can be integrated into the "log-in to the meeting" process.

## Why bother with this?

We think it's pretty obvious, but live streaming deep fakes is definitely going to be a thing. Does the BLT fix everything? absolutely not, but it's a step in the right direction.  Just like fake watermarks in produced media, digital authenticity is always a cat and mouse game.  We believe that by tying reputation (a.k.a digital identity) into on-chain attestation makes the best use of the tools that we currently have available.  We also think that sometimes to avoid technical vulnerabilities you need non-technical solutions.

To inspire fear, here are a couple of scenarios that will be likely within the next 12 months:

1) Proxy Speakers: People are very busy and value their time.  Many meetings and decisions might not require them to be present, but there is an expectation that they are.  Why not abdicate your say to someone you trust speak on your behalf, but instead of seeking approval for this just have them be a fake you... nobody has to know.
2) AI Speakers: Why try to find someone you trust - just have an AI that is trained to think, act, look and sound like you be your representative?  What could possibly go wrong.
3) Malicious Intent: Many of us are already pretty weary of trusting people over with personal information over the phone or in chats.  But hop on a video call and we get a pretty high level of comfort that we are speaking with someone legitimate.  Especially if they look and sound like you.  People are way more willing to give away private information to someone who "looks" like they are trying to help.

I could keep going, but it makes me depressed...

## Our vision

We need to start somewhere and Zeroth Technology is eager to do our part.  We don't have all the answers to this and we think it must evolve rapidly to stay a step ahead.  We look forward to community inputs to help us do a better job of face detection, noise filtering and color mixing.  We want to make a mobile version that is super simple to use and we want to have a host of independent verifying solutions.  

We don't think every live stream needs to be authenticated, but we need to have the tools ready for the ones that do.

<!-- BLOG_GIT_METADATA START -->

<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> 2024-07-08</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> 2024-07-08</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> 1</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">a4c5028d73f2c0b2...</code></p>
      
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
              <td style="padding: 0.25rem;">2024-07-08</td>
              <td style="padding: 0.25rem;">James Canterbury</td>
              <td style="padding: 0.25rem;">Uptated to BLT post</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <p style="margin-top: 1rem; margin-bottom: 0;">
        <a href="https://github.com/zeroth-tech/blogs/blob/b9419ce5299242a41df9572414a7e2e6dd8eecf8/docs/posts/blinky_light_thing.md" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
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

