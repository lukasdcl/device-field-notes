---
brand: IKEA
model: INSPELLING
category: Smart plug
power:
  - state: on, nothing plugged in
    typical_w: 0.6–0.8
  - state: "off"
    typical_w: 0.1
date: 2026-11
---

# IKEA INSPELLING

## Power

Figures are with nothing plugged into the socket, so they show what the plug itself uses.

- **On:** 0.6–0.8 W
- **Off:** 0.1 W

**How I measured:** with a GRILLPLATS plugged in between the wall and this plug, reading its power figure (it reports to 0.1 W). The INSPELLING's own built-in reading only goes in 1 W steps, and only measures what's plugged into it, so it couldn't measure this.

Uses more power than the [GRILLPLATS](grillplats.md) in either of that plug's modes.

## Responsiveness

Controlled from Home Assistant, it feels instant. It copes fine with being sent commands continuously in quick succession.

The best response time of the IKEA plugs I've tried. The [GRILLPLATS](grillplats.md) was noticeably slower in both of its modes.
