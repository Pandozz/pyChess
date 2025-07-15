from game.board import Board
from game.pieces.pawn import Pawn
from game.pieces.starting_pieces import starting_pieces

starting_piece_list = []

for piece in starting_pieces:
    if piece['type'] == 'pawn':
        starting_piece_list.append(Pawn(piece))
    elif piece['type'] == 'knight':
        pass
    elif piece['type'] == 'bishop':
        pass
    elif piece['type'] == 'rook':
        pass
    elif piece['type'] == 'queen':
        pass
    elif piece['type'] == 'king':
        pass
    else:
        raise ValueError(f"{piece['type']} is an invalid piece type.")

game_board = Board(starting_piece_list)

game_board.print_board_state()

