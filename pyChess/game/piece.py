from abc import ABC, abstractmethod

class Piece(ABC):
    
    def __init__(self, config):
        self.id = config['id']
        self.type = config['type']
        self.color = config['color']
        
        self.position = config['position']
        self.isAlive = True
        
    def move(self, end_square, board) -> int:
        
        #Check if move is legal in subclass
        if not self.is_legal_move(end_square, board):
            return -1
    
        # Check if square is occupied by enemy, if so attack.
        if board.is_occupied(end_square) and board.get_occupant(end_square).get_color() != self.color:
            board.get_occupant(end_square).kill()
            board.remove_occupant(end_square)
        
        # Move if empty.
        if not board.is_occupied(end_square):
            self.position = end_square
            board.add_occupant(end_square)
            return
            
        # Otheriwse move is invalid, shouldn't get here technially
        return -1
        
    def is_alive(self) -> bool:
        return self.isAlive
     
    def kill(self) -> None:
        self.isAlive = False
    
    def get_position(self) -> tuple[int, int]:
        return self.position
    
    def set_position(self, square) -> None:
        self.position = square
        
    def get_color(self) -> str:
        return self.color
    
    def get_type(self) -> str:
        return self.type
    
    @abstractmethod
    def is_legal_move(self, end_square, board) -> bool:
        pass # override in subclass
    
    def __repr__(self):
        return f"Piece(id={self.id}, type={self.type}, color={self.color}, position={self.position})"