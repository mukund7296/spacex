"""import pandas as pd
from spacex_tracker.launches import get_all_launches

def launches_table():
    launches = get_all_launches()
    df = pd.DataFrame(launches)
    df_table = df[['name', 'date_utc', 'rocket', 'success', 'upcoming']].copy()
    df_table.loc[:, 'date_utc'] = pd.to_datetime(df_table['date_utc'])
    df_table = df_table.sort_values('date_utc', ascending=True)

    # Print table in terminal
    print(df_table)

    # Export to CSV for Tableau
    df_table.to_csv("spacex_launches.csv", index=False)
    print("\n Exported to spacex_launches.csv! You can now open this in Tableau.")

if __name__ == "__main__":
    launches_table()
"""


from collections import Counter
from datetime import datetime
from tabulate import tabulate
from spacex_tracker.launches import get_all_launches

def main():
    launches = get_all_launches()

    # Count successful Falcon 1 launches
    falcon1_success = sum(1 for l in launches if l["rocket"] == "5e9d0d95eda69955f709d1eb" and l["success"])
    print(f"Successful Falcon 1 launches: {falcon1_success}\n")

    # Success rate by rocket
    rocket_ids = {}
    for l in launches:
        rocket_ids[l["rocket"]] = rocket_ids.get(l["rocket"], {"success": 0, "total": 0})
        rocket_ids[l["rocket"]]["total"] += 1
        if l["success"]:
            rocket_ids[l["rocket"]]["success"] += 1

    success_table = []
    for rocket_name, stats in [("Falcon 1", "5e9d0d95eda69955f709d1eb"), ("Falcon 9", "5e9d0d95eda69973a809d1ec"), ("Falcon Heavy", "5e9d0d95eda69974db09d1ed")]:
        data = rocket_ids.get(stats, {"success": 0, "total": 0})
        rate = int((data["success"] / data["total"]) * 100) if data["total"] > 0 else 0
        success_table.append([rocket_name, f"{rate}%"])
    print("Success rate by rocket:")
    print(tabulate(success_table, headers=["Rocket", "Success Rate"], tablefmt="grid"))
    print()

    # Launches by site
    site_counter = Counter(l.get("launch_site", "Unknown") for l in launches)
    site_table = [[site, count] for site, count in site_counter.items()]
    print("Launches by site:")
    print(tabulate(site_table, headers=["Launch Site", "Launches"], tablefmt="grid"))
    print()

    # Monthly launch frequency
    month_counter = Counter(datetime.fromisoformat(l["date_utc"]).strftime("%Y-%m") for l in launches)
    month_table = [[month, count] for month, count in sorted(month_counter.items())]
    print("Monthly launch frequency:")
    print(tabulate(month_table, headers=["Month", "Launches"], tablefmt="grid"))

if __name__ == "__main__":
    main()
