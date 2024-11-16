"""
Step 5
"""


def can_drive_here(using_car: bool, age: int):
    """
        Checks if the person can drive
    """
    res = None
    try:
        if age < 0:
            raise ValueError
        if using_car is not bool:
            raise TypeError
        res = (using_car and age >= 21) or (not using_car and 3 < age < 21)
    except ValueError:
        print("Invalid age. Cannot be less than 0")
    except TypeError:
        print("Invalid argument type")
    except Exception:
        print("Something went wrong")
    return res
