"""How common is your birthday? 62 million US births (2000–2014), from FiveThirtyEight's public data.
Usage:  python analyse_birthdays.py [YOUR_MONTH YOUR_DAY]      e.g.  python analyse_birthdays.py 12 25

Prints the rarest and most common birthdays, the weekday effect, Friday the 13th vs other Fridays,
and (optionally) how your birthday ranks. Saves a calendar heatmap to birthday_heatmap.png.
"""
import sys
from pathlib import Path

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

URL = "https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_2000-2014_SSA.csv"
local = Path("data/US_births_2000-2014_SSA.csv")
d = pd.read_csv(local if local.exists() else URL)          # columns: year, month, date_of_month, day_of_week (1 = Mon), births
print(f"{d.births.sum():,} births over {len(d):,} days ({d.year.min()}–{d.year.max()})\n")

# 1. how common is each calendar day? (average births on that date, compared with the average day)
by_day = d.groupby(["month", "date_of_month"]).births.mean()
ratio = by_day / by_day.drop((2, 29)).mean()               # Feb 29 only exists in leap years, so leave it out of the average
order = ratio.drop((2, 29)).sort_values()
name = lambda md: pd.Timestamp(2001, md[0], md[1]).strftime("%d %b")
print("Rarest birthdays:      ", ", ".join(f"{name(k)} ({v - 1:+.0%})" for k, v in order.head(5).items()))
print("Most common birthdays: ", ", ".join(f"{name(k)} ({v - 1:+.0%})" for k, v in order.tail(5)[::-1].items()))

# 2. the weekday effect (scheduled C-sections and inductions happen on weekdays)
dow = d.groupby("day_of_week").births.mean()
print("\nBirths by weekday vs the average day:", ", ".join(f"{n} {v - 1:+.0%}" for n, v in zip("Mon Tue Wed Thu Fri Sat Sun".split(), dow / dow.mean())))

# 3. Friday the 13th vs Fridays one week either side (the 6th and the 20th): same weekday, so it's a fair comparison
fri = d[d.day_of_week == 5]
f13, other = fri[fri.date_of_month == 13].births.mean(), fri[fri.date_of_month.isin([6, 20])].births.mean()
print(f"Friday the 13th: {f13:,.0f} births a day vs {other:,.0f} on other Fridays ({f13 / other - 1:+.1%})")

# 4. your birthday
if len(sys.argv) == 3:
    m, day = int(sys.argv[1]), int(sys.argv[2])
    rank = int(order.rank(ascending=False)[(m, day)]) if (m, day) != (2, 29) else None
    print(f"\nYour birthday ({name((m, day)) if (m, day) != (2, 29) else '29 Feb'}): {ratio[(m, day)] - 1:+.0%} vs an average day"
          + (f", #{rank} most common of 365" if rank else " (leap day, the rarest of all)"))

# 5. calendar heatmap: rows = months, columns = days
grid = ratio.unstack().reindex(columns=range(1, 32))
fig, ax = plt.subplots(figsize=(14, 5))
im = ax.imshow(grid, cmap="YlOrBr", vmin=0.85, vmax=1.12, aspect="auto")
ax.set_yticks(range(12), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]); ax.set_xticks(range(0, 31, 2), range(1, 32, 2))
ax.set_title("How common is each birthday? (US births 2000–2014, vs the average day)", loc="left", fontweight="bold")
fig.colorbar(im, ax=ax, fraction=0.025); fig.tight_layout(); fig.savefig("birthday_heatmap.png", dpi=150)
print("\nSaved birthday_heatmap.png")
