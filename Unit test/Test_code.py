import unittest
from unittest.mock import patch
from io import StringIO
import datetime

# Import the functions to be tested
from personality_quiz_module import calculate_age, personality_quiz

class TestPersonalityQuiz(unittest.TestCase):

    def test_calculate_age(self):
        # Test the calculate_age function
        dob = "2000-01-01"
        expected_age = datetime.datetime.today().year - 2000
        self.assertEqual(calculate_age(dob), expected_age)

    @patch("builtins.input", side_effect=["John", "1990-01-01", "1", "2", "3", "1", "2", "3", "1", "2", "3", "1", "2", "3", "1", "2", "3", "1", "2", "3", "yes"])
    def test_personality_quiz_scenario1(self, mock_input):
        # Test the personality_quiz function - Scenario 1

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            personality_quiz()
        self.assertIn("Great job! Let's see what your personality reveals...", mock_stdout.getvalue())
        self.assertIn("Your personality type is:", mock_stdout.getvalue())
        self.assertIn("In a nutshell:", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["Alice", "2005-06-15", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "yes"])
    def test_personality_quiz_scenario2(self, mock_input):
        # Test the personality_quiz function - Scenario 2

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            personality_quiz()
        self.assertIn("Great job! Let's see what your personality reveals...", mock_stdout.getvalue())
        self.assertIn("Your personality type is:", mock_stdout.getvalue())
        self.assertIn("In a nutshell:", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["Bob", "1980-03-10", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "yes"])
    def test_personality_quiz_scenario3(self, mock_input):
        # Test the personality_quiz function - Scenario 3

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            personality_quiz()
        self.assertIn("Great job! Let's see what your personality reveals...", mock_stdout.getvalue())
        self.assertIn("Your personality type is:", mock_stdout.getvalue())
        self.assertIn("In a nutshell:", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["Eva", "1995-12-20", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "yes"])
    def test_personality_quiz_scenario4(self, mock_input):
        # Test the personality_quiz function - Scenario 4

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            personality_quiz()
        self.assertIn("Great job! Let's see what your personality reveals...", mock_stdout.getvalue())
        self.assertIn("Your personality type is:", mock_stdout.getvalue())
        self.assertIn("In a nutshell:", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)