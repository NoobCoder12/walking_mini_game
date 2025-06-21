# Walking Game

A simple text-based mini-game in Python where the player takes steps and may find treasure chests with gold or nothing at all.

---

## Project Overview

This project consists of three main files:

- `chest.py` — Defines the `Chest` class representing treasure chests of various colors and gold values.
- `game.py` — Contains the `Game` class that handles game logic. The player can take steps, find chests, or find nothing. It tracks statistics and prints messages.
- `main.py` — The entry point that runs the game.
- `test_game.py` — Basic unit tests using `pytest` to verify core functionality of the `Game` class.

---

## How to Run the Game

1. Make sure you have Python 3.6+ installed.
2. (Optional) Install the `rich` library for colorful console output:
   ```bash
   pip install rich

3. Run the game:

  python main.py

## File Structure

      /
      ├── chest.py         # Chest class - treasure chests with gold
      ├── game.py          # Game class - game logic
      ├── main.py          # Entry point to run the game
      └── test_game.py     # Unit tests using pytest

## Testing

Tests verify:

    That after finding a chest, the chest count and gold amount increase.

    That after finding nothing, the 'nothing found' counter increases.

To run tests:

pytest test_game.py

## Sample Gameplay

      Welcome to my mini game!Each step you will have a chance to find something.
      Let's try!
      Would you like to take a step? y/n
      y
      You found [green]GREEN[/green] chest!Received 1023 gold.

      Would you like to take a step? y/n
      n
      Game statistics: 
      You took 1 steps. 
      You have found 1 chests and collected 1023 gold.
      You have found nothing 0 times.
      
      Would you like to save statistics as a text file? y/n 
      y
      File was saved. Thank you for playing. See you next time!

## Author

NoobCoder12

## License

This project is licensed under the MIT License.
