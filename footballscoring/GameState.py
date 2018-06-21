class GameState:
    def __init__(self):
        self.init_game()

    def init_game(self):
        self.score_home = 0
        self.score_guest = 0
        self.quarter = 1

        self.reset_half()

    def reset_half(self):
        self.ball_on = 35

        self.reset_first_down()

    def reset_first_down(self):
        self.down = 1
        self.distance = 10


    
    