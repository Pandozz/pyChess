from game.piece import Piece


class Bishop(Piece):

    def is_legal_move(self, end_square, board):
        # Check if move is on the board
        board.validate_square(end_square)

        # Any move must be within a diagonal
        if abs(end_square[1] - self.position[1]) != abs(end_square[0] - self.position[0]):
            return False

        # Ensure there are no pieces in the way.
        return not board.check_diagonal_blocking(self.position, end_square)
