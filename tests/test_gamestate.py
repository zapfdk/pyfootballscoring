import unittest

from footballscoring.definitions import Team, Score
from footballscoring.gamestate import GameState

class GameStateTest(unittest.TestCase):
    def setUp(self):
        self.game_state = GameState()

    def testInitState(self):
        print("Testing initialization of game state...")

        self.assertEqual(self.game_state.state["down"], 1)
        self.assertEqual(self.game_state.state["quarter"], 1)
        self.assertEqual(self.game_state.state["distance"], 10)
        self.assertEqual(self.game_state.state["ball_on"], 35)
        self.assertEqual(self.game_state.state["timeouts"][Team.HOME], 3)
        self.assertEqual(self.game_state.state["timeouts"][Team.GUEST], 3)
        self.assertEqual(self.game_state.state["score"][Team.HOME], 0)
        self.assertEqual(self.game_state.state["score"][Team.GUEST], 0)
        self.assertEqual(self.game_state.state["possession"], Team.UNKNOWN)

    def testSettingProperties(self):
        print("Testing setting of properties...")

        self.game_state.set_state_property("down", 2)
        self.assertEqual(self.game_state.state["down"], 2)

        self.game_state.set_state_property("quarter", 2)
        self.assertEqual(self.game_state.state["quarter"], 2)

        self.game_state.set_state_property("distance", 15)
        self.assertEqual(self.game_state.state["distance"], 15)

        self.game_state.set_state_property("ball_on", 3)
        self.assertEqual(self.game_state.state["ball_on"], 3)

        self.game_state.set_state_property("possession", Team.HOME)
        self.assertEqual(self.game_state.state["possession"], Team.HOME)

        self.game_state.set_state_property("score", 2, team=Team.HOME)
        self.assertEqual(self.game_state.state["score"][Team.HOME], 2)

        self.game_state.set_state_property("score", 4, team=Team.GUEST)
        self.assertEqual(self.game_state.state["score"][Team.GUEST], 4)

    def testResetFirstDown(self):
        print("Testing resetting first down...")
        
        self.game_state.set_state_property("down", 3)
        self.game_state.set_state_property("distance", 9)

        self.game_state.reset_first_down()

        self.assertEqual(self.game_state.state["down"], 1)
        self.assertEqual(self.game_state.state["distance"], 10)

    def testResetQuarter(self):
        print("Testing resetting half...")

        self.game_state.set_state_property("down", 3)
        self.game_state.set_state_property("distance", 9)
        self.game_state.set_state_property("quarter", 2)
        self.game_state.set_state_property("ball_on", 20)
        self.game_state.set_state_property("timeouts", 1, team=Team.HOME)
        self.game_state.set_state_property("timeouts", 2, team=Team.GUEST)
        self.game_state.set_state_property("possession", Team.HOME)

        self.game_state.reset_half()

        self.assertEqual(self.game_state.state["down"], 1)
        self.assertEqual(self.game_state.state["distance"], 10)
        self.assertEqual(self.game_state.state["quarter"], 3)
        self.assertEqual(self.game_state.state["ball_on"], 35)
        self.assertEqual(self.game_state.state["timeouts"][Team.HOME], 3)
        self.assertEqual(self.game_state.state["timeouts"][Team.GUEST], 3)
        self.assertEqual(self.game_state.state["possession"], Team.UNKNOWN)

        self.game_state.reset_half(half=1)

        self.assertEqual(self.game_state.state["quarter"], 1)

    def testTeamActionCheck(self):
        print("Testing check whether action is for a team property...")

        self.assertTrue(self.game_state.check_team_property("timeouts", 0))
        self.assertTrue(self.game_state.check_team_property("timeouts", 1))
        self.assertRaises(ValueError, self.game_state.check_team_property, "timeouts", 2)

        self.assertTrue(self.game_state.check_team_property("score", 0))
        self.assertTrue(self.game_state.check_team_property("score", 1))
        self.assertRaises(ValueError, self.game_state.check_team_property, "score", 2)

        self.assertFalse(self.game_state.check_team_property("distance", team=None))

    def testModifyingStateProperty(self):
        print("Testing incrementation and decrementation of state properties...")

        self.assertRaises(ValueError, self.game_state.modify_state_property, "down", -1)

        for action in ["down", "distance", "quarter", "ball_on"]:
            self.game_state.modify_state_property(action, value=1)

        self.assertEqual(self.game_state.state["down"], 2)
        self.assertEqual(self.game_state.state["distance"], 11)
        self.assertEqual(self.game_state.state["quarter"], 2)
        self.assertEqual(self.game_state.state["ball_on"], 36)

        for action in ["down", "distance", "quarter", "ball_on"]:
            self.game_state.modify_state_property(action, value=-1)

        self.assertEqual(self.game_state.state["down"], 1)
        self.assertEqual(self.game_state.state["distance"], 10)
        self.assertEqual(self.game_state.state["quarter"], 1)
        self.assertEqual(self.game_state.state["ball_on"], 35)

        self.game_state.modify_state_property("score", Score.TOUCHDOWN, team=Team.HOME)
        self.assertEqual(self.game_state.state["score"][Team.HOME], 6)
        self.game_state.modify_state_property("score", Score.FIELDGOAL, team=Team.GUEST)
        self.assertEqual(self.game_state.state["score"][Team.GUEST], 3)

        self.game_state.modify_state_property("timeouts", -1, team=Team.HOME)
        self.assertEqual(self.game_state.state["timeouts"][Team.HOME], 2)

        self.game_state.modify_state_property("timeouts", -2, team=Team.GUEST)
        self.assertEqual(self.game_state.state["timeouts"][Team.GUEST], 1)

        self.assertRaises(ValueError, self.game_state.modify_state_property, "timeouts", -2, Team.GUEST)