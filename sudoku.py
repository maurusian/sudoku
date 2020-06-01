from numpy import matrix, zeros
from math import sqrt, floor
from random import randint


class Sudoku():
    """
    Class that handles the creation
    and modification of a Sudoku object.
    """
    def __init__(self,board):
        """
        Constructor. Intitializes the board

        -- Input:
        - board: NumPy matrix that represents
        a Sudoku board. Empty values are set to
        zero.

        Attributes:
        -- board: already explained
        -- solutions: number of solutions that
        were found when solving the Sudoku board
        (see solve function).
        """
        self.board = board
        self.solutions = 0


    def __repr__(self):
        """
        Returns a string representation of a Sudoku
        object, which is simply the string form of
        the board attribute.
        """
        return str(matrix(self.board))

    def __str__(self):
        """
        Returns a string representation of a Sudoku
        object, which is simply the string form of
        the board attribute.
        """
        return str(matrix(self.board))

    def is_perf_square_board(self):
        """
        Tests if the the board size is a perfect
        square.

        Returns the square root if true, and 0
        otherwise.
        """
        size = self.get_board_size()
        sq   = int(floor(sqrt(size)))

        if sq**2 == size:
            return sq
        else:
            return 0

    def is_composite(self):
        """
        Tests if the the board size is a composite
        number.

        Calculates the two components with the
        smallest difference. For a given side of
        the board n, k and h that satisfy:
        - k*h = n
        - abs(k-h) is the smallest possible value
        the function would return min(h,k).

        For prime numbers, the function returns 0.
        """

        size = self.get_board_size()
        sq   = int(floor(sqrt(size)))
        x = 1
        for k in range(2,sq+1):
            if size%k == 0:
                x = k

        if x==1:
            return 0

        return x
        

    def get_board_size(self):
        """
        Returns board size.
        """
        return len(self.board)

    def number_fits(self,i,j,x):
        """
        Checks if a given number fits in a cell.
        A number fits in a cell, if and only if
        it does not violate Sudoku rules, that is,
        it's not repeated in the same row, same
        column, or the same square (if the board
        size is a perfect square).
        Returns a boolean value.

        -- Input:
        - i: row number
        - j: column number
        - x: value to check

        -- Output:
        - True: x fits in the cell (i,j)
        - False: otherwise
        """
        size = self.get_board_size()
        
        if x < 0 or x > size:
            return False
        for e in range(size):
            if self.board[i,e] == x:
                return False
        for e in range(size):
            if self.board[e,j] == x:
                return False

        #the rule of checking the sub-squares
        #is only enabled for board sizes that
        #are perfect squares, e.g. 4, 9, 16, etc
        sq = self.is_perf_square_board()
        co = self.is_composite()
        if sq!=0:
            posi = (i//sq)*sq
            posj = (j//sq)*sq
            for e in range(posi,posi+sq):
                for f in range(posj,posj+sq):
                    if self.board[e,f]==x:
                        return False
        #the rule of checking the sub-rectangles
        #is only enabled for board sizes that
        #are composite numbers
        elif co!=0:
            mp = size//co
            posi = (i//co)*co
            posj = (j//mp)*mp
            for e in range(posi,posi+co):
                for f in range(posj,posj+mp):
                    if self.board[e,f]==x:
                        return False

        return True
            
        

    def solve(self):
        """
        Recursive function that checks each
        empty cell for possible values, until
        the Sudoku puzzle is solved, or no
        solutions are found. Prints all found
        solutions.
        Increments the attribute solutions as
        more solutions are found.
        """
        size = self.get_board_size()
        for i in range(size):
            for j in range(size):
                if self.board[i,j] == 0:
                    
                    for x in range(1,size+1):
                        if self.number_fits(i,j,x):
                            
                            self.board[i,j] = x
                            self.solve()
                            self.board[i,j] = 0
                    
                    return
        
        input("Next solution? --- ")
        print(self)
        self.solutions+=1
        return

    def pseudo_solve(self):
        """
        The same as solve(), except that this
        function stops as soon as the number
        of solutions exceeds 1 (i.e. is equal
        to 2).
        Does not print the solutions if any
        are found.
        This special implementation was created
        to generate random Sudoku puzzle games
        (see build_random_game).
        """
        size = self.get_board_size()
        if self.solutions > 1:
            return
        for i in range(size):
            for j in range(size):
                if self.board[i,j] == 0:
                    
                    for x in range(1,size+1):
                        if self.number_fits(i,j,x):
                            
                            self.board[i,j] = x
                            self.pseudo_solve()
                            self.board[i,j] = 0
                    
                    return
        
        self.solutions+=1
        return

    def build_random_board(self,size):
        """
        Updates the board attribute of the current
        object, by setting the board size, setting
        all values to zero, and initializing some
        cells to random values.

        -- Input:
        - size: size of the board, and also number
        of cells that will be initiated.
        """
        
        self.board = zeros([size,size],dtype = int)
        k = 0
        while k<size:
            i = randint(0,size-1)
            j = randint(0,size-1)
            x = randint(1,size)
            if self.board[i,j] == 0 and self.number_fits(i,j,x):
                self.board[i,j] = x
                k+=1

    def build_random_game(self,size):
        """
        Creates a random Sudoku game. Keeps checking
        the solutions to the game and adding values,
        until an optimal game is found, i.e. one that
        has the least number of values but a single
        solution.
        -- Input:
        - size: size of the board.
        """
        self.build_random_board(size)
        
        while self.solutions != 1:
            self.solutions = 0
            i = randint(0,size-1)
            j = randint(0,size-1)
            x = randint(1,size)
            if self.board[i,j] == 0 and self.number_fits(i,j,x):
                self.board[i,j] = x
                print(self)
                self.pseudo_solve()
                print('Number of solutions: '+str(self.solutions))
                if self.solutions == 0:
                    self.board[i,j] = 0
                    
        print('Sudoku game generated:')
        print(self)



if __name__=='__main__':
    """
    Test implementation for Sudoku class
    and its functionalities.
    """
    sudoku = Sudoku(matrix(([0,1,4,0,1,4],
                            [0,3,0,0,1,4],
                            [0,0,2,1,1,4],
                            [0,0,0,0,1,4],
                            [0,0,0,0,1,4],
                            [0,0,0,0,1,4])))

    #print(sudoku)
    #sudoku.solve()
    #print(sudoku.solutions)
    #print(sudoku.solve())
    #print(sudoku.number_fits(2,1,3))
    #sudoku.build_random_game(6)
    #sudoku.build_random_board(12)
    #print(sudoku.is_composite())
    
