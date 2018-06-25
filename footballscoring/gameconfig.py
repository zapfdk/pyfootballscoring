from footballscoring.definitions import Team

class GameConfig:
    """Contains general information about the game.

    Attributes:
        quarter_length (int): Length of a quarter in minutes.
        name_home (str): Name of home team
        name_guest (str): Name of guest team
        logo_home (str): Path of logo of home team
        logo_guest (str): path of logo of guest team
    """
    def __init__(self, quarter_length, name_home="", name_guest="", logo_home="", logo_guest=""):
        self.config = {
            "name": {
                Team.HOME: name_home,
                Team.GUEST: name_guest
            },
            "logo": {
                Team.HOME: logo_home,
                Team.GUEST: logo_guest
            },
            "quarter_length": quarter_length
        }
