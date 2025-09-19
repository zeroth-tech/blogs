
# Welcome to the Zeroth Technology blog space

This is where we share our latest thinking, rants, and some ramblings... it's also the archive for everything we've been talking about for years.

Our work spans three key areas of research and development:

<div class="landing-buttons">
  <a href="category/agentic-ai-research/" class="landing-button pyrana-button">
    <div class="button-icon">
      <img src="images/pyrana.svg" alt="Pyrana" class="custom-icon">
    </div>
    <div class="button-content">
      <h2>Agentic AI (Pyrana)</h2>
      <p>AI agents, context engineering, and intelligent systems</p>
    </div>
  </a>
  
  <a href="category/identity-authenticity/" class="landing-button vero-button">
    <div class="button-icon">
      <img src="images/vero.svg" alt="Vero" class="custom-icon">
    </div>
    <div class="button-content">
      <h2>Identity & Authenticity (Vero)</h2>
      <p>Digital identity, attestation, and trust systems</p>
    </div>
  </a>
  
  <a href="category/supply-chain/" class="landing-button supply-button">
    <div class="button-icon">
      <img src="images/cser-icon.svg" alt="Supply Chain" class="custom-icon">
    </div>
    <div class="button-content">
      <h2>Supply Chain & Tokenization</h2>
      <p>Supply chain transparency and tokenization systems</p>
    </div>
  </a>
</div>

---

<div class="page-break-text">
  <p>Scroll down for a complete listing of all blogs.</p>
</div>

<style>
.landing-buttons {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
  margin: 2rem 0;
  max-width: 1000px;
}

@media (min-width: 768px) {
  .landing-buttons {
    grid-template-columns: 1fr 1fr 1fr;
  }
}

.landing-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.5rem;
  border-radius: 8px;
  color: inherit;
  text-decoration: none;
  transition: all 0.2s ease;
  border: 2px solid #3399ff;
  background: var(--md-default-bg-color);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.landing-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  text-decoration: none;
}

.pyrana-button:hover {
  border-color: #ed7445;
  box-shadow: 0 4px 12px rgba(237, 116, 69, 0.2);
}

.vero-button:hover {
  border-color: #3399ff;
  box-shadow: 0 4px 12px rgba(51, 153, 255, 0.2);
}

.supply-button:hover {
  border-color: #4caf50;
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.2);
}

.button-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.custom-icon {
  height: 70px;
  width: 70px;
  object-fit: contain;
}

.pyrana-button .custom-icon,
.vero-button .custom-icon {
  height: 117px;
  width: 117px;
}

.button-content h2 {
  margin: 0 0 0.5rem 0;
  font-size: 1.1rem;
  font-weight: 600;
  text-align: center;
  color: var(--md-default-fg-color);
}

.button-content p {
  margin: 0;
  font-size: 0.9rem;
  text-align: center;
  color: var(--md-default-fg-color--light);
  line-height: 1.4;
}

[data-md-color-scheme="slate"] .landing-button {
  background: var(--md-default-bg-color);
  border-color: #3399ff;
}

.page-break-text {
  text-align: center;
  margin: 2rem 0;
}

.page-break-text p {
  font-size: 0.9rem;
  color: var(--md-default-fg-color--light);
  font-style: italic;
  margin: 0;
}
</style>