from .api import fetch_spacex_data
from .cache import save_to_cache, load_from_cache

CACHE_FILE = "launches.json"

def get_all_launches(force_refresh=False):
    """
    Retrieves all launches, either from cache or API.

    Args:
        force_refresh (bool): If True, ignores cache and fetches fresh data

    Returns:
        list[dict]: Launch data
    """
    if not force_refresh:
        cached = load_from_cache(CACHE_FILE)
        if cached:
            return cached

    launches = fetch_spacex_data("launches")
    save_to_cache(CACHE_FILE, launches)
    return launches

def get_upcoming_launches():
    """
    Filters launches that are upcoming.

    Returns:
        list[dict]: Upcoming launches
    """
    all_launches = get_all_launches()
    return [launch for launch in all_launches if launch.get("upcoming")]

def count_launches_by_year(launches):
    """
    Count the number of launches per year.

    Args:
        launches (list[dict]): List of launch dictionaries

    Returns:
        dict: {year: count}
    """
    counts = {}
    for launch in launches:
        year = int(launch["date_utc"][:4])
        counts[year] = counts.get(year, 0) + 1
    return counts
