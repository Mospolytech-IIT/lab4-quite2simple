"""
    Step 9
"""

from step1 import is_street, is_safe_lane
from step2 import widen_symmetrical_road
from step3 import add_dutch_speed_limit
from step4 import lane_count_ratio, confirm_car_lane, square_plaza_side
from step5 import can_drive_here
from step7 import adults_on_scooters
from step8 import remove_bike_lanes, validate_age, fix_age


def call_everything():
    """
        Call everything
    """
    print("Step 1")
    try:
        print(is_street(-1))
    except Exception as e:
        print(e)

    try:
        is_safe_lane("a")
    except Exception as e:
        print(e)

    print("Step 2")
    widen_symmetrical_road("a")

    print("Step 3")
    add_dutch_speed_limit([])

    print("Step 4")
    lane_count_ratio("a", 2)
    confirm_car_lane([], 1)
    square_plaza_side("a")

    print("Step 5")
    can_drive_here("a", 2)

    print("Step 7")
    adults_on_scooters(-1, "a")

    print("Step 8")
    remove_bike_lanes([])
    try:
        validate_age("a")
    except Exception as e:
        print(e)
    print(fix_age("a"))
