# maze_solver.py

# Define constants for maze symbols
WALL = '%'
AGENT = 'P'
REWARD = '.'

class MazeSolver:
    
    def __init__(self, maze_file):
        self.maze = self.load_maze(maze_file)
        self.num_prizes = sum(row.count(REWARD) for row in self.maze)
        self.player_position = self.get_start_position()

        # Print the maze for visualization
        self.print_maze()

    def load_maze(self, maze_file):
        with open(maze_file, 'r') as f:
            return [list(line.strip()) for line in f.readlines()]

    def get_start_position(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == AGENT:
                    return (x, y)

    def print_maze(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if (x, y) == self.player_position:
                    print('P', end='')  # Print player symbol
                else:
                    print(cell, end='')  # Print maze cell
            print()  # Newline for next row

    def is_valid_move(self, x, y):
        if 0 <= x < len(self.maze[0]) and 0 <= y < len(self.maze):
            return self.maze[y][x] != WALL
        return False

    def transition(self, action):
        x, y = self.player_position
        if action == 'N':
            y -= 1
        elif action == 'S':
            y += 1
        elif action == 'E':
            x += 1
        elif action == 'W':
            x -= 1
        elif action == 'NN':
            y -= 2
        elif action == 'SS':
            y += 2
        elif action == 'EE':
            x += 2
        elif action == 'WW':
            x -= 1

        if self.is_valid_move(x, y):
            self.player_position = (x, y)

    def goal_test(self, state):
        return self.maze[state[1]][state[0]] == REWARD

    def solve(self):
        start_state = self.get_start_position()
        current_state = start_state
        collected_prizes = 0

        while collected_prizes < self.num_prizes:
            action = input("Enter action (N (NN[2]), S(SS[2]), E(EE[2]), W(WW[2])) : ")
            self.transition(action)  # Update player's position based on action
            self.print_maze()
            
            # Check if a prize is collected at the new position
            if self.goal_test(self.player_position):
                collected_prizes += 1
                print(f"Prize collected! Total: {collected_prizes}/{self.num_prizes}")

    print("All prizes collected!")

if __name__ == "__main__":
    maze_solver = MazeSolver("maze.txt")
    maze_solver.solve()

