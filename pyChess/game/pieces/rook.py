from game.piece import Piece


class Rook(Piece):

    def is_legal_move(self, end_square, board):
        # Check if move is on the board
        board.validate_square(end_square)

        # Any move must be either horizontal or vertical
        if end_square[0] != self.position[0] \
           and end_square[1] != self.position[1]:
            return False

        # Ensure there are no pieces in the way.
        return not board.check_linear_blocking(self.position, end_square)
