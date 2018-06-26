from footballscoring.definitions import Team, Score, Constraints
from footballscoring.gameconfig import GameConfig

class GameState:
    """Handles storage of game state and modification of game properties.

    Args:
        None 
    Attributes:
        state (dict): Contains the current state of the game
    """

    def __init__(self):     
        self.init_game()

    def init_game(self):
        """Initializes game state with default values.

        Args:
            None
        Returns:
            None
        """
        self.state = {
                "score": {
                    Team.HOME: 0,
                    Team.GUEST: 0
                },
                "timeouts": {
                    Team.HOME: 3,
                    Team.GUEST: 3
                },
                "quarter": 1,
                "down": 1,
                "distance": 10,
                "ball_on": 35,
                "possession": Team.UNKNOWN,
        }

    def reset_first_down(self):
        """Resets state to first down and 10 yds distance.

        Args:
            None
        Returns:
            None
        """
        self.state["down"] = 1
        self.state["distance"] = 10

    def reset_half(self, half=2):
        """Resets state to begin of a half.

        Args:
            half (int, optional): Either 1 or 2. Usually this is needed at the second half of the game, so 2 is default.
        Returns:
            None
        """
        self.state["down"] = 1
        self.state["distance"] = 10
        self.state["ball_on"] = 35
        self.state["possession"] = Team.UNKNOWN
        self.state["timeouts"][Team.HOME] = 3
        self.state["timeouts"][Team.GUEST] = 3

        if half == 1:
            self.state["quarter"] = 1
        elif half == 2: 
            self.state["quarter"] = 3
        else:
            raise ValueError("Half must be either 1 or 2")

    def modify_state_property(self, var_to_set, value, team=None):
        """Increase or decrease property. Checks if property to set is a team property. 

        Args:
            var_to_set (str): The property you want to modify.
            value (int): The value you want to increase or decrease the property by. For decrementation, simply pass a negative value.
            team (int, optional): If the property is a team property, you can specify the team here. 
        Returns: 
            None
        """
        if self.check_team_property(var_to_set, team):
            current_property_value = self.state[var_to_set][team]
            new_property_value = current_property_value + value

            if Constraints.check_constraint(var_to_set, new_property_value):
                self.state[var_to_set][team] = new_property_value
        else:
            current_property_value = self.state[var_to_set]
            new_property_value = current_property_value + value

            if Constraints.check_constraint(var_to_set, new_property_value):
                self.state[var_to_set] = new_property_value

    def check_team_property(self, var_to_set, team):
        """Checks if the property to modify is team property and if the team number is valid.

        Args:
            var_to_set (str): The property to check.
            team (int): The team number.
        Returns:
            is_team_property (bool): True, if team property and valid team number, False if otherwise.
        Raises:
            ValueError: If team number is invalid.
        """
        if var_to_set in Team.TEAM_PROPERTIES:
            if Constraints.check_constraint("team", team):
                return True
        else:
            return False

    def set_state_property(self, var_to_set, value, team=None):
        """Sets the the given property to the value wanted.

        Args:
            var_to_set (str): The property to set.
            value (str): The value the property should be setted to.
            team (int): If the property to set is a team property, specify team. Defaults to None, if it's no team property.
        Returns:
            None
        Raises:
            ValueError: If var_to_set is no valid property or if value is out of valid range.
            TypeError: If value is not of the proper type

        """
        if Constraints.check_constraint(var_to_set, value):
            if self.check_team_property(var_to_set, team):                    
                self.state[var_to_set][team] = value
            else:
                self.state[var_to_set] = value
   
    