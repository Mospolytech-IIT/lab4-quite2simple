"""
Step 3
"""


def add_dutch_speed_limit(speed_limits):
    """
        Adds 30 to the list
    """
    try:
        if 30 in speed_limits:
            return
        speed_limits.append('test')
        speed_limits.remove('test')
    except Exception:
        print("Invalid speed limit list")
        speed_limits = []
    finally:
        speed_limits.append(30)
