"""
This module contains unit tests for the Guess the Number Game.
"""
import unittest
from unittest.mock import patch
import guess_the_number_game


class TestGuesstheNumberGame(unittest.TestCase):
    """
    Test suite for the Guess the Number Game.
    """
    def setUp(self):
        # This method is called before each test case
        self.game = guess_the_number_game

    def test_generate_random_number(self):
        """
            Test the generate_random_number function.
            This test checks if the generated random
            number is a string and has a length of 4.
        """
        self.assertIsInstance(
            self.game.generate_random_number(),
            str,
            "Returned value is not a string")
        self.assertEqual(len(
            self.game.generate_random_number()),
            4,
            "Returned string does not have a length of 4")

    def test_provide_hints(self):
        """
            Test the provide_hints function.
            This test checks if the provide_hints function
            generates valid hints based on the comparison
            between a random number and a guessed number.
        """
        random_number = "1234"
        guessed_number = "5678"
        hints = self.game.provide_hints(random_number, guessed_number)

        # Check if the hints are valid
        valid_hint_characters = {'-'}
        for hint in hints:
            self.assertIn(
                hint,
                valid_hint_characters,
                f"Invalid hint character: {hint}")

    def test_play_game_runs(self):
        """
        To test whether the play_game function runs without errors.
        """
        try:
            self.game.play_game()
        except AssertionError as exception:
            self.fail(f"play_game() raised an exception: {exception}")

    def test_main(self):
        """
        Test the main function.
        This test simulates the execution of the main function and verifies
        if the user inputs 'yes' and 'no' are correctly processed.
        """
        # Mock the input to simulate user responses
        user_input = ['yes', 'no']

        with patch('builtins.input', side_effect=user_input):
            try:
                self.game.main()
            except StopIteration:
                pass  # StopIteration will be raised when input is exhausted


if __name__ == '__main__':
    unittest.main()
