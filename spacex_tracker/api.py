import requests

def fetch_spacex_data(endpoint: str):
    """
    Fetches data from SpaceX API for a given endpoint.

    Args:
        endpoint (str): API endpoint, e.g., 'launches', 'rockets'

    Returns:
        list[dict]: List of JSON objects returned by the API.
    """
    url = f"https://api.spacexdata.com/v4/{endpoint}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch {endpoint}: {e}")
        return []
