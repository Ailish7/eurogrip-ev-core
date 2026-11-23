"""Print the case's headline numbers from the models."""
from . import cost_model, load_rating as lr, range_model as rm


def main():
    gross = lr.gross_mass(120, 150)
    lo, hi = lr.rear_tyre_load(gross, 0.55), lr.rear_tyre_load(gross, 0.60)
    print(f"Gross {gross:.0f} kg; rear tyre load {lo:.0f}-{hi:.0f} kg")
    print(f"LI 51 util {lr.utilisation(hi, 51):.0%}, LI 54 util {lr.utilisation(hi, 54):.0%}")

    items = cost_model.load_items()
    t = cost_model.total_range(items)
    print(f"Cost delta (additive) +{t[0]:.0f}% to +{t[1]:.0f}%; case states +8% to +12%")
    print("Reconciles with case:", cost_model.reconciles_with_case(items))

    for cut in (15, 20):
        print(f"RR cut {cut}% -> range gain ~{rm.range_gain_from_rr(cut):.1f}% (case claims 2-4%)")
    print(f"3% gain on 3.3 kWh pack @ INR 9,000/kWh = INR {rm.oem_value_inr(3, 3.3, 9000):.0f}")


if __name__ == "__main__":
    main()
