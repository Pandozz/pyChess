
# Piece = {id:x, type:x, color:x, location:x}
# Board = {}

def index_to_file(index):
    """Convert file index 1-8 to letter a-h"""
    return chr(ord('a') + index - 1)

chess_pieces = []

# White major pieces on rank 1
white_back_rank = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
for file_index, abbrev in enumerate(white_back_rank, start=1):
    square = f"{index_to_file(file_index)}1"
    piece_info = {
        'id': f"{abbrev}{square}",
        'type': {'R': 'rook', 'N': 'knight', 'B': 'bishop', 'Q': 'queen', 'K': 'king'}[abbrev],
        'color': 'white',
        'position': (1, file_index)
    }
    chess_pieces.append(piece_info)

# White pawns on rank 2
for file_index in range(1, 9):
    file_letter = index_to_file(file_index)
    square = f"{file_letter}2"
    chess_pieces.append({
        'id': f"P{square}",
        'type': 'pawn',
        'color': 'white',
        'position': (2, file_index)
    })

# Black major pieces on rank 8
black_back_rank = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
for file_index, abbrev in enumerate(black_back_rank, start=1):
    square = f"{index_to_file(file_index)}8"
    piece_info = {
        'id': f"{abbrev}{square}",
        'type': {'R': 'rook', 'N': 'knight', 'B': 'bishop', 'Q': 'queen', 'K': 'king'}[abbrev],
        'color': 'black',
        'position': (8, file_index)
    }
    chess_pieces.append(piece_info)

# Black pawns on rank 7
for file_index in range(1, 9):
    file_letter = index_to_file(file_index)
    square = f"{file_letter}7"
    chess_pieces.append({
        'id': f"P{square}",
        'type': 'pawn',
        'color': 'black',
        'position': (7, file_index)
    })

# Optional: print out the result
for piece in chess_pieces:
    print(piece)
