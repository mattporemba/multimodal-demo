#!/usr/bin/env python3
"""
Main script for the chessboard application.
This script allows users to play chess by moving pieces on a 2D chessboard.
"""

from chessboard.chessboard import display_chessboard
from chessboard.game_controller import GameController


def main():
    """
    Main function to run the chessboard application.
    """
    print("Hello, Chess World!")
    print("Here's a 2D representation of a chessboard:")
    print()

    # Create a game controller and set up the pieces
    game = GameController()
    game.setup_pieces()

    # Display the initial board
    display_chessboard(game.get_board())

    # Game loop
    while True:
        # Get user input
        user_input = input("\nEnter move (e.g., 'a2 a4') or 'quit' to exit: ")

        # Check if user wants to quit
        if user_input.lower() == 'quit':
            print("Thanks for playing!")
            break

        # Parse the input
        try:
            positions = user_input.split()
            if len(positions) != 2:
                print("Invalid input. Please enter two positions separated by a space (e.g., 'a2 a4').")
                continue

            from_pos, to_pos = positions

            # Move the piece
            if game.move_piece(from_pos, to_pos):
                print(f"Moved piece from {from_pos} to {to_pos}")
                # Display the updated board
                display_chessboard(game.get_board())
            else:
                print("Move failed. Please try again.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
