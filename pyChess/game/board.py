from collections import defaultdict
from game.piece import Piece


class Board():

    def __init__(self, pieces = []):
        self.board_state = defaultdict(Piece)
        self.rows = self.columns = [i for i in range(1, 9)]
        self.board_attack_status = defaultdict(set)

        for r in self.rows:
            for c in self.columns:
                self.board_state[(r, c)] = None
                self.board_attack_status[(r, c)] = set()

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
        return self.board_state[square] is not None

    def get_occupant(self, square) -> Piece:
        self.validate_square(square)
        return self.board_state[square]

    def add_occupant(self, square, piece):
        self.validate_square(square)
        self.board_state[square] = piece

    def remove_occupant(self, square):
        self.validate_square(square)
        self.board_state[square] = None

    def attacking_square(self, square, color):
        if color in self.board_attack_status[square]:
            return True
        return False

    def check_linear_blocking(self, start_square, end_square):
        dx = end_square[1] - start_square[1]
        dy = end_square[0] - start_square[0]

        if dx:
            squares_to_check = [(start_square[0], start_square[1] + i) if dx > 0 else (start_square[0], start_square[1] - i) for i in range(1, abs(dx))]
            print(squares_to_check)
            for square in squares_to_check:
                if self.is_occupied(square):
                    raise ValueError(f"Linear move {start_square} to {end_square} not valid, blocked by {square}")

        if dy:
            squares_to_check = [(start_square[0] + i, start_square[1]) if dy > 0 else (start_square[0] - i, start_square[1]) for i in range(1, abs(dy))]
            print(squares_to_check)
            for square in squares_to_check:
                if self.is_occupied(square):
                    raise ValueError(f"Linear move {start_square} to {end_square} not valid, blocked by {square}")

        return False

    def check_diagonal_blocking(self, start_square, end_square):
        dx = end_square[1] - start_square[1]
        dy = end_square[0] - start_square[0]

        x_vals = []
        y_vals = []

        if dx < 0:
            x_vals = list(range(-1, dx, -1))
        else:
            x_vals = list(range(1, dx))

        if dy < 0:
            y_vals = list(range(-1, dy, -1))
        else:
            y_vals = list(range(1, dy))

        squares_to_check = [(start_square[0] + y, start_square[1] + x) for x, y in zip(x_vals, y_vals)]

        for square in squares_to_check:
            if self.is_occupied(square):
                raise ValueError(f"Diagonal move {start_square} to {end_square} not valid, blocked by {square}")

        return False

    # PRINTING FUNCTIONS

    def print_board_state(self):
        print(self.board_state)
        # TODO: Pretty print

    def pretty_print_board_state(self):
        # Create an 8x8 grid initialized with empty spaces
        board = [['.' for _ in range(8)] for _ in range(8)]

        # Map piece types to symbols
        piece_symbols = {
            'pawn': 'P',
            'rook': 'R',
            'knight': 'N',
            'bishop': 'B',
            'queen': 'Q',
            'king': 'K'
        }

        # Place each piece on the board
        for loc, piece in self.board_state.items():
            if not piece:
                continue
            rank, file = loc
            symbol = piece_symbols.get(piece.get_type())
            # Use uppercase for white, lowercase for black
            if piece.get_color() == 'black':
                symbol = symbol.lower()
            board[8 - rank][file - 1] = symbol  # flip rank for display (rank 8 at top)

        # Print the board with ranks and files
        print("  a b c d e f g h")
        for idx, row in enumerate(board):
            print(f"{8 - idx} {' '.join(row)} {8 - idx}")
        print("  a b c d e f g h")
        print("")
