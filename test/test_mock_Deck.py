import unittest
from unittest.mock import patch
from card_game.card.entity.Deck import *


class TestMockDeck(unittest.TestCase):

    def test_play_a_card_from_deck_random(self):
        # Sub-task 5 – Mock Random Card Selection
        
        deck = create_deck()
        first_card = deck[0]

        with patch(
            "card_game.card.entity.Deck.random.randint",
            return_value = 0
        ) as mock_randint:
            
            card = play_a_card_from_deck(deck)

            self.assertEqual(first_card, card)

            mock_randint.assert_called_once_with(0,51)


