class EightQueens:
    def __init__(self, size=8):
        self.size = size

    def is_safe(self, board, row, col):
        """Check if placing a queen at board[row][col] is safe."""
        for i in range(col):
            if board[row][i] == 1:  # Check this row on the left
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):  # Check upper diagonal
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.size), range(col, -1, -1)):  # Check lower diagonal
            if board[i][j] == 1:
                return False

        return True

    def alpha_beta_search(self, board, col, alpha, beta, maximizing_player):
        """Alpha-Beta Pruning Search."""
        if col >= self.size:  # If all queens are placed
            return 0, [row[:] for row in board]  # Return 0 as heuristic since it's a valid solution

        if maximizing_player:
            max_eval = float('-inf')
            best_board = None
            for row in range(self.size):
                if self.is_safe(board, row, col):
                    board[row][col] = 1
                    eval_score, potential_board = self.alpha_beta_search(board, col + 1, alpha, beta, False)
                    board[row][col] = 0
                    if eval_score > max_eval:
                        max_eval = eval_score
                        best_board = potential_board
                    alpha = max(alpha, eval_score)
                    if beta <= alpha:  # Beta cutoff
                        break
            return max_eval, best_board
        else:
            min_eval = float('inf')
            best_board = None
            for row in range(self.size):
                if self.is_safe(board, row, col):
                    board[row][col] = 1
                    eval_score, potential_board = self.alpha_beta_search(board, col + 1, alpha, beta, True)
                    board[row][col] = 0
                    if eval_score < min_eval:
                        min_eval = eval_score
                        best_board = potential_board
                    beta = min(beta, eval_score)
                    if beta <= alpha:  # Alpha cutoff
                        break
            return min_eval, best_board

    def solve(self):
        """Solve the 8-Queens problem."""
        board = [[0] * self.size for _ in range(self.size)]
        _, solution = self.alpha_beta_search(board, 0, float('-inf'), float('inf'), True)
        return solution

    def print_board(self, board):
        """Print the chessboard."""
        for row in board:
            print(" ".join("Q" if col else "." for col in row))
        print()


if __name__ == "__main__":
    game = EightQueens()
    solution = game.solve()
    if solution:
        print("Solution found:")
        game.print_board(solution)
    else:
        print("No solution exists.")
