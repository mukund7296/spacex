import pytest
from spacex_tracker.api import fetch_spacex_data


def test_fetch_launches_data():
    """Test fetching launch data from SpaceX API."""
    data = fetch_spacex_data("launches")
    assert isinstance(data, list), "Expected a list of launches"

    if data:  # If data is returned, check one example
        first_launch = data[0]
        assert "name" in first_launch, "Launch item should have a 'name'"
        assert "date_utc" in first_launch, "Launch item should have a 'date_utc'"
    else:
        # Fail the test if no data is returned
        assert False, "No launch data returned"
