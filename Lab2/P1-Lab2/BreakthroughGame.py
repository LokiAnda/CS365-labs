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

    def display_state(self):
        for row in self.state:
            print(''.join(row))
        print()

    def is_game_over(self):
        # Check if any player has reached the last row or has no pieces left
        return any(row[0] == PLAYER1 for row in self.state) or any(row[-1] == PLAYER2 for row in self.state) \
            or not any(PLAYER1 in row for row in self.state) or not any(PLAYER2 in row for row in self.state)

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
