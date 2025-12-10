# TicTacToe Game
A simple console-based Tic-Tac-Toe game implemented in Python. Two players take turns marking spaces on a 3x3 grid.

## Project Structure
The core of this project is a single Python file, main.py. It contains the TicTacToe class with its associated attributes and methods.

Here is a brief overview of the class methods:

* `__init__()` initializes the game board and randomly selects the first player.
* `get_random_first_player()` chooses whether 'X' or 'O' will play first.
* `fix_spot()` allows a player to mark a cell on the board.
* `has_player_won()` checks if a player has won the game.
* `is_board_filled()` checks if the game board is completely filled.
* `swap_player_turn()` toggles the active player.
* `show_board()` prints out the current state of the game board.
* `start()` begins the game loop, processing user input and game updates.

## Requirements
To run this project, you will need:

* Python 3.x
* prettytable
  to install prettytable, run:

`pip install prettytable colorama`

## Usage 
Run the main script

` python main.py`

### How to Play

1. The grid is numbered 1-9 as follows:
```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┴───┴───┘
```
1. Turns: Players alternate. Enter a number (1-9) for your desired cell.
2. Validation:
Must be a number between 1 and 9.
Cell must be empty (game will reprompt if taken).
1. Winning: First to get three in a row (horizontal, vertical, or diagonal) wins.
2. Draw: If the board fills without a winner, it's a draw.
3. Exit: The game ends automatically on win or draw.