# Author: Diego Vallejo

from RPS import player
from RPS_game import play, quincy, johnny, jake, jane

if __name__ == '__main__':
    # Uncomment the following line to run the tests automatically
    # import test_module

    # Example to test the player against quincy
    # play(player, quincy, 1000, verbose=True)

    # Run unit tests
    import unittest
    import test_module

    unittest.main()
