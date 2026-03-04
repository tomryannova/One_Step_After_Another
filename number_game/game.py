

"""
Number Guessing Game

A simple CLI-based guessing game that:
- Validates numeric input
- Enforces bounds (1–10)
- Allows replay until user exits
"""
import random
from .constants import MIN_VALUE, MAX_VALUE

def validate_guess(value: str) -> int:
    """
    Convert user input to integer and validate bounds.

    Args:
        value (str): Raw user input

    Returns:
        int: Validated integer guess

    Raises:
        ValueError: If input is not numeric or out of bounds
    """
    """
    Responsibility

        -Input validation
        -Type conversion
        -Enforcing business constraints (min/max)
    
    Professional Description

          validate_guess enforces domain constraints and ensures 
          that downstream logic receives a correctly typed, bounded 
          integer. It raises exceptions for invalid input rather than 
          handling presentation concerns. 
    Why That Matters

       -It is fully unit testable.
       -It isolates business rules.
       -It fails fast.
    """
    guess = int(value)

    """
    This is a Domain Constraint -- a business rule
    
    The "Domain" is the problem space you're modeling.
       o) Guessing game domain: Number guessing rules
       o) Banking app domain: Financial transactions
       o) Snowflake ETL domain: Data pipelines
       o) Healthcare system domain: Patient and medical data. 

    It has nothing to do with the python script itself

    The following line is an example of "Enforcing a Domain Constraint" 
    """
    if not MIN_VALUE <= guess <= MAX_VALUE:
        raise ValueError("Guess out of allowed range.")

    return guess

def generate_number() -> int:
    """Generate a random integer within allowed range."""

    """
    Responsibility

       Encapsulates randomness
       Centralizes number generation logic

    What It Does NOT Do

       -It does not validate
       -It does not compare guesses
       -It does not handle input

    Professional Description

       generate_number abstracts the randomness mechanism, allowing 
       the system to control or mock number generation during testing.


    Why That Matters

        In testing, you can replace it with:

        def generate_number():
                  return 5

    Now your tests are deterministic: the same input always produces 
         the same output — no randomness or unpredictability.

    That’s professional engineering.
    """
    return random.randint(MIN_VALUE, MAX_VALUE)

def play_round() -> None:
    """Execute a single round of the guessing game."""
    user_input = input(f"Guess a number between {MIN_VALUE} and {MAX_VALUE}: ")

    try:
        guess = validate_guess(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer within range.")
        return

    system_number = generate_number()

    if guess == system_number:
        print(f"Correct! The number was {system_number}.")
    elif guess > system_number:
        print(f"Too high! The number was {system_number}.")
    else:
        print(f"Too low! The number was {system_number}.")

def main() -> None:
    """Main game loop."""
    while True:
        play_round()

        if input("Play again? [y/n]: ").lower() == "n":
            break


if __name__ == "__main__":
    main()

