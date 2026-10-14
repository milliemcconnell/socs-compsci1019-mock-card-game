import unittest
from unittest.mock import patch, mock_open
from card_game.LoadCSV import *

class test_mock_LoadCSV(unittest.TestCase):

    def test_get_csv_rows(self):
        #Sub-task 4 – Mock File Load
        mocked_file = mock_open(read_data="Derek\nXI")

        with patch("builtins.open", mocked_file):
            rows = LoadCSV.get_csv_rows("any_file.csv")

        self.assertEqual("Xi", rows[1][0])