---
brand: IKEA
model: GRILLPLATS
category: Smart plug
power:
  - state: Thread mode, on, nothing plugged in
    typical_w: 0.4
  - state: Thread mode, off
    typical_w: 0.1–0.2
    notes: Sometimes reads 0 W.
  - state: Zigbee mode, on, nothing plugged in
    typical_w: 0.4
  - state: Zigbee mode, off
    typical_w: 0
date: 2026-11
---

# IKEA GRILLPLATS

Can run in either Thread mode or Zigbee mode. I tested both.

## Power

All figures are with nothing plugged into the socket, so they show what the plug itself uses.

| Mode | On | Off |
|---|---|---|
| Thread | about 0.4 W | 0.1–0.2 W, sometimes 0 W |
| Zigbee | 0.4 W | 0 W |

**How I measured:** with a second GRILLPLATS plugged in between the wall and this plug, reading its power figure (it reports to 0.1 W). That measures this plug's own draw from the mains. A plug's built-in meter only measures what's plugged into it, so it can't show this.

Uses less power than the [INSPELLING](inspelling.md) in either mode.

## Responsiveness

Controlled from Home Assistant.

- **Thread mode:** pretty responsive, but occasionally freezes for a second. In my setup, commands go through Apple HomePods acting as the Thread border router (the bridge between the Thread network and the rest of the home network).
- **Zigbee mode (via Zigbee2MQTT):** not responsive enough. It often hangs. Unusable for anything that needs fast, repeated switching, such as lighting effects.

For response time, the [INSPELLING](inspelling.md) is much better.
