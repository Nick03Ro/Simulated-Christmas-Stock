import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cracker_placement_simulated.csv")

COLORS = {
    "Baseline (Standard Planogram, No Active Placement)": "tab:orange",
    "New (Active Placement Strategy)": "tab:blue",
}

fig, ax = plt.subplots(figsize=(9, 5.5))

for approach, subset in df.groupby("Approach"):
    ax.plot(
        subset["Week"],
        subset["Cumulative_SellThrough_Pct"],
        marker="o",
        linewidth=2,
        label=approach,
        color=COLORS.get(approach),
    )

ax.axhline(100, color="grey", linestyle=":", linewidth=1)
ax.set_title(
    "Cumulative Sell-Through: Baseline vs New Placement Strategy\n"
    "(Simulated/illustrative data)",
    fontsize=12,
    fontweight="bold",
)
ax.set_xlabel("Week")
ax.set_ylabel("Cumulative Sell-Through (%)")
ax.legend(loc="lower right", fontsize=9)
ax.grid(True, linestyle=":", alpha=0.6)

plt.tight_layout()
plt.savefig("cracker_sellthrough_preview.png", dpi=150)
print("Saved cracker_sellthrough_preview.png")
