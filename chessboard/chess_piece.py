"""
Module for representing chess pieces on a chessboard.
"""

class ChessPiece:
    """
    Class representing a chess piece.

    Attributes:
        color (str): The color of the piece ('white' or 'black').
        piece_type (str): The type of the piece ('pawn', 'rook', 'knight', 'bishop', 'queen', 'king').
        symbol (str): The symbol representing the piece on the board.
    """

    def __init__(self, color, piece_type):
        """
        Initialize a chess piece.

        Args:
            color (str): The color of the piece ('white' or 'black').
            piece_type (str): The type of the piece ('pawn', 'rook', 'knight', 'bishop', 'queen', 'king').
        """
        self.color = color
        self.piece_type = piece_type

        # Define piece symbols
        pieces = {
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

        self.symbol = pieces[color][piece_type]

    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        """
        Check if a move is valid for this piece.

        Args:
            board (list): The current state of the board.
            from_row (int): The row index of the starting position.
            from_col (int): The column index of the starting position.
            to_row (int): The row index of the ending position.
            to_col (int): The column index of the ending position.

        Returns:
            tuple: (bool, str) - A tuple containing a boolean indicating if the move is valid,
                  and a string with an explanation if the move is invalid.
        """
        # Check if destination has a piece of the same color
        if isinstance(board[to_row][to_col], ChessPiece) and board[to_row][to_col].color == self.color:
            return False, f"Cannot capture your own {board[to_row][to_col].piece_type}."

        # Check specific piece movement rules
        if self.piece_type == 'pawn':
            return self._is_valid_pawn_move(board, from_row, from_col, to_row, to_col)
        elif self.piece_type == 'rook':
            return self._is_valid_rook_move(board, from_row, from_col, to_row, to_col)
        elif self.piece_type == 'knight':
            return self._is_valid_knight_move(board, from_row, from_col, to_row, to_col)
        elif self.piece_type == 'bishop':
            return self._is_valid_bishop_move(board, from_row, from_col, to_row, to_col)
        elif self.piece_type == 'queen':
            return self._is_valid_queen_move(board, from_row, from_col, to_row, to_col)
        elif self.piece_type == 'king':
            return self._is_valid_king_move(board, from_row, from_col, to_row, to_col)

        return False, "Unknown piece type."

    def _is_valid_pawn_move(self, board, from_row, from_col, to_row, to_col):
        """Check if a pawn move is valid."""
        # Determine direction based on color (white moves up, black moves down)
        direction = -1 if self.color == 'white' else 1

        # Check for forward movement (1 square)
        if from_col == to_col and to_row == from_row + direction:
            # Check if destination is empty
            if isinstance(board[to_row][to_col], str):
                return True, ""
            return False, "Cannot move forward into an occupied square."

        # Check for initial double move
        start_row = 6 if self.color == 'white' else 1
        if from_row == start_row and from_col == to_col and to_row == from_row + 2 * direction:
            # Check if both squares in front are empty
            if (isinstance(board[from_row + direction][from_col], str) and 
                isinstance(board[to_row][to_col], str)):
                return True, ""
            return False, "Cannot move forward two squares if path is blocked."

        # Check for diagonal capture
        if (to_row == from_row + direction and 
            (to_col == from_col - 1 or to_col == from_col + 1)):
            # Check if destination has an opponent's piece
            if (isinstance(board[to_row][to_col], ChessPiece) and 
                board[to_row][to_col].color != self.color):
                return True, ""
            return False, "Pawns can only move diagonally to capture an opponent's piece."

        return False, "Invalid pawn move. Pawns can move forward one square (or two from starting position) or diagonally to capture."

    def _is_valid_rook_move(self, board, from_row, from_col, to_row, to_col):
        """Check if a rook move is valid."""
        # Rooks move horizontally or vertically
        if from_row != to_row and from_col != to_col:
            return False, "Rooks can only move horizontally or vertically."

        # Check for obstacles in the path
        if from_row == to_row:  # Horizontal move
            start, end = min(from_col, to_col), max(from_col, to_col)
            for col in range(start + 1, end):
                if isinstance(board[from_row][col], ChessPiece):
                    return False, "Rook's path is blocked."
        else:  # Vertical move
            start, end = min(from_row, to_row), max(from_row, to_row)
            for row in range(start + 1, end):
                if isinstance(board[row][from_col], ChessPiece):
                    return False, "Rook's path is blocked."

        return True, ""

    def _is_valid_knight_move(self, board, from_row, from_col, to_row, to_col):
        """Check if a knight move is valid."""
        # Knights move in an L-shape: 2 squares in one direction, then 1 square perpendicular
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            return True, ""

        return False, "Knights move in an L-shape: 2 squares in one direction, then 1 square perpendicular."

    def _is_valid_bishop_move(self, board, from_row, from_col, to_row, to_col):
        """Check if a bishop move is valid."""
        # Bishops move diagonally
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        if row_diff != col_diff:
            return False, "Bishops can only move diagonally."

        # Check for obstacles in the path
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1

        row, col = from_row + row_step, from_col + col_step
        while row != to_row and col != to_col:
            if isinstance(board[row][col], ChessPiece):
                return False, "Bishop's path is blocked."
            row += row_step
            col += col_step

        return True, ""

    def _is_valid_queen_move(self, board, from_row, from_col, to_row, to_col):
        """Check if a queen move is valid."""
        # Queens can move like rooks or bishops
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        # Diagonal move (like bishop)
        if row_diff == col_diff:
            return self._is_valid_bishop_move(board, from_row, from_col, to_row, to_col)

        # Horizontal or vertical move (like rook)
        if from_row == to_row or from_col == to_col:
            return self._is_valid_rook_move(board, from_row, from_col, to_row, to_col)

        return False, "Queens can only move horizontally, vertically, or diagonally."

    def _is_valid_king_move(self, board, from_row, from_col, to_row, to_col):
        """Check if a king move is valid."""
        # Kings move one square in any direction
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        if row_diff <= 1 and col_diff <= 1:
            return True, ""

        return False, "Kings can only move one square in any direction."

    def __str__(self):
        """
        Return the string representation of the chess piece.

        Returns:
            str: The symbol representing the piece.
        """
        return self.symbol
