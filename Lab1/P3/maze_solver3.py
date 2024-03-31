from queue import Queue, PriorityQueue

# Define constants for maze symbols
WALL = '%'
AGENT = 'P'
PRIZE = '.'

class MazeSolver:
    def __init__(self, maze_file):
        self.maze = self.load_maze(maze_file)
        self.start_position = self.find_start_position()
        self.goal_positions = self.find_goal_positions()
    
    def load_maze(self, maze_file):
        with open(maze_file, 'r') as f:
            return [list(line.strip()) for line in f.readlines()]

    def find_start_position(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == AGENT:
                    return (x, y)
        return None

    def find_goal_positions(self):
        goals = []
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == PRIZE:
                    goals.append((x, y))
        return goals

    def bfs(self):
        print("Running BFS...")
        visited = set()
        queue = Queue()
        queue.put((self.start_position, []))  # Queue stores position and path

        while not queue.empty():
            position, path = queue.get()
            x, y = position

            # Print current position being explored
            print("Exploring:", position)

            # Check if the current position is a goal
            if position in self.goal_positions:
                print("Goal found!")
                return path, len(path), len(visited)

            # Mark the current position as visited
            visited.add(position)

            # Generate next possible moves
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = x + dx, y + dy
                next_position = (next_x, next_y)

                # Check if the next position is valid and not visited
                if 0 <= next_x < len(self.maze[0]) and 0 <= next_y < len(self.maze) \
                        and self.maze[next_y][next_x] != WALL \
                        and next_position not in visited:
                    queue.put((next_position, path + [next_position]))

        # If no solution is found
        print("No solution found.")
        return None, -1, len(visited)

    def gbfs(self):
        print("Running Greedy Best-First Search (GBFS)...")
        visited = set()
        priority_queue = PriorityQueue()
        priority_queue.put((0, self.start_position, []))  # Queue stores (priority, position, path)

        while not priority_queue.empty():
            _, position, path = priority_queue.get()
            x, y = position

            # Print current position being explored
            print("Exploring:", position)

            # Check if the current position is a goal
            if position in self.goal_positions:
                print("Goal found!")
                return path, len(path), len(visited)

            # Mark the current position as visited
            visited.add(position)

            # Generate next possible moves
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = x + dx, y + dy
                next_position = (next_x, next_y)

                # Check if the next position is valid and not visited
                if 0 <= next_x < len(self.maze[0]) and 0 <= next_y < len(self.maze) \
                        and self.maze[next_y][next_x] != WALL \
                        and next_position not in visited:
                    # Calculate priority using Manhattan distance heuristic
                    priority = self.manhattan_distance(next_position, self.goal_positions[0])
                    priority_queue.put((priority, next_position, path + [next_position]))

        # If no solution is found
        print("No solution found.")
        return None, -1, len(visited)

    def astar(self):
        print("Running A* Search...")
        visited = set()
        priority_queue = PriorityQueue()
        priority_queue.put((0, self.start_position, []))  # Queue stores (priority, position, path)

        while not priority_queue.empty():
            _, position, path = priority_queue.get()
            x, y = position

            # Print current position being explored
            print("Exploring:", position)

            # Check if the current position is a goal
            if position in self.goal_positions:
                print("Goal found!")
                return path, len(path), len(visited)

            # Mark the current position as visited
            visited.add(position)

            # Generate next possible moves
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = x + dx, y + dy
                next_position = (next_x, next_y)

                # Check if the next position is valid and not visited
                if 0 <= next_x < len(self.maze[0]) and 0 <= next_y < len(self.maze) \
                        and self.maze[next_y][next_x] != WALL \
                        and next_position not in visited:
                    # Calculate priority using Manhattan distance heuristic and path cost
                    priority = len(path) + self.manhattan_distance(next_position, self.goal_positions[0])
                    priority_queue.put((priority, next_position, path + [next_position]))

        # If no solution is found
        print("No solution found.")
        return None, -1, len(visited)

    def manhattan_distance(self, position1, position2):
        x1, y1 = position1
        x2, y2 = position2
        return abs(x1 - x2) + abs(y1 - y2)

    def display_solution(self, solution_path, path_cost, expanded_nodes):
        if solution_path is None:
            print("No solution found.")
            return
    
        print("Solution Path:")
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if (x, y) in solution_path:
                    print("#", end="")
                else:
                    print(cell, end="")
            print()
        print("Path Cost:", path_cost)
        print("Expanded Nodes:", expanded_nodes)

if __name__ == "__main__":
    maze_solver = MazeSolver("maze.txt")
    maze_solver.bfs()
    maze_solver.gbfs()
    maze_solver.astar()
