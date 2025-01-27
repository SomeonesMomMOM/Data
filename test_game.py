import unittest
from game.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(3)

    def test_game_initialization(self):
        self.assertEqual(self.game.correct_answers, 0)
        self.assertEqual(self.game.required_correct_answers, 3)

    def test_is_game_over(self):
        self.assertFalse(self.game.is_game_over())
        self.game.correct_answers = 3
        self.assertTrue(self.game.is_game_over())

    def test_str_method(self):
        self.assertEqual(str(self.game), "You have answered 0 questions correctly out of 3.")
        self.game.correct_answers = 1
        self.assertEqual(str(self.game), "You have answered 1 questions correctly out of 3.")


if __name__ == "__main__":
    unittest.main()
