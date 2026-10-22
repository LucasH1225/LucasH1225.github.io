---
title: Wankai
description: A collaborative local multiplayer 3D combat prototype where weapon contact drives both movement and fighting.
permalink: /projects/wankai/
lead: A physics-driven fighting game where the weapon that hits your opponent also gets you across the arena.
summary: A local multiplayer 3D combat prototype where weapons also propel the characters. Custom physics brings movement, ground contact, and combat together.
status: Playable prototype
context_label: Play
context: Local multiplayer
stack: React, Three.js, Electron
role: "My recent contributions: playable characters, the preparation interface, and arena integration."
featured: true
featured_order: 3
image: /assets/personal/wankai-arena.webp
image_alt: Two animal fighters facing each other in Wankai's 3D Colosseum arena
image_width: 900
image_height: 531
image_caption: The local Colosseum arena. Visual and camera work continues alongside the playable prototype.
thumbnail_class: game-thumbnail
---

## One action, two purposes

In Wankai, moving and attacking are part of the same physical interaction. A player swings and turns a weapon; when it meets the ground, the contact can lift or propel the character. The next swing might be a way to reposition, land a hit or recover from a bad angle.

That shared mechanic makes the character's relationship with the ground important. There is no separate conventional movement control to hide behind. The game has to make force, contact and inertia readable enough for players to learn through experimentation.

## Making contact feel consistent

The prototype uses a custom fixed-timestep physics system rather than treating each swing as a canned animation. Constraints connect the character and weapon, while collision handling supports ground contact, hits and blocks. Weapon geometry affects reach, turning and contact, giving equipment choices consequences beyond appearance.

Two players share a keyboard. Split-screen and fixed-camera modes use the same underlying rules, with practice and solo views available for exploring the controls. Camera framing is its own design problem: it must explain the action without changing what the simulation does.

## Characters are part of the mechanic

My recent work has included integrating a beagle with a long-ear fighting setup and a seated orange tabby with independent giant paws. A character needs more than a model: its approved motion, contact points and controls have to survive the transition into actual play.

The asset workflow combines AI-assisted generation, Tripo base models and Blender preparation with runtime integration. Reviewing motion before integration helps catch a model that looks convincing in a still but fails when it swings, turns or supports its body.

<figure class="inline-figure">
  <img src="/assets/personal/wankai-preparation.webp" alt="The full-window preparation screen with separate character and weapon choices and model previews for two players" width="1500" height="742" loading="lazy">
  <figcaption>The preparation interface gives each player a separate loadout and ready state before the match starts.</figcaption>
</figure>

## Preparing a match

The preparation screen brings both players into one full-window view. Each side selects a valid character and weapon, inspects the actual model, and marks itself ready. Changing a choice cancels that player's readiness; the match starts after both sides are ready. Returning to the menu abandons the draft rather than silently changing the previous setup.

This work connects interface state with game state: a selection should describe what will actually spawn, and menu inputs should never leak into combat. The arena work follows the same principle, matching the visible floor and physical boundary while keeping the existing simulation intact.

## Collaboration and current status

Wankai is a collaborative project in the [Gumssss/Wankai repository](https://github.com/Gumssss/Wankai). My recent contributions cover character production and integration, the preparation interface, and local arena/camera work, developed with AI-assisted coding. The shared repository and its asset records retain the wider project and model credits.

The current result is a playable local prototype. Some newer local arena work may be ahead of the shared source checkpoint. There is no packaged application release, and Windows/Linux have not been validated. Further work is about playtesting, tuning contact and making the controls easier to understand.
