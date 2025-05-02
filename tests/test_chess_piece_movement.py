"""
Unit tests for chess piece movement validation.
"""

import unittest
from chessboard.game_controller import GameController
from chessboard.chess_piece import ChessPiece


class TestChessPieceMovement(unittest.TestCase):
    """Test cases for chess piece movement validation."""

    def setUp(self):
        """Set up a game controller with an empty board for each test."""
        self.game = GameController()
        # Create an empty board
        self.game.board = self.game._create_empty_board()

    def test_pawn_movement(self):
        """Test pawn movement validation."""
        # Place a white pawn at e2 (row 6, col 4)
        self.game.board[6][4] = ChessPiece('white', 'pawn')

        # Valid moves: forward one square
        self.assertTrue(self.game.move_piece('e2', 'e3'))

        # Reset for next test
        self.setUp()

        # Place a white pawn at e2 (row 6, col 4)
        self.game.board[6][4] = ChessPiece('white', 'pawn')

        # Valid moves: forward two squares from starting position
        self.assertTrue(self.game.move_piece('e2', 'e4'))

        # Reset for next test
        self.setUp()

        # Place a white pawn at e3 (row 5, col 4) - not starting position
        self.game.board[5][4] = ChessPiece('white', 'pawn')

        # Invalid moves: forward two squares from non-starting position
        self.assertFalse(self.game.move_piece('e3', 'e5'))

        # Reset for next test
        self.setUp()

        # Place a white pawn at e2 (row 6, col 4) and a black piece at d3 (row 5, col 3)
        self.game.board[6][4] = ChessPiece('white', 'pawn')
        self.game.board[5][3] = ChessPiece('black', 'pawn')

        # Valid moves: diagonal capture
        self.assertTrue(self.game.move_piece('e2', 'd3'))

        # Reset for next test
        self.setUp()

        # Place a white pawn at e2 (row 6, col 4)
        self.game.board[6][4] = ChessPiece('white', 'pawn')

        # Invalid moves: diagonal move without capture
        self.assertFalse(self.game.move_piece('e2', 'd3'))

        # Reset for next test
        self.setUp()

        # Place a white pawn at e2 (row 6, col 4) and a white piece at e3 (row 5, col 4)
        self.game.board[6][4] = ChessPiece('white', 'pawn')
        self.game.board[5][4] = ChessPiece('white', 'knight')

        # Invalid moves: forward into occupied square
        self.assertFalse(self.game.move_piece('e2', 'e3'))

        # Reset for next test
        self.setUp()

        # Place a black pawn at e7 (row 1, col 4)
        self.game.board[1][4] = ChessPiece('black', 'pawn')

        # Set the current turn to black for this test
        self.game.current_turn = 'black'

        # Valid moves: forward one square (black pawn moves down)
        self.assertTrue(self.game.move_piece('e7', 'e6'))

    def test_rook_movement(self):
        """Test rook movement validation."""
        # Place a white rook at a1 (row 7, col 0)
        self.game.board[7][0] = ChessPiece('white', 'rook')

        # Valid moves: horizontal
        self.assertTrue(self.game.move_piece('a1', 'h1'))

        # Reset for next test
        self.setUp()

        # Place a white rook at a1 (row 7, col 0)
        self.game.board[7][0] = ChessPiece('white', 'rook')

        # Valid moves: vertical
        self.assertTrue(self.game.move_piece('a1', 'a8'))

        # Reset for next test
        self.setUp()

        # Place a white rook at d4 (row 4, col 3) and a piece at d6 (row 2, col 3)
        self.game.board[4][3] = ChessPiece('white', 'rook')
        self.game.board[2][3] = ChessPiece('black', 'pawn')

        # Valid moves: vertical with capture
        self.assertTrue(self.game.move_piece('d4', 'd6'))

        # Reset for next test
        self.setUp()

        # Place a white rook at d4 (row 4, col 3) and a piece at d6 (row 2, col 3)
        self.game.board[4][3] = ChessPiece('white', 'rook')
        self.game.board[2][3] = ChessPiece('black', 'pawn')

        # Invalid moves: vertical beyond a piece
        self.assertFalse(self.game.move_piece('d4', 'd8'))

        # Reset for next test
        self.setUp()

        # Place a white rook at d4 (row 4, col 3)
        self.game.board[4][3] = ChessPiece('white', 'rook')

        # Invalid moves: diagonal
        self.assertFalse(self.game.move_piece('d4', 'f6'))

    def test_knight_movement(self):
        """Test knight movement validation."""
        # Place a white knight at b1 (row 7, col 1)
        self.game.board[7][1] = ChessPiece('white', 'knight')

        # Valid moves: L-shape
        self.assertTrue(self.game.move_piece('b1', 'c3'))
        self.setUp()
        self.game.board[7][1] = ChessPiece('white', 'knight')
        self.assertTrue(self.game.move_piece('b1', 'a3'))

        # Reset for next test
        self.setUp()

        # Place a white knight at d4 (row 4, col 3)
        self.game.board[4][3] = ChessPiece('white', 'knight')

        # Valid moves: all possible L-shapes
        self.assertTrue(self.game.move_piece('d4', 'c2'))
        self.setUp()
        self.game.board[4][3] = ChessPiece('white', 'knight')
        self.assertTrue(self.game.move_piece('d4', 'e2'))
        self.setUp()
        self.game.board[4][3] = ChessPiece('white', 'knight')
        self.assertTrue(self.game.move_piece('d4', 'f3'))
        self.setUp()
        self.game.board[4][3] = ChessPiece('white', 'knight')
        self.assertTrue(self.game.move_piece('d4', 'f5'))
        self.setUp()
        self.game.board[4][3] = ChessPiece('white', 'knight')
        self.assertTrue(self.game.move_piece('d4', 'e6'))
        self.setUp()
        self.game.board[4][3] = ChessPiece('white', 'knight')
        self.assertTrue(self.game.move_piece('d4', 'c6'))
        self.setUp()
        self.game.board[4][3] = ChessPiece('white', 'knight')
        self.assertTrue(self.game.move_piece('d4', 'b5'))
        self.setUp()
        self.game.board[4][3] = ChessPiece('white', 'knight')
        self.assertTrue(self.game.move_piece('d4', 'b3'))

        # Reset for next test
        self.setUp()

        # Place a white knight at d4 (row 4, col 3)
        self.game.board[4][3] = ChessPiece('white', 'knight')

        # Invalid moves: non-L-shape
        self.assertFalse(self.game.move_piece('d4', 'd5'))
        self.assertFalse(self.game.move_piece('d4', 'e4'))
        self.assertFalse(self.game.move_piece('d4', 'f6'))

    def test_bishop_movement(self):
        """Test bishop movement validation."""
        # Place a white bishop at c1 (row 7, col 2)
        self.game.board[7][2] = ChessPiece('white', 'bishop')

        # Valid moves: diagonal
        self.assertTrue(self.game.move_piece('c1', 'a3'))
        self.setUp()
        self.game.board[7][2] = ChessPiece('white', 'bishop')
        self.assertTrue(self.game.move_piece('c1', 'h6'))

        # Reset for next test
        self.setUp()

        # Place a white bishop at d4 (row 4, col 3) and a piece at f6 (row 2, col 5)
        self.game.board[4][3] = ChessPiece('white', 'bishop')
        self.game.board[2][5] = ChessPiece('black', 'pawn')

        # Valid moves: diagonal with capture
        self.assertTrue(self.game.move_piece('d4', 'f6'))

        # Reset for next test
        self.setUp()

        # Place a white bishop at d4 (row 4, col 3) and a piece at f6 (row 2, col 5)
        self.game.board[4][3] = ChessPiece('white', 'bishop')
        self.game.board[2][5] = ChessPiece('black', 'pawn')

        # Invalid moves: diagonal beyond a piece
        self.assertFalse(self.game.move_piece('d4', 'h8'))

        # Reset for next test
        self.setUp()

        # Place a white bishop at d4 (row 4, col 3)
        self.game.board[4][3] = ChessPiece('white', 'bishop')

        # Invalid moves: non-diagonal
        self.assertFalse(self.game.move_piece('d4', 'd8'))
        self.assertFalse(self.game.move_piece('d4', 'h4'))

    def test_queen_movement(self):
        """Test queen movement validation."""
        # Place a white queen at d1 (row 7, col 3)
        self.game.board[7][3] = ChessPiece('white', 'queen')

        # Valid moves: horizontal
        self.assertTrue(self.game.move_piece('d1', 'h1'))

        # Reset for next test
        self.setUp()

        # Place a white queen at d1 (row 7, col 3)
        self.game.board[7][3] = ChessPiece('white', 'queen')

        # Valid moves: vertical
        self.assertTrue(self.game.move_piece('d1', 'd8'))

        # Reset for next test
        self.setUp()

        # Place a white queen at d1 (row 7, col 3)
        self.game.board[7][3] = ChessPiece('white', 'queen')

        # Valid moves: diagonal
        self.assertTrue(self.game.move_piece('d1', 'h5'))

        # Reset for next test
        self.setUp()

        # Place a white queen at d4 (row 4, col 3) and a piece at d6 (row 2, col 3)
        self.game.board[4][3] = ChessPiece('white', 'queen')
        self.game.board[2][3] = ChessPiece('black', 'pawn')

        # Valid moves: vertical with capture
        self.assertTrue(self.game.move_piece('d4', 'd6'))

        # Reset for next test
        self.setUp()

        # Place a white queen at d4 (row 4, col 3) and a piece at f6 (row 2, col 5)
        self.game.board[4][3] = ChessPiece('white', 'queen')
        self.game.board[2][5] = ChessPiece('black', 'pawn')

        # Valid moves: diagonal with capture
        self.assertTrue(self.game.move_piece('d4', 'f6'))

        # Reset for next test
        self.setUp()

        # Place a white queen at d4 (row 4, col 3) and a piece at d6 (row 2, col 3)
        self.game.board[4][3] = ChessPiece('white', 'queen')
        self.game.board[2][3] = ChessPiece('black', 'pawn')

        # Invalid moves: vertical beyond a piece
        self.assertFalse(self.game.move_piece('d4', 'd8'))

        # Reset for next test
        self.setUp()

        # Place a white queen at d4 (row 4, col 3)
        self.game.board[4][3] = ChessPiece('white', 'queen')

        # Invalid moves: non-straight, non-diagonal
        self.assertFalse(self.game.move_piece('d4', 'e6'))

    def test_king_movement(self):
        """Test king movement validation."""
        # Place a white king at e1 (row 7, col 4)
        self.game.board[7][4] = ChessPiece('white', 'king')

        # Valid moves: one square in any direction
        self.assertTrue(self.game.move_piece('e1', 'd1'))  # Left
        self.setUp()
        self.game.board[7][4] = ChessPiece('white', 'king')
        self.assertTrue(self.game.move_piece('e1', 'f1'))  # Right
        self.setUp()
        self.game.board[7][4] = ChessPiece('white', 'king')
        self.assertTrue(self.game.move_piece('e1', 'e2'))  # Up
        self.setUp()
        self.game.board[7][4] = ChessPiece('white', 'king')
        self.assertTrue(self.game.move_piece('e1', 'd2'))  # Diagonal

        # Reset for next test
        self.setUp()

        # Place a white king at e4 (row 4, col 4) and a black piece at e5 (row 3, col 4)
        self.game.board[4][4] = ChessPiece('white', 'king')
        self.game.board[3][4] = ChessPiece('black', 'pawn')

        # Valid moves: capture
        self.assertTrue(self.game.move_piece('e4', 'e5'))

        # Reset for next test
        self.setUp()

        # Place a white king at e4 (row 4, col 4)
        self.game.board[4][4] = ChessPiece('white', 'king')

        # Invalid moves: more than one square
        self.assertFalse(self.game.move_piece('e4', 'e6'))
        self.assertFalse(self.game.move_piece('e4', 'g4'))
        self.assertFalse(self.game.move_piece('e4', 'c2'))


if __name__ == '__main__':
    unittest.main()
