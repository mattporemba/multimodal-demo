"""
Unit tests for the chessboard module.
"""

import unittest
from chessboard.chessboard import generate_chessboard


class TestChessboard(unittest.TestCase):
    """Test cases for the chessboard module."""

    def test_default_size(self):
        """Test that the default chessboard size is 8x8."""
        chessboard = generate_chessboard()
        self.assertEqual(len(chessboard), 8, "Chessboard should have 8 rows")
        for row in chessboard:
            self.assertEqual(len(row), 8, "Each row should have 8 columns")

    def test_custom_size(self):
        """Test that a custom size chessboard can be generated."""
        size = 4
        chessboard = generate_chessboard(size)
        self.assertEqual(len(chessboard), size, f"Chessboard should have {size} rows")
        for row in chessboard:
            self.assertEqual(len(row), size, f"Each row should have {size} columns")

    def test_alternating_pattern(self):
        """Test that the chessboard has the correct alternating pattern."""
        chessboard = generate_chessboard(4)
        # Expected pattern for a 4x4 chessboard
        expected = [
            ['□', '■', '□', '■'],
            ['■', '□', '■', '□'],
            ['□', '■', '□', '■'],
            ['■', '□', '■', '□']
        ]
        self.assertEqual(chessboard, expected, "Chessboard pattern is incorrect")

    def test_first_square_is_white(self):
        """Test that the first square (0,0) is always white."""
        chessboard = generate_chessboard()
        self.assertEqual(chessboard[0][0], '□', "First square should be white")

    def test_edge_case_size_one(self):
        """Test the edge case of a 1x1 chessboard."""
        chessboard = generate_chessboard(1)
        self.assertEqual(len(chessboard), 1, "Chessboard should have 1 row")
        self.assertEqual(len(chessboard[0]), 1, "Row should have 1 column")
        self.assertEqual(chessboard[0][0], '□', "Single square should be white")


if __name__ == '__main__':
    unittest.main()