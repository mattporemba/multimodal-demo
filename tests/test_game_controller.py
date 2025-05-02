"""
Unit tests for the game_controller module.
"""

import unittest
from chessboard.game_controller import GameController
from chessboard.chess_piece import ChessPiece


class TestGameController(unittest.TestCase):
    """Test cases for the game_controller module."""

    def test_init(self):
        """Test initialization of the game controller."""
        game = GameController()
        self.assertEqual(game.size, 8)
        self.assertEqual(len(game.board), 8)
        for row in game.board:
            self.assertEqual(len(row), 8)

    def test_create_empty_board(self):
        """Test creation of an empty board with alternating pattern."""
        game = GameController(4)
        board = game._create_empty_board()

        # Expected pattern for a 4x4 chessboard
        expected = [
            ['□', '■', '□', '■'],
            ['■', '□', '■', '□'],
            ['□', '■', '□', '■'],
            ['■', '□', '■', '□']
        ]
        self.assertEqual(board, expected)

    def test_setup_pieces(self):
        """Test setting up pieces in their starting positions."""
        game = GameController()
        game.setup_pieces()

        # Test a few key positions
        self.assertIsInstance(game.board[0][0], ChessPiece)
        self.assertEqual(game.board[0][0].color, 'black')
        self.assertEqual(game.board[0][0].piece_type, 'rook')

        self.assertIsInstance(game.board[7][4], ChessPiece)
        self.assertEqual(game.board[7][4].color, 'white')
        self.assertEqual(game.board[7][4].piece_type, 'king')

        # Check pawns
        for j in range(8):
            self.assertIsInstance(game.board[1][j], ChessPiece)
            self.assertEqual(game.board[1][j].color, 'black')
            self.assertEqual(game.board[1][j].piece_type, 'pawn')

            self.assertIsInstance(game.board[6][j], ChessPiece)
            self.assertEqual(game.board[6][j].color, 'white')
            self.assertEqual(game.board[6][j].piece_type, 'pawn')

    def test_parse_position(self):
        """Test parsing chess positions to board coordinates."""
        game = GameController()

        # Test various positions
        self.assertEqual(game.parse_position('a1'), (7, 0))
        self.assertEqual(game.parse_position('h8'), (0, 7))
        self.assertEqual(game.parse_position('e4'), (4, 4))

        # Test invalid positions
        with self.assertRaises(ValueError):
            game.parse_position('i1')  # Column out of bounds

        with self.assertRaises(ValueError):
            game.parse_position('a9')  # Row out of bounds

        with self.assertRaises(ValueError):
            game.parse_position('a')  # Incomplete position

    def test_move_piece(self):
        """Test moving a piece on the board."""
        game = GameController()
        game.setup_pieces()

        # Move a pawn
        self.assertTrue(game.move_piece('a2', 'a4'))

        # Check that the piece moved
        self.assertIsInstance(game.board[4][0], ChessPiece)
        self.assertEqual(game.board[4][0].color, 'white')
        self.assertEqual(game.board[4][0].piece_type, 'pawn')

        # Check that the original position is now empty
        self.assertIsInstance(game.board[6][0], str)

        # Test moving from an empty square (should fail)
        self.assertFalse(game.move_piece('a2', 'a3'))

        # Test invalid positions (should return False)
        self.assertFalse(game.move_piece('i1', 'a3'))
        self.assertFalse(game.move_piece('a1', 'a9'))

    def test_turn_based_movement(self):
        """Test that turns alternate correctly between white and black."""
        game = GameController()
        game.setup_pieces()

        # Verify white moves first
        self.assertEqual(game.current_turn, 'white')

        # White's move (should succeed)
        self.assertTrue(game.move_piece('a2', 'a4'))

        # Verify turn switched to black
        self.assertEqual(game.current_turn, 'black')

        # Black's move (should succeed)
        self.assertTrue(game.move_piece('a7', 'a5'))

        # Verify turn switched back to white
        self.assertEqual(game.current_turn, 'white')

        # White tries to move black piece (should fail)
        self.assertFalse(game.move_piece('b7', 'b5'))

        # Verify turn still white
        self.assertEqual(game.current_turn, 'white')

        # White's move (should succeed)
        self.assertTrue(game.move_piece('b2', 'b4'))

        # Verify turn switched to black
        self.assertEqual(game.current_turn, 'black')

        # Black tries to move white piece (should fail)
        self.assertFalse(game.move_piece('c2', 'c4'))

        # Verify turn still black
        self.assertEqual(game.current_turn, 'black')


if __name__ == '__main__':
    unittest.main()
