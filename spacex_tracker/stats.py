from .launches import get_all_launches

def count_launches_by_year():
    """
    Count the number of launches grouped by year.

    Returns:
        dict: Year -> Launch count
    """
    launches = get_all_launches()
    year_count = {}
    for launch in launches:
        year = launch.get("date_utc", "")[:4]
        if year:
            year_count[year] = year_count.get(year, 0) + 1
    return year_count

def get_total_launches(launches):
    """Return total number of launches."""
    return len(launches)
