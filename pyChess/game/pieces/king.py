from game.piece import Piece

class King(Piece):
    
    def is_legal_move(self, end_square, board):
        # Check if move is on the board
        board.validate_square()

        dx = abs(end_square[1] - self.position[1])
        dy = abs(end_square[0] - self.position[0])
        
        # Any move must be within 1 square
        if dx > 1 or dy > 1:
            return False
            
        # TODO Handle Castling
        
        if self.color == 'white':
            if board.attacking_square(end_square, 'black'):
                return False
        else:
            if board.attacking_square(end_square, 'white'):
                return False
            
        return True
