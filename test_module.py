# Author: Diego Vallejo

import unittest
from RPS import player

class TestPlayer(unittest.TestCase):
    def test_initial_play(self):
        self.assertIn(player(""), ["R", "P", "S"])

    def test_react_to_previous_move(self):
        history = ["R", "P", "S"]
        self.assertIn(player("R"), ["P", "S"])
        self.assertIn(player("P"), ["R", "S"])
        self.assertIn(player("S"), ["R", "P"])

if __name__ == '__main__':
    unittest.main()
