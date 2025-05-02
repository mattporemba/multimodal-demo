"""
Module for controlling the chess game, including piece movement and game state.
"""

from chessboard.chess_piece import ChessPiece

class GameController:
    """
    Class for controlling the chess game.

    Attributes:
        board (list): A 2D list representing the chessboard with pieces.
        size (int): The size of the chessboard (default: 8x8).
    """

    def __init__(self, size=8):
        """
        Initialize the game controller with an empty board.

        Args:
            size (int): The size of the chessboard (default: 8x8).
        """
        self.size = size
        self.board = self._create_empty_board()
        self.current_turn = 'white'  # White always moves first

    def _create_empty_board(self):
        """
        Create an empty chessboard with alternating white and black squares.

        Returns:
            list: A 2D list representing the empty chessboard.
        """
        board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                # If the sum of row and column indices is even, it's a white square
                # Otherwise, it's a black square
                if (i + j) % 2 == 0:
                    row.append('□')  # White square
                else:
                    row.append('■')  # Black square
            board.append(row)
        return board

    def setup_pieces(self):
        """
        Set up the chess pieces in their starting positions.
        """
        # Add black pieces (top of the board)
        self.board[0][0] = ChessPiece('black', 'rook')
        self.board[0][1] = ChessPiece('black', 'knight')
        self.board[0][2] = ChessPiece('black', 'bishop')
        self.board[0][3] = ChessPiece('black', 'queen')
        self.board[0][4] = ChessPiece('black', 'king')
        self.board[0][5] = ChessPiece('black', 'bishop')
        self.board[0][6] = ChessPiece('black', 'knight')
        self.board[0][7] = ChessPiece('black', 'rook')

        # Add black pawns
        for j in range(8):
            self.board[1][j] = ChessPiece('black', 'pawn')

        # Add white pawns
        for j in range(8):
            self.board[6][j] = ChessPiece('white', 'pawn')

        # Add white pieces (bottom of the board)
        self.board[7][0] = ChessPiece('white', 'rook')
        self.board[7][1] = ChessPiece('white', 'knight')
        self.board[7][2] = ChessPiece('white', 'bishop')
        self.board[7][3] = ChessPiece('white', 'queen')
        self.board[7][4] = ChessPiece('white', 'king')
        self.board[7][5] = ChessPiece('white', 'bishop')
        self.board[7][6] = ChessPiece('white', 'knight')
        self.board[7][7] = ChessPiece('white', 'rook')

    def get_board(self):
        """
        Get the current state of the board.

        Returns:
            list: A 2D list representing the current state of the chessboard.
        """
        return self.board

    def parse_position(self, position):
        """
        Parse a chess position (e.g., 'a1') into board coordinates.

        Args:
            position (str): A chess position in algebraic notation (e.g., 'a1').

        Returns:
            tuple: A tuple of (row, column) indices for the board.
        """
        if len(position) != 2:
            raise ValueError(f"Invalid position: {position}. Position must be in the format 'a1'.")

        col = ord(position[0].lower()) - ord('a')
        row = self.size - int(position[1])

        if not (0 <= row < self.size and 0 <= col < self.size):
            raise ValueError(f"Position {position} is out of bounds.")

        return row, col

    def move_piece(self, from_pos, to_pos):
        """
        Move a piece from one position to another.

        Args:
            from_pos (str): The starting position in algebraic notation (e.g., 'a2').
            to_pos (str): The ending position in algebraic notation (e.g., 'a4').

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        try:
            from_row, from_col = self.parse_position(from_pos)
            to_row, to_col = self.parse_position(to_pos)

            # Check if there's a piece at the starting position
            if isinstance(self.board[from_row][from_col], str):
                print(f"No piece at position {from_pos}.")
                return False

            # Get the piece
            piece = self.board[from_row][from_col]

            # Check if it's the correct player's turn
            if piece.color != self.current_turn:
                print(f"It's {self.current_turn}'s turn to move, not {piece.color}'s.")
                return False

            # Check if the move is valid according to chess rules
            is_valid, explanation = piece.is_valid_move(self.board, from_row, from_col, to_row, to_col)

            if not is_valid:
                print(f"Invalid move: {explanation}")
                print(f"The {piece.color} {piece.piece_type} at {from_pos} cannot move to {to_pos}.")
                return False

            # Move the piece
            self.board[to_row][to_col] = piece

            # Set the original position to an empty square
            if (from_row + from_col) % 2 == 0:
                self.board[from_row][from_col] = '□'  # White square
            else:
                self.board[from_row][from_col] = '■'  # Black square

            # Toggle the turn
            self.current_turn = 'black' if self.current_turn == 'white' else 'white'

            return True

        except ValueError as e:
            print(f"Error: {e}")
            return False
