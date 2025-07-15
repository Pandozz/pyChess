from game.piece import Piece

class Queen(Piece):
    
    def is_legal_move(self, end_square, board):
        # Check if move is on the board
        board.validate_square()

        # Any move must be either diagonal, or straight
        dx = abs(end_square[1] - self.position[1])
        dy = abs(end_square[0] - self.position[0])

        # If it's not diagonal AND not straight, it's invalid
        if dx != dy and end_square[0] != self.position[0] and end_square[1] != self.position[1]:
            return False
        
        return True
