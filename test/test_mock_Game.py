import unittest
from unittest.mock import patch, mock_open
from card_game.Game import *

class test_mock_Game(unittest.TestCase):

    def test_get_game_info(self):
        #Sub-task 2 – Mock Console Game Info
        with patch.object(ConsoleInOut, "get_string", side_effect=["Derek", "3"]):
            result = Game.get_game_info()

        self.assertEqual(3,result)

    def test_get_computer_players_names(self):
        #Sub-task 5 – Mock Get Player Names
        pass