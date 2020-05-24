from numpy import matrix, zeros
from math import sqrt, floor
from random import randint


class Sudoku():
    def __init__(self,board):
        self.board = board
        self.solutions = 0


    def __repr__(self):
        return str(matrix(self.board))

    def __str__(self):
        return str(matrix(self.board))

    def is_perf_square_board(self):
        size = self.get_board_size()
        sq   = floor(sqrt(size))

        if sq**2 == size:
            return sq
        else:
            return 0

    def get_board_size(self):
        return len(self.board)

    def number_fits(self,i,j,x):
        size = self.get_board_size()
        if x < 0 or x > size:
            return False
        for e in range(size):
            if self.board[i,e] == x:
                return False
        for e in range(size):
            if self.board[e,j] == x:
                return False

        sq = self.is_perf_square_board()
        if sq!=0:
            posi = (i//sq)*sq
            posj = (j//sq)*sq
            for e in range(posi,posi+sq):
                for f in range(posj,posj+sq):
                    if self.board[e,f]==x:
                        return False

        return True
            
        

    def solve(self):
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
        self.board = zeros([size,size],dtype = int)

        for k in range(size):
            i = randint(0,size-1)
            j = randint(0,size-1)
            x = randint(1,size)
            if self.board[i,j] == 0 and self.number_fits(i,j,x):
                self.board[i,j] = x
            else:
                k-=1

    def build_random_game(self,size):
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
                print(self.solutions)
                if self.solutions == 0:
                    self.board[i,j] = 0
                    

        print(self)

            
             
            

    

if __name__=='__main__':
        
    sudoku = Sudoku(matrix(([0,1,4,0],
                            [0,3,0,0],
                            [0,0,2,1],
                            [0,0,0,0])))

    #print(sudoku)
    #sudoku.solve()
    #print(sudoku.solutions)
    #print(sudoku.solve())
    #print(sudoku.number_fits(2,1,3))
    sudoku.build_random_game(9)
    
