from game.piece import Piece

class Bishop(Piece):
    
    def is_legal_move(self, end_square, board):
        # Check if move is on the board
        board.validate_square()

        # Any move must be within a diagonal
        if abs(end_square[1] - self.position[1]) != abs(end_square[0] - self.position[0]):
            return False
            
        return True
