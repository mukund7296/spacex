import pytest
from spacex_tracker.launches import count_launches_by_year
from spacex_tracker.api import fetch_spacex_data
from spacex_tracker.launches import get_all_launches, count_launches_by_year


def test_count_launches_by_year():
    """Test counting launches by year."""
    launches = fetch_spacex_data("launches")
    counts = count_launches_by_year(launches)

    assert isinstance(counts, dict), "Expected a dictionary of counts"

    # If data exists, ensure counts are positive integers
    if counts:
        for year, count in counts.items():
            assert isinstance(year, int), "Year should be an integer"
            assert isinstance(count, int), "Count should be an integer"
            assert count >= 0, "Count should be non-negative"
    else:
        assert False, "No launch data returned"
