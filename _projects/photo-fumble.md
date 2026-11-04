---
title: Photo Fumble
description: A real-time browser party game built at OxHack 2026 for three or more friends.
permalink: /projects/photo-fumble/
lead: Bring a photo, a voice note, or an old chat. See how much your friends remember about what happened.
summary: A real-time browser party game that turns friends’ photos, voice recordings, and old chats into five games.
status: Live game
context_label: Hackathon
context: OxHack 2026
stack: React, TypeScript, Node.js, Socket.IO, Supabase
role: I led the OxHack team and built the web application.
featured: true
featured_order: 2
image: /assets/personal/photo-fumble-landing.webp
image_alt: Photo Fumble’s landing page, with an empty room join form and a spread of sample photo prints
image_width: 1265
image_height: 1000
image_caption: The public room entry screen uses sample photos. Photo credits are listed on the game’s homepage.
---

[**Play Photo Fumble**](https://photo-fumble.onrender.com/) · [View source](https://github.com/LucasH1225/photo-fumble)

## From a shared memory to a round

I built Photo Fumble at [OxHack 2026](https://26.oxhack.net/) as a party game for groups of three or more. One player creates a room and shares its six-digit code. The others join from their own browsers. The host picks a mode, everyone contributes one item, and the game runs timed rounds and shows a final ranking before returning the group to the lobby.

Each mode asks a different question about what the group remembers. In **Memory Quiz**, players guess when a photo was taken. **Voice Detective** and **Chat Archaeology** ask them to reconstruct the context of a recording or a chat. **Memory Bluff** pairs a photo with two stories and asks which is true. In **Memory Impostor**, one player sees a blurred photo and has to describe it without giving themselves away.

## Keeping the room in sync

I built the interface in React and TypeScript. A Node.js server controls round deadlines, validates actions, and calculates scores. Socket.IO sends state updates as players submit guesses, vote, and move between rounds. Each browser receives only the view for its player, so the server can send the blurred photo to the impostor while the others see the clear one.

Supabase stores room state and media in production. Rooms keep separate players, uploads, and games, and a refresh returns a player to the current round with its original deadline. The same group can reuse its room code to play another mode.
