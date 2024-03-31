# Lab 1
In this README, it will show how to execute each to maze_solvers for each part and a short description for each part. 

## Part 1 
This Python script, maze_solver.py, is designed to solve a maze represented by a text file. Here's a breakdown of its functionality:

#### **Constants**
It defines symbolic constants for various elements of the maze, such as walls, the agent (player), and rewards.

#### **MazeSolver class:**

* **Initialization**: It initializes the maze solver by loading the maze from a text file, counting the number of prizes in the maze, and determining the starting position of the player.
* **Load Maze**: It loads the maze from a given text file.
* **Get Start Position**: It finds the starting position of the player in the maze.
* **Print Maze**: It prints the current state of the maze with the player's position.
* **Valid Move Check**: It checks if a move in a given direction is valid (i.e., not blocked by a wall and within the maze boundaries).
* **Transition**: It updates the player's position based on a given action (movement direction).
* **Goal Test**: It checks if the current position of the player contains a reward.
* **Solver**: It executes the solving process:
    - It initializes the starting state and collects user input for actions (movements).
    - It updates the player's position and checks for collected prizes until all prizes have been collected.
    - It prints the maze after each action and notifies the user when a prize is collected.
* **Main Section**: It creates an instance of the MazeSolver class, passing the filename of the maze text file. Then, it initiates the solving process by calling the solve method.

Overall, this script enables a user to interactively navigate through a maze, collecting rewards until all prizes are obtained.
