from datetime import datetime

def format_date(date_str: str, fmt="%Y-%m-%d %H:%M:%S"):
    """
    Converts a UTC date string to a formatted string.

    Args:
        date_str (str): UTC date string
        fmt (str): Desired output format

    Returns:
        str: Formatted date string
    """
    try:
        date_obj = datetime.fromisoformat(date_str.rstrip("Z"))
        return date_obj.strftime(fmt)
    except Exception:
        return date_str
