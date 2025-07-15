from game.piece import Piece


class Pawn(Piece):

    def __init__(self, config):
        super().__init__(config)

        self.start_square = config['position']

    def is_legal_move(self, end_square, board):
        # Check if move is on the board
        board.validate_square(end_square)

        # Handle first move
        if self.position == self.start_square and end_square[1] == self.position[1]:
            if board.is_occupied(end_square):
                return False
            if self.color == 'white':
                if end_square[0] > self.position[0] + 2:
                    return False
            if self.color == 'black':
                if end_square[0] < self.position[0] - 2:
                    return False
            return True

        # Any move must be within +- 1 column
        if end_square[1] > self.position[1] + 1 or end_square[1] < self.position[1] - 1:
            return False

        # Any non-first move must be 1 row further
        if self.color == 'white':
            if end_square[0] != self.position[0] + 1:
                return False
        if self.color == 'black':
            if end_square[0] != self.position[0] - 1:
                return False

        # Any non-attacking move must move to an unoccupied space
        if end_square[1] == self.position[1]:
            if board.is_occupied(end_square):
                return False
        # Any attacking move must move to an occupied space
        else:
            # TODO: Handle En-passant
            if not board.is_occupied(end_square):
                return False

        return True
