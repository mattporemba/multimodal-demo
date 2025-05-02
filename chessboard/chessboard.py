"""
Module for generating and displaying a 2D representation of a chessboard.
"""

# Define chess pieces
PIECES = {
    'white': {
        'pawn': 'wP',
        'rook': 'wR',
        'knight': 'wKn',
        'bishop': 'wB',
        'queen': 'wQ',
        'king': 'wKi'
    },
    'black': {
        'pawn': 'bP',
        'rook': 'bR',
        'knight': 'bKn',
        'bishop': 'bB',
        'queen': 'bQ',
        'king': 'bKi'
    }
}

def generate_chessboard(size=8, with_pieces=False):
    """
    Generate a 2D representation of a chessboard with optional pieces in starting position.

    Args:
        size (int): The size of the chessboard (default: 8x8).
        with_pieces (bool): Whether to include chess pieces in their starting positions (default: False).

    Returns:
        list: A 2D list representing the chessboard, where '■' represents black squares
             and '□' represents white squares. Pieces are represented by their color and type if with_pieces is True.
    """
    chessboard = []
    for i in range(size):
        row = []
        for j in range(size):
            # If the sum of row and column indices is even, it's a white square
            # Otherwise, it's a black square
            if (i + j) % 2 == 0:
                row.append('□')  # White square
            else:
                row.append('■')  # Black square
        chessboard.append(row)

    # Only add pieces if requested and it's a standard 8x8 chessboard
    if with_pieces and size == 8:
        # Add black pieces (top of the board)
        chessboard[0][0] = PIECES['black']['rook']
        chessboard[0][1] = PIECES['black']['knight']
        chessboard[0][2] = PIECES['black']['bishop']
        chessboard[0][3] = PIECES['black']['queen']
        chessboard[0][4] = PIECES['black']['king']
        chessboard[0][5] = PIECES['black']['bishop']
        chessboard[0][6] = PIECES['black']['knight']
        chessboard[0][7] = PIECES['black']['rook']

        # Add black pawns
        for j in range(8):
            chessboard[1][j] = PIECES['black']['pawn']

        # Add white pawns
        for j in range(8):
            chessboard[6][j] = PIECES['white']['pawn']

        # Add white pieces (bottom of the board)
        chessboard[7][0] = PIECES['white']['rook']
        chessboard[7][1] = PIECES['white']['knight']
        chessboard[7][2] = PIECES['white']['bishop']
        chessboard[7][3] = PIECES['white']['queen']
        chessboard[7][4] = PIECES['white']['king']
        chessboard[7][5] = PIECES['white']['bishop']
        chessboard[7][6] = PIECES['white']['knight']
        chessboard[7][7] = PIECES['white']['rook']

    return chessboard


def display_chessboard(chessboard):
    """
    Display a 2D representation of a chessboard with grid markings.

    Args:
        chessboard (list): A 2D list representing the chessboard.
    """
    # Add 5 lines of whitespace before displaying the board
    for _ in range(5):
        print()

    size = len(chessboard)

    # Find the maximum width of any piece representation
    max_width = 3  # "bKn" and "wKn" are 3 characters wide

    # Column labels (a-h for standard 8x8 board)
    padded_labels = [f"{chr(97 + j):{max_width}s}" for j in range(size)]
    col_labels = '  ' + ' '.join(padded_labels)
    print(col_labels)

    # Print each row with row numbers
    for i, row in enumerate(chessboard):
        # Row number (8 to 1 from top to bottom)
        row_num = size - i
        # Pad each element to have the same width
        padded_row = []
        for cell in row:
            # Convert cell to string if it's not already a string
            cell_str = str(cell)
            padded_row.append(f"{cell_str:{max_width}s}")
        print(f"{row_num} {' '.join(padded_row)} {row_num}")

    # Column labels again at the bottom
    print(col_labels)


def main():
    """
    Main function to generate and display a chessboard.
    """
    print("Chessboard Representation:")
    chessboard = generate_chessboard()
    display_chessboard(chessboard)


if __name__ == "__main__":
    main()
