"""Range gain and OEM value of lower rolling resistance (illustrative)."""

# Case: 3% range gain ~ 0.1 kWh battery ~ INR 800-1,000 per vehicle.
# Implies ~3.3 kWh pack and ~INR 8,000-10,000 per kWh.


def battery_kwh_saved(range_gain_pct: float, pack_kwh: float) -> float:
    """Pack size the OEM could shed for the same range."""
    return pack_kwh * range_gain_pct / 100


def oem_value_inr(range_gain_pct: float, pack_kwh: float, inr_per_kwh: float) -> float:
    return battery_kwh_saved(range_gain_pct, pack_kwh) * inr_per_kwh


def range_gain_from_rr(rr_cut_pct: float, rr_energy_share: float = 0.15) -> float:
    """First-order range gain = RR cut x share of traction energy spent on RR.

    rr_energy_share is an ASSUMPTION (urban 2W). 17% RR cut x ~15% share ~ 2.6%,
    consistent with the case's 2-4% claim. Replace with measured data in Round 2.
    """
    return rr_cut_pct * rr_energy_share
