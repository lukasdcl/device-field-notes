---
brand: Sonoff
model: SNZB-06P
category: Zigbee presence sensor
power:
  - state: normal operation
    typical_w: 0.1
    peak_w: 0.1
    notes: Steady; never seen it deviate.
date: 2026-11
---

# Sonoff SNZB-06P

## Power

Sits at 0.1 W the whole time. Unlike the [SNZB-06P24](snzb-06p24.md), no bursts.

**How I measured:** powered from an Anker 25,000mAh 165W power bank (the one with built-in retractable cables), reading the output on its display, which shows power to 0.1 W. That means this is the sensor alone, with no mains adapter losses. It also means 0.1 W is the smallest step the display can show, so the true idle draw could be a bit lower.
