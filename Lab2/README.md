# Lab 2
Here's a description for each part in Lab 2. 

## Part 1
**Description**:
This Python script provides a simple implementation of the Breakthrough board game. Breakthrough is a two-player abstract strategy game played on an 8x8 grid. Each player has a set of pieces represented by 'X' and 'O' on the board, and the goal is to reach the opponent's home row or eliminate all opponent's pieces.

**Functionality**:

**Initialization**: The BreakthroughGame class initializes the game with customizable parameters such as the number of rows and columns on the board and the number of rows with pieces for each player.
**Initial State**: The initial_state method sets up the starting state of the game board with pieces arranged according to the rules of Breakthrough.
**Display State**: The display_state method prints the current state of the game board.
**Game Over Check**: The is_game_over method checks if the game is over by determining if any player has reached the last row or has no pieces left.
**Move Generation**: The generate_moves method generates all possible moves for a given player. These moves include advancing a piece forward or capturing opponent pieces diagonally.
**Usage**:

1. Ensure Python 3.x is installed on your system.
2. Download or clone the repository containing the script.
3. Run the script.

**Running the Script** :

```
python breathrough_game.py
```

**Output** :
Upon execution, the script will display the initial state of the game board, check if the game is over, and generate possible moves for both players.

**Example Output**:

```
Initial State:
XXXXXXXX
XXXXXXXX
........
........
........
........
oooooooo
oooooooo

Is game over? False

Possible moves for PLAYER1:
((0, 0), (1, 0))
((0, 0), (1, 1))
((0, 1), (1, 0))
((0, 1), (1, 1))
((0, 2), (1, 1))
((0, 2), (1, 2))
...

Possible moves for PLAYER2:
((7, 0), (6, 0))
((7, 0), (6, 1))
((7, 1), (6, 0))
((7, 1), (6, 1))
((7, 2), (6, 1))
((7, 2), (6, 2))
...






