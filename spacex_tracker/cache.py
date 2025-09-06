import json
from pathlib import Path

CACHE_DIR = Path("cache")
CACHE_DIR.mkdir(exist_ok=True)

def save_to_cache(filename: str, data: list):
    """
    Save API data to a JSON file for caching.

    Args:
        filename (str): Name of the cache file
        data (list): Data to be cached
    """
    path = CACHE_DIR / filename
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_from_cache(filename: str):
    """
    Load cached data if available.

    Args:
        filename (str): Cache file to read

    Returns:
        list: Cached data or empty list if file not found
    """
    path = CACHE_DIR / filename
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return []
