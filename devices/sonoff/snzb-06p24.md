---
brand: Sonoff
model: SNZB-06P24
category: Zigbee presence sensor
power:
  - state: normal operation
    typical_w: 0.1
    peak_w: 0.5
    notes: Mostly 0.1 W, with occasional short bursts up to 0.5 W.
date: 2026-11
---

# Sonoff SNZB-06P24

## Power

Spends most of its time at 0.1 W. Every so often it bursts up to about 0.5 W, then drops back.
Compare the [SNZB-06P](snzb-06p.md), which holds a flat 0.1 W.

**How I measured:** powered from an Anker 25,000mAh 165W power bank (the one with built-in retractable cables), reading the output on its display, which shows power to 0.1 W. That means this is the sensor alone, with no mains adapter losses. It also means 0.1 W is the smallest step the display can show, so the true idle draw could be a bit lower.
