"""
Step 1
"""


def is_street(speed_limit):
    """
        Checks if the speed limit is a street speed limit
    """
    return speed_limit < 40


def is_safe_lane(lane_type):
    """
        Checks if the lane type is a safe lane
    """
    match lane_type:
        case "car":
            return False
        case "bike":
            return True
        case "bus":
            return True
        case "ped":
            return True
        case _:
            return None
