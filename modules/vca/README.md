# VCA Module

A simple analog Voltage-Controlled Amplifier for audio signals.

---

## Overview

- **Type:** VCA
- **Domain:** Analog
- **Status:** Work in progress

Block diagram: TODO!

---

## Features
- **Overdrive**: the input can be overdriven on purpose to add _colors_ to the function
- **Control**: linear and logarithmic control

---

## Interfaces

### Inputs
| Name | Type | Range | Description |
|-----|------|-------|-------------|
| IN | Audio | ±1V | Input signal |
| AMP_CV | Analog | 0–5 V | Volume control |

### Outputs
| Name | Type | Description |
|------|------|-------------|
| OUT | Audio | Filtered signal |

---

## Controls

| Control | Type | Description |
|--------|------|-------------|
| Cutoff | Potentiometer | Manual cutoff frequency |


---

## Electrical Characteristics

- **Supply voltage:** ±12V
- **Current consumption:** TBD mA
- **Signal levels:** TBD

---

## Implementation Notes
Section is TODO.


---

## Files

| File                      | Description                       |
|---------------------------|-----------------------------------|
| `vca_rev_A.pdf`           | Electrical schematic (PDF export)|
| `vca_amp_rev_A.kicad_sch` | Schematic (KiCad 10.0.7)|
| `vca_amp_rev_A.kicad_pcb` | PCB layout (KiCad 10.0.7)|
| `sim/XXX.asc`             | SPICE simulation |

---

## Tools
Designed with KiCAD 10.0.7

### KiCAD Grid dimensions

| Name   | Size    | Description        |
|--------|---------|--------------------|
| Grid 1 | 0.5 mm  | PCB outline        |
| Grid 2 | 50 mil  | Parts placement    |
| Grid 3 | 50 mil  | Routing            |

Track size: 500µm

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


---

## Related Modules

Links to other submodules in the repository:
- `../vca/`
- `../ring_modulator/`

---

## References



