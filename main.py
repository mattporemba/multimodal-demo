#!/usr/bin/env python3
"""
Main script for the chessboard application.
This script prints a 2D representation of a chessboard.
"""

from chessboard.chessboard import generate_chessboard, display_chessboard


def main():
    """
    Main function to run the chessboard application.
    """
    print("Hello, Chess World!")
    print("Here's a 2D representation of a chessboard:")
    print()

    # Generate and display an 8x8 chessboard with pieces
    chessboard = generate_chessboard(with_pieces=True)
    display_chessboard(chessboard)


if __name__ == "__main__":
    main()
