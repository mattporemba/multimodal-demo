"""
Unit tests for the chess_piece module.
"""

import unittest
from chessboard.chess_piece import ChessPiece


class TestChessPiece(unittest.TestCase):
    """Test cases for the chess_piece module."""

    def test_init_white_pawn(self):
        """Test initialization of a white pawn."""
        piece = ChessPiece('white', 'pawn')
        self.assertEqual(piece.color, 'white')
        self.assertEqual(piece.piece_type, 'pawn')
        self.assertEqual(piece.symbol, 'wP')

    def test_init_black_knight(self):
        """Test initialization of a black knight."""
        piece = ChessPiece('black', 'knight')
        self.assertEqual(piece.color, 'black')
        self.assertEqual(piece.piece_type, 'knight')
        self.assertEqual(piece.symbol, 'bKn')

    def test_str_representation(self):
        """Test string representation of chess pieces."""
        white_queen = ChessPiece('white', 'queen')
        black_king = ChessPiece('black', 'king')
        
        self.assertEqual(str(white_queen), 'wQ')
        self.assertEqual(str(black_king), 'bKi')

    def test_all_piece_types(self):
        """Test all piece types for both colors."""
        piece_types = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
        expected_white_symbols = ['wP', 'wR', 'wKn', 'wB', 'wQ', 'wKi']
        expected_black_symbols = ['bP', 'bR', 'bKn', 'bB', 'bQ', 'bKi']
        
        for i, piece_type in enumerate(piece_types):
            white_piece = ChessPiece('white', piece_type)
            black_piece = ChessPiece('black', piece_type)
            
            self.assertEqual(white_piece.symbol, expected_white_symbols[i])
            self.assertEqual(black_piece.symbol, expected_black_symbols[i])


if __name__ == '__main__':
    unittest.main()