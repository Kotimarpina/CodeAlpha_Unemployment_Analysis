from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_1 = BASE_DIR / "unemployment_india_cleaned.csv"
DATA_2 = BASE_DIR / "unemployment_rate_upto_nov2020_cleaned.csv"
OUTPUT_DIR = BASE_DIR / "analysis_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

area_data = pd.read_csv(DATA_1, parse_dates=["Date"])
state_data = pd.read_csv(DATA_2, parse_dates=["Date"])

rate = "Estimated Unemployment Rate (%)"
employment = "Estimated Employed"
participation = "Estimated Labour Participation Rate (%)"

monthly_state = state_data.groupby("Date")[rate].mean().reset_index()
monthly_area = area_data.groupby(["Date", "Area"])[rate].mean().reset_index()
pre_covid = state_data.loc[state_data["Date"] < "2020-03-01", rate].mean()
covid_period = state_data.loc[state_data["Date"] >= "2020-03-01", rate].mean()
peak_row = monthly_state.loc[monthly_state[rate].idxmax()]
lowest_row = monthly_state.loc[monthly_state[rate].idxmin()]
region_average = state_data.groupby("Region")[rate].mean().sort_values(ascending=False)

print("STATE-LEVEL DATASET")
print(state_data.describe(include="all").to_string())
print("\nMean unemployment rate before March 2020:", round(pre_covid, 2), "%")
print("Mean unemployment rate from March to October 2020:", round(covid_period, 2), "%")
print("Difference:", round(covid_period - pre_covid, 2), "percentage points")
print("\nPeak monthly average:", peak_row["Date"].strftime("%B %Y"), round(peak_row[rate], 2), "%")
print("Lowest monthly average:", lowest_row["Date"].strftime("%B %Y"), round(lowest_row[rate], 2), "%")
print("\nHighest average by state:")
print(region_average.head(5).round(2).to_string())

plt.figure(figsize=(10, 5))
plt.plot(monthly_state["Date"], monthly_state[rate], marker="o")
plt.title("Average Unemployment Rate by Month (2020)")
plt.xlabel("Month")
plt.ylabel("Unemployment rate (%)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_unemployment_trend.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 5))
for area in monthly_area["Area"].dropna().unique():
    subset = monthly_area[monthly_area["Area"] == area]
    plt.plot(subset["Date"], subset[rate], marker="o", label=area)
plt.title("Rural and Urban Unemployment Trends")
plt.xlabel("Month")
plt.ylabel("Unemployment rate (%)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "rural_urban_trends.png", dpi=300)
plt.show()

plt.figure(figsize=(11, 6))
region_average.sort_values().plot(kind="barh")
plt.title("Average Unemployment Rate by State/Region")
plt.xlabel("Average unemployment rate (%)")
plt.ylabel("State/region")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "state_average_unemployment.png", dpi=300)
plt.show()

monthly_state.to_csv(OUTPUT_DIR / "monthly_unemployment_summary.csv", index=False)
region_average.rename("Average Unemployment Rate (%)").to_csv(
    OUTPUT_DIR / "state_unemployment_summary.csv"
)
