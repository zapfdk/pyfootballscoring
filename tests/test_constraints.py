import unittest

from footballscoring.definitions import Constraints

class ConstraintsTest(unittest.TestCase):
    def testDowns(self):
        print("Testing down constraints...")

        for i in [1,2,3,4]:
            self.assertTrue(Constraints.check_constraint("down", i))
        for i in [0, 5]: 
            self.assertRaises(ValueError, Constraints.check_constraint, "down", i)
        for i in ["asdf"]:
            self.assertRaises(TypeError,  Constraints.check_constraint, "down", i)

    def testQuarter(self):
        print("Testing quarter constraints...")

        for i in [1,2,3,4]:
            self.assertTrue(Constraints.check_constraint("quarter", i))
        for i in [0, 5]: 
            self.assertRaises(ValueError, Constraints.check_constraint, "quarter", i)
        for i in ["asdf"]:
            self.assertRaises(TypeError,  Constraints.check_constraint, "quarter", i)

    def testDistance(self):
        print("Testing distance constraints...")

        for i in range(-1,100):
            self.assertTrue(Constraints.check_constraint("distance", i))
        for i in [-2, 100]: 
            self.assertRaises(ValueError, Constraints.check_constraint, "distance", i)
        for i in ["asdf"]:
            self.assertRaises(TypeError,  Constraints.check_constraint, "distance", i)

    def testBallOn(self):
        print("Testing ball_on constraints...")

        for i in range(1,51):
            self.assertTrue(Constraints.check_constraint("ball_on", i))
        for i in [0, 51]: 
            self.assertRaises(ValueError, Constraints.check_constraint, "ball_on", i)
        for i in ["asdf"]:
            self.assertRaises(TypeError,  Constraints.check_constraint, "ball_on", i)

    def testScore(self):
        print("Testing score constraints...")

        for i in range(0, 1000):
            self.assertTrue(Constraints.check_constraint("score", i))
        for i in [-1, 1000]: 
            self.assertRaises(ValueError, Constraints.check_constraint, "score", i)
        for i in ["asdf"]:
            self.assertRaises(TypeError,  Constraints.check_constraint, "score", i)

    def testQuarterLength(self):
        print("Testing quarter length constraints...")

        for i in range(1, 100):
            self.assertTrue(Constraints.check_constraint("quarter_length", i))
        for i in [-1, 1000]: 
            self.assertRaises(ValueError, Constraints.check_constraint, "quarter_length", i)
        for i in ["asdf"]:
            self.assertRaises(TypeError,  Constraints.check_constraint, "quarter_length", i)

    def testWrongKey(self):
        print("Testing checking invalid property...")

        self.assertRaises(ValueError, Constraints.check_constraint, "asdf", 1)

if __name__ == "__main__":
    unittest.main()