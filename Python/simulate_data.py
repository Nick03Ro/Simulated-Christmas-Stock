import pandas as pd
import numpy as np

np.random.seed(7)

WEEKS = list(range(1, 17))
WEEK_START_DATES = pd.date_range(start="2025-09-01", periods=16, freq="W-MON")

DELIVERY_UNITS = {1: 3000, 5: 2000, 9: 1000}
TOTAL_UNITS = sum(DELIVERY_UNITS.values())


def simulate(approach: str, display_share_fn, sell_rate: float) -> list[dict]:
    warehouse = 0.0
    display = 0.0
    cumulative_sold = 0.0
    rows = []

    for week in WEEKS:
        inbound = DELIVERY_UNITS.get(week, 0)
        warehouse += inbound

        target_share = display_share_fn(week)
        total_stock = warehouse + display
        target_display = total_stock * target_share
        move = max(0.0, target_display - display)
        move = min(move, warehouse)
        warehouse -= move
        display += move

        sold = display * sell_rate
        noise = np.random.normal(0, sold * 0.06) if sold > 0 else 0
        sold = max(0.0, min(sold + noise, display))

        display -= sold
        cumulative_sold += sold

        rows.append({
            "Week": week,
            "Week_Start_Date": WEEK_START_DATES[week - 1].date().isoformat(),
            "Approach": approach,
            "Delivery_Units": inbound,
            "Warehouse_Stock": round(warehouse),
            "Entry_Display_Stock": round(display),
            "Total_On_Hand": round(warehouse + display),
            "Units_Sold_This_Week": round(sold),
            "Cumulative_Units_Sold": round(cumulative_sold),
            "Cumulative_SellThrough_Pct": round(cumulative_sold / TOTAL_UNITS * 100, 1),
        })

    return rows


baseline_rows = simulate(
    approach="Baseline (Standard Planogram, No Active Placement)",
    display_share_fn=lambda w: min(0.08 + 0.027 * w, 0.44),
    sell_rate=0.31,
)

new_rows = simulate(
    approach="New (Active Placement Strategy)",
    display_share_fn=lambda w: min(0.32 + 0.055 * w, 0.68),
    sell_rate=0.30,
)

columns = [
    "Week", "Week_Start_Date", "Approach", "Delivery_Units",
    "Warehouse_Stock", "Entry_Display_Stock", "Total_On_Hand",
    "Units_Sold_This_Week", "Cumulative_Units_Sold", "Cumulative_SellThrough_Pct",
]
df = pd.DataFrame(baseline_rows + new_rows, columns=columns)
df.to_csv("cracker_placement_simulated.csv", index=False)

print(f"Baseline final sell-through: {baseline_rows[-1]['Cumulative_SellThrough_Pct']}%")
print(f"New final sell-through:      {new_rows[-1]['Cumulative_SellThrough_Pct']}%")
print("Saved cracker_placement_simulated.csv")
