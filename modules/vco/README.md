# VCO Module

Voltage-Controlled Module, with digital control for accurate tuning.

<!-- Example:
> This module implements a voltage-controlled low-pass filter based on a 4-pole ladder topology, intended for use in the analog signal path. -->

---

## Overview

- **Type:** VCO
- **Domain:** Analog, with Digital stabilisation
- **Status:** Work in progress

Block diagram: TODO!

---

## Features

- **Waveforms**: Sawtooth, Rectangular
- **Control**: exponential (1V/oct)
- **Inner Modulation**: up to 2 synchronised modulators to add more depth 
- **Sync**: digital input for synchronisation effect + random synchronisation


---

## Interfaces

### Inputs
| Name | Type | Range | Description |
|-----|------|-------|-------------|
| TODO | TODO | TODO |

### Outputs
| Name | Type | Description |
|------|------|-------------|
| TODO | TODO | TODO |

---

## Controls

| Control | Type | Description |
|--------|------|-------------|
| TODO | TODO | TODO |


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
| `vco_rev1.pdf` | Electrical schematic (PDF export)|
| `vco_rev1.kicad_pcb` | Schematic (KiCad 9.0.6)|
| `vco_rev1.kicad_pcb` | PCB layout (KiCad 9.0.6)|
| `sim/XXX.asc` | SPICE simulation of the Schmitt Trigger |

---

## Calibration / Tuning
> This section is TODO!



---

## Known Issues / TODO
- [ ] Create footprint for the STM32G441KB

---

## Revision History

| Revision | Date | Notes |
|--------|------|-------|
| Rev A | 30 January 2026 | Initial prototype |


---

## Related Modules

Links to other submodules in the repository:
- `../vca/`
- `../ring_modulator/`

---

## References
- Elektor FORMANT, Chapter 4 and 5


