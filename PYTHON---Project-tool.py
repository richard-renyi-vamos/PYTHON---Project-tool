import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Project milestones data
milestones = [
    {"name": "Project Kickoff", "date": "2024-11-01"},
    {"name": "Requirements Gathering", "date": "2024-11-15"},
    {"name": "Design Phase", "date": "2024-12-01"},
    {"name": "Development Start", "date": "2025-01-01"},
    {"name": "Testing Phase", "date": "2025-02-15"},
    {"name": "Final Review", "date": "2025-03-01"},
    {"name": "Project Launch", "date": "2025-03-15"}
]

# Convert milestone dates to datetime objects
dates = [datetime.strptime(milestone["date"], "%Y-%m-%d") for milestone in milestones]
names = [milestone["name"] for milestone in milestones]

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 2))
ax.plot(dates, [1]*len(dates), "o-", color="royalblue", markerfacecolor="orange")  # Line and markers

# Customize the timeline appearance
ax.set_yticks([])  # Hide y-axis
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
plt.xticks(rotation=45)

# Add milestone labels
for i, (date, name) in enumerate(zip(dates, names)):
    ax.text(date, 1.05, name, ha="center", fontsize=10, rotation=45)

# Title and display
plt.title("Project Timeline", fontsize=14)
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
