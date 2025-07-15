from game.piece import Piece

class Knight(Piece):
    
    def is_legal_move(self, end_square, board):
        # Check if move is on the board
        board.validate_square(end_square)

        # Any move must be within a 2x1 L shape
        dx = abs(end_square[1] - self.position[1])
        dy = abs(end_square[0] - self.position[0])

        return (dx, dy) in [(2, 1), (1, 2)]
