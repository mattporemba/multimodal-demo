"""
Module for representing chess pieces on a chessboard.
"""

class ChessPiece:
    """
    Class representing a chess piece.
    
    Attributes:
        color (str): The color of the piece ('white' or 'black').
        piece_type (str): The type of the piece ('pawn', 'rook', 'knight', 'bishop', 'queen', 'king').
        symbol (str): The symbol representing the piece on the board.
    """
    
    def __init__(self, color, piece_type):
        """
        Initialize a chess piece.
        
        Args:
            color (str): The color of the piece ('white' or 'black').
            piece_type (str): The type of the piece ('pawn', 'rook', 'knight', 'bishop', 'queen', 'king').
        """
        self.color = color
        self.piece_type = piece_type
        
        # Define piece symbols
        pieces = {
            'white': {
                'pawn': 'wP',
                'rook': 'wR',
                'knight': 'wKn',
                'bishop': 'wB',
                'queen': 'wQ',
                'king': 'wKi'
            },
            'black': {
                'pawn': 'bP',
                'rook': 'bR',
                'knight': 'bKn',
                'bishop': 'bB',
                'queen': 'bQ',
                'king': 'bKi'
            }
        }
        
        self.symbol = pieces[color][piece_type]
    
    def __str__(self):
        """
        Return the string representation of the chess piece.
        
        Returns:
            str: The symbol representing the piece.
        """
        return self.symbol