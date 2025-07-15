from collections import defaultdict
from game.piece import Piece

class Board():
     
    def __init__(self, pieces = []):
        self.board_state = defaultdict(Piece)
        self.rows = self.columns = [i for i in range(1, 9)]
        self.board_attack_status = defaultdict(set)
    
        for r in self.rows:
            for c in self.columns:
                self.board_state[(r,c)] = None
                self.board_attack_status[(r,c)] = set()
                
        for piece in pieces:
            self.add_occupant(piece.get_position(), piece)
                        
    def validate_square(self, square):
        if square[0] not in self.rows or square[1] not in self.columns:
            raise ValueError(f"{chr(square[1])}, {square[0]}) is not a valid square.")
        
    def get_rows(self): 
        return self.rows
    
    def get_columns(self):
        return self.columns
    
    def is_occupied(self, square):
        self.validate_square(square)
        return self.board_state[square] != None
    
    def get_occupant(self, square) -> Piece:
        self.validate_square(square)
        return self.board_state[square]
    
    def add_occupant(self, square, piece):
        self.validate_square(square)
        self.board_state[square] = piece
        
    def remove_occupant(self, square):
        self.validate_square(square)
        self.board_state[square].kill()
        self.board_state[square] = None
        
    def attacking_square(self, square, color):
        if color in self.board_attack_status[square]:
            return True
        return False

    def print_board_state(self):
        print(self.board_state)
        # TODO: Pretty print
    