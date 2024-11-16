"""
Step 6
"""


class InvalidAgeException(Exception):
    """
        Age is a bad value
    """
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}. Age should be above or equal to 0")


class UnderageException(Exception):
    """
        Person is underage
    """
    def __init__(self, age):
        super().__init__(f"Person is underage (under 18). Age: {age}")


class InvalidLaneTypeException(Exception):
    """
        Lane type is a bad value
    """
    def __init__(self, lane_type):
        self.allowed_types = ["car", "bike", "bus", "ped"]
        super().__init__(f"Invalid lane type: \
            {lane_type}. The only valid values are {", ".join(self.allowed_types)}")


class InvalidSpeedLimitException(Exception):
    """
        Speed limit is a bad value
    """
    def __init__(self, speed_limit):
        super().__init__(f"Invalid speed limit: {speed_limit}. Speed limit should be above 0")
