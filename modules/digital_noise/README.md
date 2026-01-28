# Digital Noise Module

A Digital Noise Generator module for pink and white noise generation.



---

## Overview

- **Type:** Noise generator
- **Domain:** Digital
- **Status:** Work in progress

Block diagram: TODO!

---

## Features

- **Waveforms**: Noise
- **Control**: 


---

## Interfaces

### Inputs
| Name | Type | Range | Description |
|-----|------|-------|-------------|
| clock | Digital | 0–5 V | Clock for the PRBS generator |
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
No calibration required.


---

## Known Issues / TODO

- [ ] TODO

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
- Elektor Voiced/Devoiced detector, April 1981 p.32-33


