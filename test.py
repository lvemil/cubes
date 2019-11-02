import unittest
from GameMaster import GameMaster

class TestChalleges(unittest.TestCase):
    def test_Challenge1(self):
        game = GameMaster(11,30)
        count = game.SetupChallenge1()
        result = game.Table.CountCubes()
        self.assertEqual(result, count)

if __name__ == '__main__':
    unittest.main()  
