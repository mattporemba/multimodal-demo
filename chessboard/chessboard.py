"""
Module for generating and displaying a 2D representation of a chessboard.
"""


def generate_chessboard(size=8):
    """
    Generate a 2D representation of a chessboard.
    
    Args:
        size (int): The size of the chessboard (default: 8x8).
        
    Returns:
        list: A 2D list representing the chessboard, where '■' represents black squares
             and '□' represents white squares.
    """
    chessboard = []
    for i in range(size):
        row = []
        for j in range(size):
            # If the sum of row and column indices is even, it's a white square
            # Otherwise, it's a black square
            if (i + j) % 2 == 0:
                row.append('□')  # White square
            else:
                row.append('■')  # Black square
        chessboard.append(row)
    return chessboard


def display_chessboard(chessboard):
    """
    Display a 2D representation of a chessboard.
    
    Args:
        chessboard (list): A 2D list representing the chessboard.
    """
    for row in chessboard:
        print(' '.join(row))


def main():
    """
    Main function to generate and display a chessboard.
    """
    print("Chessboard Representation:")
    chessboard = generate_chessboard()
    display_chessboard(chessboard)


if __name__ == "__main__":
    main()