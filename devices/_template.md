---
# Copy this file to devices/<brand>/<model>.md (lowercase, hyphens).
# Only brand, model and category are required. Delete any section you don't need.
brand: Example
model: ABC-123
category: Smart plug

# One entry per state you measured. typical_w is what it sits at most of the time;
# peak_w is the highest you saw. Leave peak_w out if it never moved.
power:
  - state: standby
    typical_w: 0.4
    peak_w: 1.2
    notes: Optional short note.
  - state: on, full load
    typical_w: 5.0

date: 2026-11
---

# Example ABC-123

## Power

Anything worth saying that doesn't fit in the numbers above.

## Other notes

Anything else you've found out about this device: boot time, noise, real-world range, quirks.
