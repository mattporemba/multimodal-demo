# Chessboard

Track the state of a chessboard in a terminal using Unicode with a video live stream from a phone.

## Goals

1. Explore Google's Live API.
2. Track the board state of a chess game.
3. Use a phone camera to capture the game. Images at first, then live video.
4. Test bandwidth and latency of the phone camera.
5. Test costs of using the Live API and streaming video.
6. Explore efficiency options: segment video locally and extract only relevant frames.
7. Explore voice generation in broadcast.
   See [NEXT ping pong demo](https://github.com/GoogleCloudDevRel/next25-retro-ping-pong)

## Architecture

(This is just a guess) A phone app will send pictures a GCP bucket, or livestream video to (??). That bucket/video is
processed by Gemini. Gemini will identify what two board locations changed: where the piece moved from and to.
Programmatically determine the state of the board off of the changes observed to track what pieces are where.

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
