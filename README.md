# Sudoku

Written by Maurusian, in Python 3.6.0

## Overview
This program implements a backtracking algorithm to solve Sudoku puzzles, and also to generate random Sudoku puzzles of any desired size.
Obviously, the larger the size of the puzzle, the more time it will take to solve or generate. The full rules of Sudoku are impemented if the board size is a perfect square. For composite numbers, the third Sudoku rule is implemented with rectangles instead of squares, by choosing a rectangle of sides a and b, such that a x b = the size of the board, and if a is the smallest of a and b, a will be counted on rows, while b will be counted on columns. For board sizes that are prime numbers, only rows and columns are checked.

Generated puzzles must evidently have a single solution to be valid. Once a puzzle is created, it can be drawn on canvas, and exported
as a Postscript file. This file can then be converted to another format (image, PDF, etc). An implementation where the puzzle is exported
to PDF has been added.

## Requirements
- Python 3 or above
- NumPy
- Ghostscript installed (to convert PS files to PDF). Download here: https://www.ghostscript.com/download/gsdnld.html

## Inspiration
The algorithm for solving the puzzle (solve() function) was mainly taken from this Computerphile video (Python Sudoku Solver - Computerphile): 
https://www.youtube.com/watch?v=G_UYXzGuqvM

The StackExchange community was also very helpful in solving a few technical hiccups encountered in this project.

## Future development

### Core functionalities
- The algorithm that generates puzzles can definitely be improved upon for speed.
- Storing and loading puzzles can be added.
- Hashing and comparing boards to ensure unicity (although the likelihood of repeating the same initial state by a random process is quite small).

### Drawing the board
- The arrow somehow doesn't disappear from the canvas, and neither from the exported PDF, despite using hideturtle() and ht(). This should be fixed.
- Making the lines that separate square areas bolder to make them easier to distinguish.

### Implementation
- The implementation (impl.py) was made for Windows OS. An implementation for Linux (Ubuntu) will be coming soon.
- Generating a large PDF with multiple puzzles.
- PDF formatting (text, style, etc).

One can imagine a gazillion other enhancements and functionalities.
