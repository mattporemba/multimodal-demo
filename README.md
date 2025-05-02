# Chessboard

A simple Python application that prints a 2D representation of a chessboard.

## Description

This application generates and displays a 2D representation of a chessboard in the terminal. The chessboard is represented using Unicode characters, with '□' for white squares and '■' for black squares.

## Features

- Generate a standard 8x8 chessboard
- Support for custom-sized chessboards
- Clean, modular code structure
- Comprehensive unit tests

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/mattporemba/multimodal-demo.git
   cd multimodal-demo
   ```

2. Install the package:
   ```
   pip install -e .
   ```

## Usage

### Running from the command line

After installation, you can run the application using the provided console script:

```
chessboard
```

### Running the main function directly

You can also run the main function directly without installation:

```
python main.py
```

This will display a standard 8x8 chessboard in the terminal.

### Using as a module

You can also use the package in your own Python code:

```python
from chessboard.chessboard import generate_chessboard, display_chessboard

# Generate a standard 8x8 chessboard
board = generate_chessboard()

# Generate a custom-sized chessboard (e.g., 4x4)
small_board = generate_chessboard(4)

# Display a chessboard
display_chessboard(board)
```

## Running Tests

To run the tests, use pytest:

```
pytest
```

## Project Structure

```
chessboard/
├── chessboard/
│   ├── __init__.py
│   └── chessboard.py
├── tests/
│   ├── __init__.py
│   └── test_chessboard.py
├── main.py
├── setup.py
└── requirements.txt
```
