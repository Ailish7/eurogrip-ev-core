# Eurogrip EV-Core

Case Study 2: a purpose-built tyre platform for mass-market electric two-wheelers (Round 1 executive summary, engineering concept, and Round 2 plan).

**Thesis:** an EV two-wheeler is not an ICE bike with a battery. The rear tyre sees instant torque, bidirectional load (drive and regen), higher kerb mass and a silent powertrain, while rolling resistance (RR) directly moves range.

## Three pillars
| Pillar | What changes |
|---|---|
| A. Dual-zone, low-hysteresis compound | Silica-rich functionalised S-SBR/BR duplex tread: low-RR centre, high-grip shoulder |
| B. Bidirectional-load tread + NVH | Torque-balanced non-directional blocks, chamfered edges, 4-5 pitch sequence |
| C. Load-scaled, thermally managed construct | +2 to +3 load-index steps, stiffer apex, heat-venting sidewall |

## Repository layout
```
docs/            Case write-up split by topic (start at docs/01-case-analysis.md)
docs/source/     Original case study PDF
src/ev_core/     Small, tested calculators for the case's illustrative numbers
tests/           Unit tests (stdlib unittest, no dependencies)
data/            Cost breakdown as CSV
```

## Quick start
```bash
python -m unittest discover -s tests -v
python -m ev_core.report        # run with PYTHONPATH=src
```

## What the models cover
- `load_rating.py`: rear-axle load and load-index lookup (LI 51 = 195 kg -> LI 54 = 212 kg).
- `cost_model.py`: line-item cost delta vs ICE-equivalent tyre.
- `range_model.py`: range gain from RR reduction and its battery/INR value to an OEM.

All figures are engineering targets and estimates from the case study, to be validated in Round 2.
B77V2G
