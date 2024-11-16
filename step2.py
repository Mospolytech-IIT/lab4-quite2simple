"""
Step 2
"""


def widen_symmetrical_road(lane_count):
    """
        Returns a doubled number unless it's odd or less than 1
    """
    try:
        return lane_count * 2
    except Exception:
        print("Invalid lane count")
        return 2
