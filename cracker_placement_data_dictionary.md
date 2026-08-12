# Seasonal Bulk Item Placement — Simulated Dataset

**Important:** This is fabricated, illustrative data built to demonstrate a real
workplace scenario without using any actual employer data. Label it clearly as
simulated wherever it appears in your portfolio (e.g. "Simulated data based on
a real retail placement decision I led").

## The scenario it recreates

A UK supermarket receives a large seasonal bulk item (e.g. Christmas crackers)
across three deliveries between September and early November, ahead of the
Christmas trading period. The comparison is not between two deliberate
strategies — it's between an unmanaged default and a proactive intervention:

- **Baseline (Standard Planogram, No Active Placement):** no one was actively
  managing this item's placement. It followed the standard planogram from HQ
  like everything else, which wasn't designed with this item's disproportionate
  warehouse footprint in mind — so stock simply built up in the back with
  whatever ended up on the shop floor, rather than a chosen approach.
- **New (Active Placement Strategy):** a deliberate change — proposed after
  noticing the recurring backlog problem — to move stock to high-visibility
  entry and end-cap displays much earlier and in greater volume.

## Columns

| Column | Description |
|---|---|
| Week | Week number, 1–16, spanning the Sept–Dec selling season |
| Week_Start_Date | Illustrative calendar date for that week |
| Approach | "Baseline (Standard Planogram, No Active Placement)" or "New (Active Placement Strategy)" |
| Delivery_Units | Units received into the warehouse that week (0 except delivery weeks) |
| Warehouse_Stock | Units sitting in the warehouse at week's end |
| Entry_Display_Stock | Units on front-of-store display at week's end |
| Total_On_Hand | Warehouse_Stock + Entry_Display_Stock |
| Units_Sold_This_Week | Units sold that week |
| Cumulative_Units_Sold | Running total of units sold |
| Cumulative_SellThrough_Pct | Cumulative_Units_Sold ÷ total season stock (6,000 units), as a % |

## The story this data tells

- By week 16 (the pre-Christmas clearance point), the New approach reaches
  ~93% cumulative sell-through vs. ~75% for the Baseline — reflecting the real
  outcome from the actual initiative this recreates.
- The gap between the two lines is widest in the middle weeks (weeks 5–11),
  which mirrors the real problem: with no one actively managing it, stock just
  sat in the warehouse mid-season instead of being available where customers
  could buy it — not because anyone chose that outcome, but because nobody
  was making an active decision either way.

## Suggested Tableau charts

1. **Delivery timeline** — bar chart of Delivery_Units by Week_Start_Date, to
   set the scene (when stock actually arrived).
2. **Stock location over time** — stacked area chart of Warehouse_Stock vs.
   Entry_Display_Stock, one view per Approach, showing the warehouse backlog
   building up in the Previous approach and draining fast in the New one.
3. **The headline chart** — line chart of Cumulative_SellThrough_Pct by Week,
   both Approaches on the same axes. This is the one chart that tells the
   whole story on its own — lead with it.
