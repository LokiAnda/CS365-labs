import random

# Define constants for player pieces
EMPTY = '.'
PLAYER1 = 'X'
PLAYER2 = 'O'

class BreakthroughGame:
    def __init__(self, rows=8, columns=8, num_rows_pieces=2):
        self.rows = rows
        self.columns = columns
        self.num_rows_pieces = num_rows_pieces
        self.state = self.initial_state()

    def initial_state(self):
        state = [[EMPTY] * self.columns for _ in range(self.rows)]
        for i in range(self.num_rows_pieces):
            state[i] = [PLAYER1] * self.columns
            state[self.rows - 1 - i] = [PLAYER2] * self.columns
        return state

    def is_game_over(self):
        # Check if any player has reached the last row or has no pieces left
        return any(row[0] == PLAYER1 for row in self.state) or any(row[-1] == PLAYER2 for row in self.state) \
            or not any(PLAYER1 in row for row in self.state) or not any(PLAYER2 in row for row in self.state)

    # Part 2-A: Minimax Algorithm
    def evasive_utility(state):
        own_pieces_remaining = sum(row.count(PLAYER1) for row in state)
        return own_pieces_remaining + random.random()

    def conqueror_utility(state):
        opponent_pieces_remaining = sum(row.count(PLAYER2) for row in state)
        return -(opponent_pieces_remaining + random.random())

    def minimax(game, depth, player, utility_func):
        if depth == 0 or game.is_game_over():
            return utility_func(game.state)

        best_value = float('-inf') if player == PLAYER1 else float('inf')
        moves = game.generate_moves(player)
    
        for move in moves:
            game.apply_move(move, player)
            value = minimax(game, depth - 1, PLAYER2 if player == PLAYER1 else PLAYER1, utility_func)
        game.apply_move((move[1], move[0]), player)  # Undo move
        
        if player == PLAYER1:
            best_value = max(best_value, value)
        else:
            best_value = min(best_value, value)

        return best_value

    def generate_moves(self, player):
        moves = []
        for row in range(self.rows):
            for col in range(self.columns):
                if self.state[row][col] == player:
                    # Add possible forward moves
                    if player == PLAYER1:
                        if row < self.rows - 1 and self.state[row + 1][col] == EMPTY:
                            moves.append(((row, col), (row + 1, col)))
                        if row < self.rows - 1 and col > 0 and self.state[row + 1][col - 1] == PLAYER2:
                            moves.append(((row, col), (row + 1, col - 1)))
                        if row < self.rows - 1 and col < self.columns - 1 and self.state[row + 1][col + 1] == PLAYER2:
                            moves.append(((row, col), (row + 1, col + 1)))
                    else:
                        if row > 0 and self.state[row - 1][col] == EMPTY:
                            moves.append(((row, col), (row - 1, col)))
                        if row > 0 and col > 0 and self.state[row - 1][col - 1] == PLAYER1:
                            moves.append(((row, col), (row - 1, col - 1)))
                        if row > 0 and col < self.columns - 1 and self.state[row - 1][col + 1] == PLAYER1:
                            moves.append(((row, col), (row - 1, col + 1)))
        return moves

    def apply_move(self, move, player):
        start, end = move
        self.state[end[0]][end[1]] = self.state[start[0]][start[1]]
        self.state[start[0]][start[1]] = EMPTY

    def display_state(self):
        print("Current Board State:")
        for row in self.state:
            print(' '.join(row))
        print()


    def play_game(heuristic_white, heuristic_black, board_state):
        game = BreakthroughGame()
        current_player = PLAYER1

        while not game.is_game_over():
            current_heuristic = heuristic_white if current_player == PLAYER1 else heuristic_black
            moves = game.generate_moves(current_player)
            best_move = None
            best_value = float('-inf') if current_player == PLAYER1 else float('inf')

            for move in moves:
                game.apply_move(move, current_player)
                value = minimax(game, 3, PLAYER2 if current_player == PLAYER1 else PLAYER1, current_heuristic)
                game.apply_move((move[1], move[0]), current_player)  # Undo move
            
                if (current_player == PLAYER1 and value > best_value) or (current_player == PLAYER2 and value < best_value):
                    best_move = move
                    best_value = value

                game.apply_move(best_move, current_player)
                current_player = PLAYER2 if current_player == PLAYER1 else PLAYER1

        print("Displaying state after move:")
        game.display_state()  # Display the state after each move
        print()  # Add an empty line between moves

        # Example usage:
        play_game(evasive_utility, conqueror_utility, None)


if __name__ == "__main__":
    # Create Breakthrough game with 8x8 board and 2 rows of pieces
    game = BreakthroughGame(rows=8, columns=8, num_rows_pieces=2)

    # Display initial state
    print("Initial State:")
    game.display_state()

    # Check if game is over
    print("Is game over?", game.is_game_over())

    # Generate moves for PLAYER1
    print("Possible moves for PLAYER1:")
    moves_player1 = game.generate_moves(PLAYER1)
    for move in moves_player1:
        print(move)

    # Generate moves for PLAYER2
    print("Possible moves for PLAYER2:")
    moves_player2 = game.generate_moves(PLAYER2)
    for move in moves_player2:
        print(move)


