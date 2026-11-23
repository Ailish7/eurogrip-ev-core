"""Line-item cost delta of EV-Core vs the ICE-equivalent tyre (percent)."""
import csv
from pathlib import Path

CASE_STATED_RANGE = (8.0, 12.0)  # total quoted in the case study


def load_items(path=None):
    path = Path(path) if path else Path(__file__).resolve().parents[2] / "data" / "cost_breakdown.csv"
    with open(path, newline="") as f:
        return [
            {"item": r["item"], "low": float(r["low_pct"]), "high": float(r["high_pct"])}
            for r in csv.DictReader(f)
        ]


def total_range(items):
    return sum(i["low"] for i in items), sum(i["high"] for i in items)


def midpoint(items):
    lo, hi = total_range(items)
    return (lo + hi) / 2


def reconciles_with_case(items):
    """True if additive range equals the case's stated +8 to +12%."""
    return total_range(items) == CASE_STATED_RANGE


def premium_per_pair(base_pair_price_inr: float, pct: float) -> float:
    return base_pair_price_inr * pct / 100
