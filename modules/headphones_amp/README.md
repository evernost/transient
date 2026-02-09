# Headphones Amplifier

Output stage module.

---

## Overview

- **Type:** Amplifier
- **Domain:** Analog
- **Status:** Work in progress

Block diagram: TODO!

---

## Features
- Stereo amplifier
- Balance knob
- Volume knob
- Single power supply (+12V)
- Input impedance: TBD Ohms
- Output impedance: 32 Ohms
- Overload indicator



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
| Resonance | Potentiometer | Feedback amount |

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

| File | Description |
|-----|-------------|
| `headphones_amp_rev_A.pdf` | Electrical schematic (PDF export)|
| `headphones_amp_rev_A.kicad_pcb` | Schematic (KiCad 9.0.6)|
| `headphones_amp_rev_A.kicad_pcb` | PCB layout (KiCad 9.0.6)|
| `sim/XXX.asc` | SPICE simulation of the Schmitt Trigger |

---

## Calibration / Tuning
- Tune the bias voltage on $Q_5$ and $Q_{11}$
- Tune the quiescent current 
- Tune the overload threshold


---

## Known Issues / TODO

- [ ] Make the bias point higher: 1.6V might clip too early
- [ ] Add a reverse polarity protection


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






