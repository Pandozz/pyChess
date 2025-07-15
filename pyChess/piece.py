from abc import ABC, abstractmethod

class Piece(ABC):
    
    def __init__(self, config):
        self.type = config.type
        self.color = config.color
        
        self.location = config.location
        self.isAlive = True
        
    def move(self, end_square, board) -> int:
        
        #Check if move is legal in subclass
        if not self.is_legal_move(end_square, board):
            return -1
    
        # Check if square is occupied by enemy, if so attack.
        if board.is_occupied(end_square) and board.occupant_color(end_square) != self.color:
            board.get_occupant(end_square).kill()
            board.clear(end_square)
        
        # Move if empty.
        if not board.is_occupied(end_square):
            self.location = end_square
            board.occupy_square(end_square)
            return
            
        # Otheriwse move is invalid, shouldn't get here technially
        return -1
        
    def is_alive(self) -> bool:
        return self.isAlive
     
    def kill(self) -> None:
        self.isAlive = False
    
    def get_location(self) -> tuple[int, int]:
        return self.location
    
    def set_location(self, square) -> None:
        self.location = square
    
    @abstractmethod
    def is_legal_move(self, end_square, board) -> bool:
        pass # override in subclass