"""Rear-axle load and load-index helpers (illustrative sizing from the case)."""

# ISO/ETRTO load index -> max load per tyre (kg)
LOAD_INDEX_KG = {
    45: 165, 46: 170, 47: 175, 48: 180, 49: 185, 50: 190, 51: 195, 52: 200,
    53: 206, 54: 212, 55: 218, 56: 224, 57: 230, 58: 236, 59: 243, 60: 250,
}


def gross_mass(kerb_kg: float, payload_kg: float) -> float:
    return kerb_kg + payload_kg


def rear_tyre_load(gross_kg: float, rear_share: float) -> float:
    """Static load on the rear tyre (single rear tyre assumed)."""
    if not 0 < rear_share < 1:
        raise ValueError("rear_share must be between 0 and 1")
    return gross_kg * rear_share


def min_load_index(required_kg: float, margin: float = 0.0) -> int:
    """Lowest load index whose rated load covers required_kg * (1 + margin)."""
    target = required_kg * (1 + margin)
    for li in sorted(LOAD_INDEX_KG):
        if LOAD_INDEX_KG[li] >= target:
            return li
    raise ValueError(f"No load index in table covers {target:.0f} kg")


def utilisation(load_kg: float, load_index: int) -> float:
    return load_kg / LOAD_INDEX_KG[load_index]
