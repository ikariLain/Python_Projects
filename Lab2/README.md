# Lab 2 - Chess Board Generator

## About the Assignment
This is the second assignment in the course, implemented in Python. The task focuses on creating a logical solution for generating a chess board pattern using basic programming concepts. The program demonstrates understanding of program flow and logical thinking without requiring complex data types or advanced structures.

## Project Requirements

### Core Functionality
- Create a program that generates a chess board pattern in the console
- Prompt the user to input a number that determines the board size
- Generate a board with equal rows and columns based on user input
- Use `◼︎` for black squares and `◻︎` for white squares
- Ensure alternating pattern both horizontally and vertically

### Implementation Details
- All code should be in a single Python file
- Comments should be included to explain the code
- Variable names and comments should be in English
- Use appropriate data type conversion for user input

## Examples

### 3x3 Board
When user inputs 3:
```
3
◻︎◼︎◻︎
◼︎◻︎◼︎
◻︎◼︎◻︎
```

### 10x10 Board
When user inputs 10:
```
10
◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎
◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎
◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎
◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎
◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎
◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎
◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎
◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎
◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎
◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎◼︎◻︎
```

## Extra Challenges

### Custom Square Characters
- Allow users to choose their own characters for black and white squares
- Support for both text characters and emojis

### Piece Placement
- Allow users to place a chess piece on the board
- Use chess notation (e.g., 'E7' for 5th column, 7th row)
- Display special characters for chess pieces (e.g., `♛ ♜ ♞`)

## Project Structure
```
├── README.md
└── chessboard.py
```

## Installation and Usage
1. Ensure Python 3 is installed on your system
2. Clone this repository
3. Run the program:
   ```bash
   python chessboard.py
   ```

## Technical Notes
- Python's Unicode support is used for displaying special characters
- Input validation is implemented for user safety
- The program uses nested loops for board generation