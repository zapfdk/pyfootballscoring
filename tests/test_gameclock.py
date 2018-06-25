import unittest
import time
from datetime import timedelta

from footballscoring.gameclock import GameClock

class GameClockTest(unittest.TestCase):
    def testWrongQuarterLength(self):
        print("Testing creating game clock with invalid quarter length...")

        self.assertRaises(ValueError, GameClock, -1)
        self.assertRaises(TypeError, GameClock, "asdf")

    def testSetGameClock(self):
        print("Testing setting game clock...")

        game_clock = GameClock(10)
        self.assertEqual(game_clock.remaining_time, timedelta(minutes=10))

        game_clock.set_clock(minutes=5, seconds=30)
        self.assertEqual(game_clock.remaining_time, timedelta(minutes=5, seconds=30))

    def testClockHitsZero(self):
        print("Testing right behaviour when clock hits zero...")

        game_clock = GameClock(1)
        game_clock.set_clock(minutes=0, seconds=2)
        game_clock.start()
        time.sleep(3)

        self.assertEqual(game_clock.running, False)
        self.assertEqual(game_clock.remaining_time, timedelta(0))

    def testClockToggle(self):
        print("Testing toggling clock...")

        game_clock = GameClock(1)
        self.assertEqual(game_clock.running, False)
        game_clock.toggle()
        self.assertEqual(game_clock.running, True)
        game_clock.toggle()
        self.assertEqual(game_clock.running, False)

    def testClockAccuracy(self):
        print("Testing clock accuracy...")

        game_clock = GameClock(1)
        game_clock.start()
        time.sleep(10)
        game_clock.stop()

        print("Time difference: ", game_clock.remaining_time.total_seconds()-50 , " seconds")
        self.assertAlmostEqual(game_clock.remaining_time.total_seconds(), 50, places=0)
