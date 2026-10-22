---
title: Personal AI Assistant
description: A native Mac and iPhone assistant that turns text, dictated speech and images into connected, editable Obsidian records.
permalink: /projects/personal-ai-assistant/
lead: Turning everyday words, voice messages, and images into connected, editable personal records.
summary: A native Mac and iPhone assistant that turns text, voice messages, and images into linked Obsidian records—with retained sources, corrections, and Undo.
status: In development
context_label: Platforms
context: macOS & iOS
stack: Swift, SwiftUI
featured: true
featured_order: 1
showcase: assistant
image: /assets/personal/assistant-explore.webp
social_image: /assets/personal/assistant-thumb.webp
thumbnail: /assets/personal/assistant-thumb.webp
thumbnail_class: assistant-thumbnail
thumbnail_alt: Connections between fictional personal records in the assistant’s People view
image_width: 600
image_height: 390
---
<section aria-labelledby="why-title">
  <h2 id="why-title">A thought is easy to capture.<br>Making it useful takes more work.</h2>
  <p>A conversation, a plan, a meal, an idea: everyday information rarely arrives neatly organised. This project starts with a simple question—can an assistant turn that input into useful records while keeping the original context?</p>
  <p>The app captures text, dictated speech, and images, then connects the resulting notes in a user-controlled Obsidian vault. The native interface provides ways to explore people, events, goals, and the moments linking them.</p>
</section>

<section aria-labelledby="approach-title">
  <h2 id="approach-title">Capture, connect, and stay in control</h2>
  <ol class="capture-flow">
    <li><strong>Capture</strong><span>Keep the original words or image.</span></li>
    <li><strong>Check</strong><span>Validate the proposed records against their source.</span></li>
    <li><strong>Connect</strong><span>Save linked Markdown records in the vault.</span></li>
    <li><strong>Correct</strong><span>Edit the result or undo the capture.</span></li>
  </ol>
  <p>The engineering work centres on the boundary between interpretation and action: what did the input actually say, what can safely be inferred, and what should remain unresolved?</p>
</section>

<section aria-labelledby="decisions-title">
  <h2 id="decisions-title">A few decisions that matter</h2>
  <div class="decision-list">
    <div><h3>The source stays with the record</h3><p>Original inputs are retained in History. Evidence checks help constrain dates, events, and measured values to what the source supports.</p></div>
    <div><h3>Automation should be reversible</h3><p>Duplicate checks, staged saves, corrections, and edit-aware Undo help protect the vault when interpretation fails or a record changes later.</p></div>
    <div><h3>Ordinary files, native interfaces</h3><p>The records remain Markdown in an Obsidian vault. Mac and iPhone interfaces share capture logic and SwiftUI features, with platform-specific input where needed.</p></div>
  </div>
</section>

<section class="project-status-note" aria-labelledby="status-title">
  <h2 id="status-title">Where it is now</h2>
  <p>A working native prototype, developed with AI-assisted coding and automated regression checks. Device-specific capture, cross-device behaviour, and Calendar/Reminders integrations are still being validated.</p>
  <p>Interpretation currently uses a model provider. Local model experiments are exploratory; this is not yet a fully offline assistant.</p>
</section>
