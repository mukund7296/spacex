import pytest
from spacex_tracker.stats import get_total_launches
from spacex_tracker.api import fetch_spacex_data


def test_get_total_launches():
    """Test total number of launches calculation."""
    launches = fetch_spacex_data("launches")
    total = get_total_launches(launches)

    assert isinstance(total, int), "Total launches should be an integer"
    assert total >= 0, "Total launches should be non-negative"

    if launches:
        assert total == len(launches), "Total should match the length of launches"
    else:
        assert total == 0, "Total should be zero if no launches exist"
