# Question
Could actively managing the placement of a high-volume seasonal item — rather 
than leaving it to the standard planogram — reduce warehouse backlog and 
improve sell-through before clearance markdown?

# Analysis
[📊 Tableau](https://public.tableau.com/app/profile/nicholas.robson/viz/SimulatedChristmasStock/Dashboard1?publish=yes)

# Datasets
This project uses a simulated dataset, not real company data. The underlying 
figures belong to my employer and can't be published, so I built a fabricated 
dataset designed to reproduce the shape and outcome of a real initiative I led 
at Waitrose — actively placing bulk seasonal stock (Christmas crackers) near 
store entry points and on end-cap displays, instead of leaving it to the 
default planogram. See dictionary for how the simulation was created.

# Findings:
- The Active Placement approach reaches ~93% cumulative sell-through by the 
  pre-Christmas clearance point, vs. ~75% for the Baseline — closely matching 
  the real outcome from the initiative this recreates.
- The Stock Location chart shows the mechanism behind the gap: under Active 
  Placement, Entry Display Stock spikes sharply at each of the three delivery 
  weeks, showing stock being moved to the floor immediately on arrival. Under 
  the Baseline, there's no such response — stock simply accumulates in the 
  warehouse and drains slowly over time, because no one was making an active 
  placement decision either way.
- The gap between the two approaches is widest in the middle of the season 
  (weeks 5-11) — the period where an unmanaged default does the most damage, 
  since stock sits in the warehouse for the longest stretch before it's found 
  its way to the shop floor.

# Note on the data
The dataset is fabricated for portfolio purposes. It is not real Waitrose 
sales, delivery, or stock data — I do not have access to that data outside 
my employer's systems, and wouldn't publish it if I did. The simulation was 
built to approximate the real, reported improvement from this initiative 
(cumulative sell-through rising from roughly 75% to roughly 90% by the time 
stock was marked down to clear).

# Libraries Used
Pandas, NumPy
