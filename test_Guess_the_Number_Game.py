import unittest
from unittest.mock import patch
import Guess_the_Number_Game

class TestGuesstheNumberGame(unittest.TestCase):


    def setUp(self):
        # This method is called before each test case
        self.game = Guess_the_Number_Game

    def test_generate_random_number(self):
        self.assertIsInstance(self.game.generate_random_number(), str, "Returned value is not a string")
        self.assertEqual(len(self.game.generate_random_number()), 4, "Returned string does not have a length of 4")

    def test_provide_hints(self):
        random_number = "1234"
        guessed_number = "5678"
        hints = self.game.provide_hints(random_number, guessed_number)

        # Check if the hints are valid
        valid_hint_characters = {'-'}
        for hint in hints:
            self.assertIn(hint, valid_hint_characters, f"Invalid hint character: {hint}")

    def test_play_game_runs(self):
        try:
            self.game.play_game()
        except Exception as e:
            self.fail(f"play_game() raised an exception: {e}")

    def test_main(self):
        # Mock the input to simulate user responses
        user_input = ['yes', 'no']
        user_input_index = 0

        with patch('builtins.input', side_effect=user_input):
            try:
                self.game.main()
            except StopIteration:
                pass  # StopIteration will be raised when input is exhausted

if __name__ == '__main__':
    unittest.main()






