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
        current_turn (str): The color of the player whose turn it is ('white' or 'black').
        in_check (str or None): The color of the player whose king is in check, or None if no king is in check.
        checkmate (str or None): The color of the player whose king is in checkmate, or None if no king is in checkmate.
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
        self.in_check = None
        self.checkmate = None

    def reset_game(self):
        """
        Reset the game to its initial state.

        Returns:
            None
        """
        self.board = self._create_empty_board()
        self.setup_pieces()
        self.current_turn = 'white'  # White always moves first
        self.in_check = None
        self.checkmate = None

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

    def find_king_position(self, color):
        """
        Find the position of the king of the specified color.

        Args:
            color (str): The color of the king to find ('white' or 'black').

        Returns:
            tuple or None: A tuple of (row, col) if the king is found, None otherwise.
        """
        for row in range(self.size):
            for col in range(self.size):
                piece = self.board[row][col]
                if (isinstance(piece, ChessPiece) and 
                    piece.color == color and 
                    piece.piece_type == 'king'):
                    return row, col
        return None

    def is_position_under_attack(self, row, col, by_color):
        """
        Check if a position is under attack by pieces of the specified color.

        Args:
            row (int): The row index of the position to check.
            col (int): The column index of the position to check.
            by_color (str): The color of the attacking pieces ('white' or 'black').

        Returns:
            bool: True if the position is under attack, False otherwise.
        """
        for attacker_row in range(self.size):
            for attacker_col in range(self.size):
                piece = self.board[attacker_row][attacker_col]
                if (isinstance(piece, ChessPiece) and 
                    piece.color == by_color):
                    # Check if this piece can attack the specified position
                    is_valid, _ = piece.is_valid_move(self.board, attacker_row, attacker_col, row, col)
                    if is_valid:
                        return True
        return False

    def is_in_check(self, color):
        """
        Check if the king of the specified color is in check.

        Args:
            color (str): The color of the king to check ('white' or 'black').

        Returns:
            bool: True if the king is in check, False otherwise.
        """
        # Find the king's position
        king_pos = self.find_king_position(color)
        if king_pos is None:
            return False

        # Check if the king is under attack by the opponent's pieces
        opponent_color = 'black' if color == 'white' else 'white'
        return self.is_position_under_attack(king_pos[0], king_pos[1], opponent_color)

    def would_move_cause_check(self, from_row, from_col, to_row, to_col, color):
        """
        Check if a move would leave the king of the specified color in check.

        Args:
            from_row (int): The row index of the starting position.
            from_col (int): The column index of the starting position.
            to_row (int): The row index of the ending position.
            to_col (int): The column index of the ending position.
            color (str): The color of the king to check ('white' or 'black').

        Returns:
            bool: True if the move would leave the king in check, False otherwise.
        """
        # Save the current state of the board
        original_from = self.board[from_row][from_col]
        original_to = self.board[to_row][to_col]

        # Make the move temporarily
        self.board[to_row][to_col] = original_from
        if (from_row + from_col) % 2 == 0:
            self.board[from_row][from_col] = '□'  # White square
        else:
            self.board[from_row][from_col] = '■'  # Black square

        # Check if the king is in check after the move
        in_check = self.is_in_check(color)

        # Restore the original state of the board
        self.board[from_row][from_col] = original_from
        self.board[to_row][to_col] = original_to

        return in_check

    def is_checkmate(self, color):
        """
        Check if the king of the specified color is in checkmate.

        Args:
            color (str): The color of the king to check ('white' or 'black').

        Returns:
            bool: True if the king is in checkmate, False otherwise.
        """
        # If the king is not in check, it's not checkmate
        if not self.is_in_check(color):
            return False

        # Find the king's position
        king_pos = self.find_king_position(color)
        if king_pos is None:
            return False

        king_row, king_col = king_pos

        # Check if the king can move to any adjacent square
        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:
                if row_offset == 0 and col_offset == 0:
                    continue  # Skip the current position

                to_row = king_row + row_offset
                to_col = king_col + col_offset

                # Check if the position is on the board
                if 0 <= to_row < self.size and 0 <= to_col < self.size:
                    # Check if the move is valid according to chess rules
                    king = self.board[king_row][king_col]
                    is_valid, _ = king.is_valid_move(self.board, king_row, king_col, to_row, to_col)

                    if is_valid:
                        # Check if the move would get the king out of check
                        if not self.would_move_cause_check(king_row, king_col, to_row, to_col, color):
                            return False  # Found a move that gets the king out of check

        # Check if any other piece can block the check or capture the attacking piece
        opponent_color = 'black' if color == 'white' else 'white'

        for from_row in range(self.size):
            for from_col in range(self.size):
                piece = self.board[from_row][from_col]
                if (isinstance(piece, ChessPiece) and piece.color == color and piece.piece_type != 'king'):
                    # Try all possible moves for this piece
                    for to_row in range(self.size):
                        for to_col in range(self.size):
                            # Check if the move is valid according to chess rules
                            is_valid, _ = piece.is_valid_move(self.board, from_row, from_col, to_row, to_col)
                            if is_valid:
                                # Check if the move would get the king out of check
                                if not self.would_move_cause_check(from_row, from_col, to_row, to_col, color):
                                    return False  # Found a move that gets the king out of check

        # If no move can get the king out of check, it's checkmate
        return True

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

            # Check if the move would leave the king in check
            if self.would_move_cause_check(from_row, from_col, to_row, to_col, piece.color):
                if self.in_check == piece.color:
                    print(f"Your king is in check! You must make a move to get out of check.")
                else:
                    print(f"Invalid move: This would leave your king in check.")
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

            # Check if the opponent is now in check or checkmate
            opponent_color = 'black' if piece.color == 'white' else 'white'

            # Reset check status
            self.in_check = None

            # Check for check
            if self.is_in_check(opponent_color):
                self.in_check = opponent_color
                print(f"{opponent_color.capitalize()} is in check!")

                # Check for checkmate
                if self.is_checkmate(opponent_color):
                    self.checkmate = opponent_color
                    print(f"Checkmate! {piece.color.capitalize()} wins! Congratulations!")
                    return "checkmate"

            return True

        except ValueError as e:
            print(f"Error: {e}")
            return False
