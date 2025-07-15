from game.board import Board
from game.pieces.pawn import Pawn
from game.pieces.knight import Knight
from game.pieces.bishop import Bishop
from game.pieces.rook import Rook
from game.pieces.queen import Queen
from game.pieces.king import King
from game.pieces.starting_pieces import starting_pieces

starting_piece_list = []

for piece in starting_pieces:
    if piece['type'] == 'pawn':
        starting_piece_list.append(Pawn(piece))
    elif piece['type'] == 'knight':
        starting_piece_list.append(Knight(piece))
    elif piece['type'] == 'bishop':
        starting_piece_list.append(Bishop(piece))
    elif piece['type'] == 'rook':
        starting_piece_list.append(Rook(piece))
    elif piece['type'] == 'queen':
        starting_piece_list.append(Queen(piece))
    elif piece['type'] == 'king':
        starting_piece_list.append(King(piece))
    else:
        raise ValueError(f"{piece['type']} is an invalid piece type.")

game_board = Board(starting_piece_list)
game_board.pretty_print_board_state()

pawn_a2 = game_board.get_occupant((2,2))

pawn_a2.move((4,2), game_board)
game_board.pretty_print_board_state()

pawn_a2 = game_board.get_occupant((4,2))

pawn_a2.move((5,2), game_board)
game_board.pretty_print_board_state()

pawn_a2 = game_board.get_occupant((5,2))

pawn_a2.move((6,2), game_board)
game_board.pretty_print_board_state()

pawn_a2 = game_board.get_occupant((6,2))

pawn_a2.move((7,3), game_board)
game_board.pretty_print_board_state()

pawn_a2 = game_board.get_occupant((7,3))

pawn_a2.move((8,2), game_board)
game_board.pretty_print_board_state()
