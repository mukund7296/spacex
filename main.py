"""
Main entry point for the SpaceX Launch Tracker.
Fetches data from SpaceX API and displays basic statistics.
"""

from spacex_tracker.api import fetch_spacex_data
from spacex_tracker.launches import get_all_launches
from spacex_tracker.stats import count_launches_by_year

def main():
    """Fetch and display SpaceX launch data and statistics."""
    print("Fetching all SpaceX launches...")
    launches = get_all_launches(force_refresh=True)
    print(f"Total launches fetched: {len(launches)}\n")

    print("Counting launches by year...")
    launch_counts = count_launches_by_year()
    for year, count in sorted(launch_counts.items()):
        print(f"{year}: {count} launches")

if __name__ == "__main__":
    main()

