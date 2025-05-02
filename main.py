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
        user_input = input(f"\n{game.current_turn.capitalize()}'s turn - Enter move (e.g., 'a2 a4') or 'quit' or 'surrender': ")

        # Check if user wants to quit
        if user_input.lower() == 'quit':
            print("Thanks for playing!")
            break

        # Check if user wants to surrender
        if user_input.lower() == 'surrender':
            confirm = input("Are you sure you want to surrender? (yes/no): ")
            if confirm.lower() in ['yes', 'y']:
                print(f"{game.current_turn.capitalize()} surrenders! Game reset.")
                game.reset_game()
                display_chessboard(game.get_board())
            continue

        # Secret debug command to set up checkmate scenario
        if user_input.lower() == 'debug checkmate':
            # Set up the checkmate scenario from the tests
            game.board = game._create_empty_board()
            from chessboard.chess_piece import ChessPiece
            game.board[7][7] = ChessPiece('white', 'king')  # h1
            game.board[7][0] = ChessPiece('black', 'rook')  # a1
            game.board[6][7] = ChessPiece('black', 'rook')  # h2
            game.board[5][0] = ChessPiece('black', 'queen')  # a3
            game.current_turn = 'black'
            display_chessboard(game.get_board())
            continue

        # Secret debug command to set up check scenario
        if user_input.lower() == 'debug check':
            # Set up a check scenario where black can put white in check with a single move
            game.board = game._create_empty_board()
            from chessboard.chess_piece import ChessPiece
            game.board[7][4] = ChessPiece('white', 'king')  # e1
            game.board[4][3] = ChessPiece('black', 'bishop')  # c3
            game.current_turn = 'black'
            display_chessboard(game.get_board())
            continue

        # Parse the input
        try:
            positions = user_input.split()
            if len(positions) != 2:
                print("Invalid input. Please enter two positions separated by a space (e.g., 'a2 a4').")
                continue

            from_pos, to_pos = positions

            # Move the piece
            result = game.move_piece(from_pos, to_pos)
            if result == "checkmate":
                # Display the updated board
                display_chessboard(game.get_board())
                # Ask if players want to reset the game
                reset_choice = input("Would you like to play again? (yes/no): ")
                if reset_choice.lower() in ['yes', 'y']:
                    game.reset_game()
                    display_chessboard(game.get_board())
                else:
                    print("Thanks for playing!")
                    break
            elif result:
                print(f"Moved piece from {from_pos} to {to_pos}")
                # Display the updated board
                display_chessboard(game.get_board())
            else:
                print("Move failed. Please try again.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
