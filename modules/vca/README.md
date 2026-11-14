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

| File                  | Description                       |
|-----------------------|-----------------------------------|
| `vca_rev_A.pdf`       | Electrical schematic (PDF export) |
| `vca_rev_A.kicad_sch` | Schematic (KiCad 10.0.8)          |
| `vca_rev_A.kicad_pcb` | PCB layout (KiCad 10.0.8)         |
| `sim/XXX.asc`         | SPICE simulation                  |

---

## Tools
Designed with KiCAD 10.0.8

### KiCAD Grid Settings

| Name   | Size    | Description        |
|--------|---------|--------------------|
| Grid 1 | 0.25 mm | PCB outline        |
| Grid 2 | 25 mil  | Parts placement    |
| Grid 3 | 25 mil  | Routing            |

**Rationale**: Grid 2 and Grid 3 were initially 50 mil, but turned out to be too coarse for precise tracks.


### KiCAD Track settings

| Name    | Size   | Description                |
|---------|--------|----------------------------|
| Class 1 | 500 um | Regular traces (signal)    |
| Class 2 | 800 um | Power traces               |

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



