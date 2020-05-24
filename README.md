# Sudoku

Written by Maurusian, in Python 3.6.0

## Overview
This program implements a backtracking algorithm to solve Sudoku puzzles, and also to generate random Sudoku puzzles of any desired size.
Obviously, the larger the size of the puzzle, the more time it will take to solve or generate. The full rules of Sudoku are impemented if
the board size is a perfect square. Otherwise, only rows and columns are checked.

Generated puzzles must evidently have a single solution to be valid. Once a puzzle is created, it can be drawn onn canvas, and exported
as a Postscript file. This file can then be converted to another format (image, PDF, etc). An implementation where the puzzle is exported
to PDF has been added.

## Requirements
- Python 3 or above
- NumPy
- Ghostscript installed (to convert PS files to PDF). Download here: https://www.ghostscript.com/download/gsdnld.html

## Inpiration
The algorithm for solving the puzzle (solve() function) was mainly taken from this Computerphile video (Python Sudoku Solver - Computerphile): 
https://www.youtube.com/watch?v=G_UYXzGuqvM

The StackExchange community was also very helpful in solving a few technical hiccups encountered in this project.

## Future development
The implementation (impl.py) was made for Windows OS. An implementation for Linux (Ubuntu) will be coming soon.

The algorithm that generates puzzles can definitely be improved upon.

The arrow somehow doesn't disappear from the canvas, hence the exported PDF as well, despite using hideturtle() and ht(). This should be fixed.

For composite numbers, the third Sudoku rule can be implemented with rectangles instead of squares.

One can imagine a gazillion other enhancements and functinalities.
