"""
Step 7
"""

from step6 import UnderageException, InvalidLaneTypeException


def adults_on_scooters(age, wants_scooter_lane):
    """
        Only adults should use scooters, and no dedicated lane please
    """
    try:
        if age < 18:
            raise UnderageException(age)
        if wants_scooter_lane:
            raise InvalidLaneTypeException("scooter")
    except UnderageException as e:
        print(e)
    except InvalidLaneTypeException as e:
        print(e)
    except TypeError:
        print("Invalid argument type")
    else:
        print("You are good to go!")
