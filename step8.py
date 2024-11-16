"""
Step 8
"""

from step6 import InvalidAgeException, InvalidLaneTypeException


def remove_bike_lanes(lanes: list):
    """
        Remove all bike lanes
    """
    res = []
    try:
        for lane in lanes:
            if lane != "bike":
                res.append(lane)
    except InvalidLaneTypeException:
        print("Invalid lane type")
    except TypeError:
        print("Invalid argument type")
    except Exception:
        print("Something went wrong")

    return res


def validate_age(age):
    """
        Validate age
    """
    if age < 0:
        raise InvalidAgeException(age)
    return True


def fix_age(age):
    """
        Fix age
    """
    try:
        validate_age(age)
    except InvalidAgeException as e:
        print(e)
        age = 18
    except TypeError:
        print("Invalid argument type")
        age = 18
    except Exception:
        print("Something went wrong")
        age = 18
    finally:
        validate_age(age)
    return age
