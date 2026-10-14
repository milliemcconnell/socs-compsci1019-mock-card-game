import unittest
from unittest.mock import patch
from card_game.communication.ConsoleInOut import *

class test_mock_ConsoleInOut(unittest.TestCase):

    def test_get_input_string(self, mock_input):
        pass

    def test_get_input_integer(self):
        #Sub-task 1: Mock Console Input Integer
        with patch.object(ConsoleInOut,"get_string", return_value="18"):
            result = ConsoleInOut.get_input_integer()

        self.assertEqual(18, result)
    def test_get_input_string_builtin(self):
        pass

    def test_get_integer_max_attempts(self):
        #Sub-task 3 – Mock Console Input With Built In
        with patch(
            "card_game.communication.ConsoleInOut.get_string", 
            return_value="abc"
        ) as mock_get_string:

            result = ConsoleInOut.get_integer()

            self.assertEqual(-1, result)
            self.assertEqual(5, mock_get_string.call_count)
         

    def test_get_input_integer_builtin(self):
        pass