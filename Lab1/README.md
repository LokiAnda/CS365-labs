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



## Part 2
This Python script defines a class, **MazeSolver**, which employs depth-first search (DFS) to find a solution path through a maze. Here's a breakdown of its functionality:

#### **Initialization**:
    * It initializes the **MazeSolver** object by loading the maze from a specified file, initializing a set to track visited nodes, initializing a counter for the number of expanded nodes, and initializing an empty list to store the solution path.

#### **load_maze method**:
    * It loads the maze from a text file and returns it as a list of lists.

#### **get_start_position method**:
    * It iterates through the maze to find the starting position marked by the symbol 'P'.

#### **single_dfs method**:
    - It performs a single depth-first search starting from a given position.
    - It maintains a stack to explore nodes in a depth-first manner.
    - It expands nodes until it finds a goal position (symbol '.') or exhausts all possible paths.
    - It updates the solution path and the number of nodes expanded during the search.

#### **display_solution method**:

It displays the maze with the solution path marked by the symbol '#'.
It prints the length of the solution path and the total number of nodes expanded during the search.

#### **Main Section**:
    - It creates an instance of the MazeSolver class, passing the filename of the maze text file.
    - It retrieves the starting position from the maze.
    - It performs a depth-first search from the starting position.
    - It displays the solution path along with relevant statistics.


#Part 3

This Python script defines a class, **MazeSolver**, which implements three different search algorithms (Breadth-First Search, Greedy Best-First Search, and A* Search) to find a solution path through a maze. Here's a breakdown of its functionality:

#### Initialization:
    - It initializes the MazeSolver object by loading the maze from a specified file and finding the start and goal positions within the maze.

####**load_maze method:**
    -It loads the maze from a text file and returns it as a list of lists.

#### **find_start_position method**:
    - It iterates through the maze to find the starting position marked by the symbol 'P'.

#### **find_goal_positions method**:
    - It iterates through the maze to find all goal positions marked by the symbol '.'.

### Search Algorithms:

#### **Breadth-First Search (bfs)**:
    - It explores the maze using a breadth-first search strategy, expanding nodes level by level.
    - It maintains a queue to store positions and paths.
    - It uses a set to track visited nodes.

#### **Greedy Best-First Search (gbfs)**:
    - It explores the maze using a greedy best-first search strategy, prioritizing nodes based on a heuristic function (Manhattan distance to the closest goal).
    - It maintains a priority queue to store positions, paths, and their priorities.
    - It uses a set to track visited nodes.

#### **A Search (astar):***
    - It explores the maze using the A* search algorithm, considering both the cost to reach a node from the start and the estimated cost to reach the goal.
    - It maintains a priority queue to store positions, paths, and their priorities.
    - It uses a set to track visited nodes.

#### **Heuristic Function (manhattan_distance):**
    - It calculates the Manhattan distance between two positions, which serves as the heuristic for Greedy Best-First Search and A* Search.
#### **display_solution method**:
    - It displays the solution path found by the search algorithm along with the path cost and the number of nodes expanded during the search.

### Main Section:

    - It creates an instance of the MazeSolver class, passing the filename of the maze text file.
    - It applies each search algorithm to find a solution path through the maze.
    - It displays the solution paths and relevant statistics.


# Part 4
The provided code is a Python implementation of the Multi-Prize A* search algorithm for solving maze-like environments where an agent (denoted by 'P') navigates to collect prizes ('.'). The maze can contain walls ('%') which the agent cannot pass through.

Here's a brief overview of the main components:

## MazeSolver Class: This class encapsulates the functionality to solve the maze.
    - **Constructor**: Initializes the solver with a maze file, loading the maze and finding the start position and goal positions.

    - **load_maze**: Reads the maze from a file and returns it as a 2D list.

    - **find_start_position**: Finds the starting position of the agent in the maze.

    - **find_goal_positions**: Finds the positions of all prizes in the maze.

    - **multi_astar**: Implements the Multi-Prize A* algorithm to find the optimal path to collect all prizes.

    - **heuristic**: Calculates the heuristic value for A* search, which is the Manhattan distance to the nearest unvisited prize.

    - **manhattan_distance**: Calculates the Manhattan distance between two positions in the maze.

    - **display_solution**: Displays the solution path, path cost, and number of expanded nodes.

## Main Section: 
Creates an instance of MazeSolver with the provided maze file "multiprize-tiny.txt" and invokes the multi_astar method to solve the maze.

To run this code, ensure that the maze file "multiprize-tiny.txt" exists in the same directory as the script, or provide the correct path to the maze file.

This script will print the solution path, path cost, and number of expanded nodes once the Multi-Prize A* search algorithm completes its execution.








