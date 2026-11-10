---
title: Personal AI Assistant
description: A Mac-first working prototype that turns text, editable voice transcripts and images into connected Markdown records.
permalink: /projects/personal-ai-assistant/
lead: Turning everyday words, voice messages, and images into connected, editable personal records.
summary: A Mac-first working prototype that turns text, voice messages, and images into linked Markdown records—with retained sources, corrections, and Undo.
status: In development
context_label: Platforms
context: macOS first; iOS prototype
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
  <p>The app captures text, editable voice transcripts, and images, then connects the resulting notes in a user-selected Markdown/Obsidian vault. The native interface provides ways to explore people, events, goals, and the moments linking them.</p>
</section>

<p><a href="/personal-ai-assistant/">Try the Capture demo</a> — an interactive illustration with fictional example data.</p>

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
    <div><h3>Ordinary files, native interfaces</h3><p>Records currently remain Markdown in a user-selected vault, compatible with Obsidian. An app-owned library is planned. Mac and iOS builds share capture logic and SwiftUI features, with platform-specific input where needed.</p></div>
  </div>
</section>

<section class="project-status-note" aria-labelledby="status-title">
  <h2 id="status-title">Where it is now</h2>
  <p>A Mac-first working native prototype, developed with AI-assisted coding and automated regression checks. An iPhone/iPad build exists but is not released or fully tested. Device-specific capture, cross-device behaviour, and Calendar/Reminders integrations are still being validated.</p>
  <p>Local Qwen text Capture and Local chat work on the Mac. Photos still use cloud interpretation, so the app is not yet fully offline.</p>
</section>
