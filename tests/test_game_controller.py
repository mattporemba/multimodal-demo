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


    def test_check_detection(self):
        """Test detection of check conditions."""
        game = GameController()

        # Set up a simple check scenario: white king at e1, black queen at e2
        game.board = game._create_empty_board()
        game.board[7][4] = ChessPiece('white', 'king')  # e1
        game.board[6][4] = ChessPiece('black', 'queen')  # e2

        # Verify the white king is in check
        self.assertTrue(game.is_in_check('white'))

        # Verify the black king is not in check (it's not even on the board)
        self.assertFalse(game.is_in_check('black'))

        # Set up another scenario: black king at e8, white rook at e7
        game.board = game._create_empty_board()
        game.board[0][4] = ChessPiece('black', 'king')  # e8
        game.board[1][4] = ChessPiece('white', 'rook')  # e7

        # Verify the black king is in check
        self.assertTrue(game.is_in_check('black'))

    def test_checkmate_detection(self):
        """Test detection of checkmate conditions."""
        game = GameController()

        # Set up a true checkmate scenario: white king at h1, black rooks at a1 and h2, black queen at g3
        # This ensures the king can't capture the rook at h2 because it would still be in check from the queen
        game.board = game._create_empty_board()
        game.board[7][7] = ChessPiece('white', 'king')  # h1
        game.board[7][0] = ChessPiece('black', 'rook')  # a1
        game.board[6][7] = ChessPiece('black', 'rook')  # h2
        game.board[5][6] = ChessPiece('black', 'queen')  # g3

        # Verify the white king is in checkmate
        self.assertTrue(game.is_in_check('white'))
        self.assertTrue(game.is_checkmate('white'))

        # Set up a check but not checkmate scenario: white king at h1, black rook at h2, but king can move to g1
        game.board = game._create_empty_board()
        game.board[7][7] = ChessPiece('white', 'king')  # h1
        game.board[6][7] = ChessPiece('black', 'rook')  # h2

        # Verify the white king is in check but not checkmate
        self.assertTrue(game.is_in_check('white'))
        self.assertFalse(game.is_checkmate('white'))

    def test_prevent_moves_leaving_king_in_check(self):
        """Test that moves leaving the king in check are prevented."""
        game = GameController()

        # Set up a scenario: white king at e1, white queen at d1, black rook at e8
        game.board = game._create_empty_board()
        game.board[7][4] = ChessPiece('white', 'king')  # e1
        game.board[7][3] = ChessPiece('white', 'queen')  # d1
        game.board[0][4] = ChessPiece('black', 'rook')  # e8

        # White's turn
        game.current_turn = 'white'

        # Moving the queen would leave the king in check - should be prevented
        self.assertFalse(game.move_piece('d1', 'd2'))

        # Moving the king out of the check's path should be allowed
        self.assertTrue(game.move_piece('e1', 'f1'))

    def test_must_move_out_of_check(self):
        """Test that a player in check must make a move to get out of check."""
        game = GameController()

        # Set up a scenario: white king at e1, white pawn at d2, black rook at e8
        game.board = game._create_empty_board()
        game.board[7][4] = ChessPiece('white', 'king')  # e1
        game.board[6][3] = ChessPiece('white', 'pawn')  # d2
        game.board[0][4] = ChessPiece('black', 'rook')  # e8

        # White's turn and white is in check
        game.current_turn = 'white'
        game.in_check = 'white'

        # Moving the pawn doesn't get out of check - should be prevented
        self.assertFalse(game.move_piece('d2', 'd3'))

        # Moving the king out of the check's path should be allowed
        self.assertTrue(game.move_piece('e1', 'f1'))

    def test_reset_game(self):
        """Test that the game can be reset to its initial state."""
        game = GameController()

        # Make some moves to change the game state
        game.move_piece('a2', 'a4')
        game.move_piece('a7', 'a5')

        # Reset the game
        game.reset_game()

        # Verify that the game state is reset
        self.assertEqual(game.current_turn, 'white')
        self.assertIsNone(game.in_check)
        self.assertIsNone(game.checkmate)

        # Verify that the board is reset to the initial state
        # Check a few key positions
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

    def test_checkmate_return_value(self):
        """Test that the move_piece method returns 'checkmate' when checkmate is detected."""
        game = GameController()

        # Set up a true checkmate scenario: white king at h1, black rooks at a1 and h2, black queen at g3
        game.board = game._create_empty_board()
        game.board[7][7] = ChessPiece('white', 'king')  # h1
        game.board[7][0] = ChessPiece('black', 'rook')  # a1
        game.board[6][7] = ChessPiece('black', 'rook')  # h2
        game.board[5][6] = ChessPiece('black', 'queen')  # g3

        # Set up a piece to move to cause checkmate
        game.board[4][0] = ChessPiece('black', 'queen')  # a4
        game.current_turn = 'black'

        # Move the queen to cause checkmate
        result = game.move_piece('a4', 'a2')

        # Verify that the move_piece method returns 'checkmate'
        self.assertEqual(result, 'checkmate')

        # Verify that the checkmate flag is set
        self.assertEqual(game.checkmate, 'white')


if __name__ == '__main__':
    unittest.main()
