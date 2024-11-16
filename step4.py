"""
Step 4
"""

from math import sqrt


def lane_count_ratio(count1, count2):
    """
        Returns the ratio of the two lane counts
    """
    res = None
    try:
        res = count1 / count2
    except TypeError:
        print("Invalid argument type")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except OverflowError:
        print("The numbers are too large")
    except Exception:
        print("Something went wrong")
    return res


def confirm_car_lane(lanes, i):
    res = False
    try:
        res = lanes[i] == "car"
    except TypeError:
        print("lanes is not a list")
    except KeyError:
        print("Invalid index type")
    except IndexError:
        print("Index out of range")
    except Exception:
        print("Something went wrong")
    return res


def square_plaza_side(area):
    """
        Returns the side of the square plaza
    """
    res = None
    try:
        res = sqrt(area)
        is_small = str(res)[10]
    except TypeError:
        print("Invalid argument type")
    except ValueError:
        print("Invalid argument value")
    except IndexError:
        print("Good, the number is small")
    except Exception:
        print("Something went wrong")
    return res
