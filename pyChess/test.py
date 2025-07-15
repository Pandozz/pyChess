from game.board import Board
from game.pieces.pawn import Pawn
from game.pieces.knight import Knight
from game.pieces.bishop import Bishop
from game.pieces.rook import Rook
from game.pieces.queen import Queen
from game.pieces.king import King
from game.pieces.starting_pieces import starting_pieces

import pytest


@pytest.fixture
def game_board():
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

    return Board(starting_piece_list)


class TestChess():

    def test_pawn_move(self, game_board):

        starting_square = (2, 2)
        target_square = (4, 2)
        pawn = game_board.get_occupant(starting_square)
        id = pawn.get_id()

        pawn.move(target_square, game_board)
        assert (game_board.is_occupied((target_square)))
        assert (game_board.get_occupant(target_square).get_id() == id)

        assert (not game_board.is_occupied((starting_square)))
        assert (game_board.get_occupant((starting_square)) is None)

    def test_bishop_move(self, game_board):
        starting_square = (1, 3)
        open_square = (3, 1)
        blocked_square = (8, 6)

        game_board.pretty_print_board_state()
        bishop = game_board.get_occupant(starting_square)
        id = bishop.get_id()

        with pytest.raises(ValueError):
            bishop.move(open_square, game_board)

        game_board.pretty_print_board_state()

        starting_square2 = (2, 2)
        target_square2 = (4, 2)
        pawn = game_board.get_occupant(starting_square2)
        pawn.move(target_square2, game_board)

        game_board.pretty_print_board_state()

        bishop = game_board.get_occupant(starting_square)
        bishop.move(open_square, game_board)

        game_board.pretty_print_board_state()
        assert (game_board.is_occupied((open_square)))
        assert (game_board.get_occupant(open_square).get_id() == id)

        assert (not game_board.is_occupied((starting_square)))
        assert (game_board.get_occupant((starting_square)) is None)

        bishop = game_board.get_occupant(open_square)
        with pytest.raises(ValueError):
            bishop.move(blocked_square, game_board)
