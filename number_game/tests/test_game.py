
# tests/test_game.py
import pytest
#.  from Python's built-in unittest.mock, used to fake/replace functions during tests
from unittest.mock import patch
#. importing the 3 functions we want to test directly from the package
from number_game.game import validate_guess, generate_number, play_round

class TestValidateGuess:
    """Tests for validate_guess()"""

    def test_valid_guess(self):
        #. if the expression is True the test passes, if False it fails
        #. calling validate_guess("5") and asserting it returns integer 5
        assert validate_guess("5") == 5

    #. boundary testing — always test the exact edges of your allowed range, not just the middle
    #. 1 and 10 are the exact min/max from constants.py
    def test_min_boundary(self):
        #. if the expression is True the test passes, if False it fails
        #. calling validate_guess("5") and asserting it returns integer 5
        assert validate_guess("1") == 1

    #. boundary testing — always test the exact edges of your allowed range, not just the middle
    #. 1 and 10 are the exact min/max from constants.py
    def test_max_boundary(self):
        #. if the expression is True the test passes, if False it fails
        #. calling validate_guess("10") and asserting it returns integer 5
        assert validate_guess("10") == 10

    #. Testing for failure/bad values.
    def test_below_min(self):
        #.  tells pytest to expect a ValueError to be raised
        with pytest.raises(ValueError):
            #. if validate_guess("0") raises ValueError → test passes
            #. if it does NOT raise → test fails
            validate_guess("0")

    def test_above_max(self):
        #.  tells pytest to expect a ValueError to be raised
        with pytest.raises(ValueError):
            #. if validate_guess("11") raises ValueError → test passes
            #. if it does NOT raise → test fails
            validate_guess("11")

    def test_non_numeric(self):
        #.  tells pytest to expect a ValueError to be raised
        with pytest.raises(ValueError):
            #. if validate_guess("abc") raises ValueError → test passes
            #. if it does NOT raise → test fails
            #. "abc" — int("abc") raises ValueError immediately
            validate_guess("abc")

    def test_float_string(self):
        #.  tells pytest to expect a ValueError to be raised
        with pytest.raises(ValueError):
            #. if validate_guess("5.5") raises ValueError → test passes
            #. if it does NOT raise → test fails
            #. "5.5" — int("5.5") also raises ValueError because int() can't convert a float string directly
            validate_guess("5.5")


class TestGenerateNumber:
    """Tests for generate_number()"""

    def test_within_bounds(self):
        #. Run 100 tests
        for _ in range(100):
            #. Calls generate_number()
            n = generate_number()
            #. Verifies that the number returned is between 1 and 10
            assert 1 <= n <= 10


class TestPlayRound:
    """Tests for play_round()"""

    #. fakes the random number always returning 5, making tests deterministic

    #. @patch is a decorator — it wraps the test function and temporarily replaces a real function with a fake one

    #. @patch("number_game.game.generate_number", return_value=5) — replaces generate_number() so it always returns 5
    @patch("number_game.game.generate_number", return_value=5) -> mock_gen

    #. fakes the user typing "5" so the test doesn't wait for real keyboard input
    #. @patch("builtins.input", return_value="5") — replaces Python's built-in input() so it always returns "5" without waiting for keyboard input
    @patch("builtins.input", return_value="5") -> mock_output

    #. bottom @patch maps to the *first* mock parameter because it is applied first ( @patch is applied bottom to top )
    def test_correct_guess(self, mock_input, mock_gen, capsys):
        #. runs with faked input "5" and faked number 5
        play_round()
        #.  captures what was printed to the screen so you can assert against it
        #. a built-in pytest fixture that captures stdout/stderr
        #. reads everything that was printed to the screen
        output = capsys.readouterr().out
        #. Checks that the word "Correct" appeared in the output
        assert "Correct" in output

    #. fakes the random number always returning 5, making tests deterministic
    @patch("number_game.game.generate_number", return_value=5)
    #. fakes the user typing "8" so the test doesn't wait for real keyboard input
    @patch("builtins.input", return_value="8")
    def test_too_high(self, mock_input, mock_gen, capsys):
        play_round()
        #.  captures what was printed to the screen so you can assert against it
        output = capsys.readouterr().out
        assert "Too high" in output

    #. fakes the random number always returning 5, making tests deterministic
    @patch("number_game.game.generate_number", return_value=5)
    #. fakes the user typing "2" so the test doesn't wait for real keyboard input
    @patch("builtins.input", return_value="2")
    def test_too_low(self, mock_input, mock_gen, capsys):
        play_round()
        #.  captures what was printed to the screen so you can assert against it
        output = capsys.readouterr().out
        assert "Too low" in output

    @patch("builtins.input", return_value="abc")
    #. fakes the user typing "abc" so the test doesn't wait for real keyboard input
    def test_invalid_input(self, mock_input, capsys):
        play_round()
        #.  captures what was printed to the screen so you can assert against it
        output = capsys.readouterr().out
        assert "Invalid input" in output
