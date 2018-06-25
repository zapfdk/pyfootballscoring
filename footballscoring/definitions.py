class Score:
    """Contains definitions for possible scores for easier handling of scores.

    Attributes:
        TOUCHDOWN (int): equals 6 points.
        FIELDGOAL (int): equals 3 points.
        SAFETY (int): equals 2 points.
        PAT (int): equals 1 points.
        TPT (int): equals 2 points.
    """
    TOUCHDOWN, FIELDGOAL, SAFETY, PAT, TPT = (6, 3, 2, 1, 2)

class Team:
    """Contains definitions for Teams as Enum, so Team Numbers can't be confused.

    Attributes:
        HOME (int): 0
        GUEST (int): 1
        UNKNOWN (int): 2
        TEAM_PROPERTIES (list): List of properties which belong to a team.
    """
    HOME, GUEST, UNKNOWN = range(3)
    TEAM_PROPERTIES = ["score", "timeouts"]

class Constraints:
    """Contains definitions for properties, their name, their valid range and their valid datatype.

    Attributes:
        valid_values (dict): Contains property name as key, and a tuple as value with (validRange, validDataType)
    """
    valid_values = {
        "down": (range(1,5), int),
        "quarter": (range(1,5), int),
        "distance": (range(-1,100), int), # -1=Goal, 0=Inches, >0=Distance to go
        "ball_on": (range(1,51), int), 
        "score": (range(0, 1000), int),
        "team": (range(2), int),
        "timeouts": (range(4), int),
        "possession": (range(3), int),
        "quarter_length": (range(1, 100), int)
    }

    @classmethod
    def check_constraint(cls, var_to_check, value):
        """Checks if the given property fits its constraints.

        Args:
            var_to_check (str): Name of the property.
            value (int): Value of the property
        Returns:
            valid_property (bool): If name and value match their constraint.
        Raises:
            ValueError: If var_to_check is no valid property or if value is out of valid range.
            TypeError: If value is not of the proper type
        """
        if var_to_check not in cls.valid_values.keys():
            raise ValueError("Please specify one the following you want to check: %s" %(",".join(cls.valid_values.keys())))
        
        valid_range = cls.valid_values[var_to_check][0]
        valid_type = cls.valid_values[var_to_check][1]

        if not isinstance(value, valid_type):
            raise TypeError("Value of {} has to be of {}".format(var_to_check, str(valid_type)))
        if not value in valid_range:
            raise ValueError("Value of {} has to be in ({})".format(var_to_check, ", ".join(str(x) for x in valid_range)))

        return True

class GameModificationResults:
    """Define result statuses. Not every modification should raise an exception but return whether operation was successful or if there was an error.
    """
    SUCCESS, WRONG_KEY_ERROR, VALUE_OUT_OF_RANGE_ERROR = range(3)