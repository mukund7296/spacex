import pandas as pd
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
