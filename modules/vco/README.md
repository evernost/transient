# VCO Module

Voltage-Controlled Module with digital control for the tuning.

Example:
> This module implements a voltage-controlled low-pass filter based on a 4-pole ladder topology, intended for use in the analog signal path.

---

## Overview

- **Type:** VCO
- **Domain:** Analog with Digital stabilisation
- **Status:** Work in progress

Block diagram: TODO!

---

## Features

- **Waveforms**: Sawtooth, Rectangular
- **Control**: exponential (1V/oct)


---

## Interfaces

### Inputs
| Name | Type | Range | Description |
|-----|------|-------|-------------|
| CV_IN | Analog | 0–5 V | Cutoff frequency control |
| RES_CV | Analog | 0–5 V | Resonance modulation |

### Outputs
| Name | Type | Description |
|------|------|-------------|
| OUT | Audio | Filtered signal |

---

## Controls

| Control | Type | Description |
|--------|------|-------------|
| Cutoff | Potentiometer | Manual cutoff frequency |
| Resonance | Potentiometer | Feedback amount |

---

## Electrical Characteristics

- **Supply voltage:** ±12V
- **Current consumption:** TBD mA
- **Signal levels:** TBD

---

## Implementation Notes

Design details, assumptions, or decisions worth remembering later.

Examples:
- Filter core based on [reference / paper / IC]
- Uses matched transistor pair for temperature stability
- Digital control smoothed with RC + oversampling

---

## Files

| File | Description |
|-----|-------------|
| `schematic.pdf` | Electrical schematic |
| `pcb.kicad_pcb` | PCB layout |
| `firmware/` | MCU code (if applicable) |
| `simulation/` | SPICE or other simulations |

---

## Calibration / Tuning

If applicable:
- Calibration steps
- Test points
- Required equipment

Example:
1. Apply 1 V to CV_IN
2. Adjust TRIM1 until cutoff = 1 kHz
3. Repeat for 5 V

---

## Known Issues / TODO

- [ ] Noise floor higher than expected
- [ ] Resonance unstable above 80%
- [ ] Add output buffer

---

## Revision History

| Revision | Date | Notes |
|--------|------|-------|
| Rev A | YYYY-MM-DD | Initial prototype |
| Rev B | YYYY-MM-DD | Fixed grounding issue |

---

## Related Modules

Links to other submodules in the repository:
- `../vca/`
- `../ring_modulator/`

---

## References

- Datasheets
- Papers
- App notes
- Inspiration designs


