class MazeSolver:
    def __init__(self, maze_file):
        self.maze = self.load_maze(maze_file)
        self.visited = set()
        self.num_nodes_expanded = 0
        self.path = []

    def load_maze(self, maze_file):
        with open(maze_file, 'r') as f:
            return [list(line.strip()) for line in f.readlines()]

    def get_start_position(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 'P':
                    return x, y
        return None

    def single_dfs(self, start):
        stack = [(start, [])]

        while stack:
            current, path = stack.pop()
            x, y = current
            self.num_nodes_expanded += 1

            if self.maze[y][x] == '.':
                self.path = path
                return

            if current in self.visited or self.maze[y][x] == '%':
                continue

            self.visited.add(current)

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.maze[0]) and 0 <= ny < len(self.maze):
                    stack.append(((nx, ny), path + [(nx, ny)]))

    def display_solution(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if (x, y) in self.path:
                    print('#', end='')
                else:
                    print(cell, end='')
            print()
        
        print(f"Path cost: {len(self.path)}")
        print(f"Nodes expanded: {self.num_nodes_expanded}")

if __name__ == "__main__":
    maze_solver = MazeSolver("maze.txt")
    start_position = maze_solver.get_start_position()
    maze_solver.single_dfs(start_position)
    maze_solver.display_solution()
