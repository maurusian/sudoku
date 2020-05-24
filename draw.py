import turtle
import os
from datetime import datetime
import numpy as np

SQUARE_SIDE = 75

DEF_WINDOW_SIZE_X = 1000
DEF_WINDOW_SIZE_Y = 800

#display coordinate corrections for numbers
CORRX = 25
CORRY = 60

class Drawing():

    def __init__(self,values):
        self.grid = turtle.Turtle()
        self.values = values  #list of lists, matrix

        self.board_size = len(self.values)
        
        self.WINDOW_SIZE_X = DEF_WINDOW_SIZE_X*(self.board_size//10+1)
        self.WINDOW_SIZE_Y = DEF_WINDOW_SIZE_Y*(self.board_size//10+1)
        self.font_size = max(25//(self.board_size//10+1),8)
        
        
        turtle.setworldcoordinates(-1, -1, self.WINDOW_SIZE_X, self.WINDOW_SIZE_Y)
        self.grid.home()
        turtle.delay(0)
        self.grid.hideturtle()
        self.grid.ht()

        self.posx = (self.WINDOW_SIZE_X - SQUARE_SIDE*len(self.values)) // 2
        self.posy = (self.WINDOW_SIZE_Y - SQUARE_SIDE*len(self.values)) // 2

    def square(self,side):
        for i in range(4):
            self.grid.forward(side)
            self.grid.left(90)

    def row(self,n,side):
        for i in range(n):
            self.square(side)
            self.grid.forward(side)
        self.grid.penup()
        self.grid.left(180)
        self.grid.forward(n * side)
        self.grid.left(180)
        self.grid.pendown()

    def row_of_rows(self,n,side):
        self.grid.pendown()
        for i in range(n):
            self.row(n,side)
            self.grid.penup()
            self.grid.left(90)
            self.grid.forward(side)
            self.grid.right(90)
            self.grid.pendown()
        self.grid.penup()
        self.grid.right(90)
        self.grid.forward(n * side)
        self.grid.left(90)
        self.grid.pendown()

    
    def draw_sudoku(self,filename):
        side = SQUARE_SIDE
        self.grid.penup()
        self.grid.goto(self.posx,self.posy)
        self.row_of_rows(len(self.values),side)
        self.grid.penup()
        self.grid.goto(self.posx,self.posy)
        topx = (self.WINDOW_SIZE_X - SQUARE_SIDE*len(self.values)) // 2 + CORRX  #correction on the X coordinates for number positions
        topy = (self.WINDOW_SIZE_Y + SQUARE_SIDE*(len(self.values))) // 2 - CORRY #correction on the Y coordinates for number positions
        
        for i in range(len(self.values)):
            posi = topy - i*75
            for j in range(len(self.values[i])):
                posj = topx + j*75
                self.grid.goto(posj,posi)
                if self.values[i][j] != 0:
                    self.grid.write(str(self.values[i][j]),move=True,align="left", font=("Arial", self.font_size, "normal"))

        if filename is None or filename.split('.')[0].strip() == '':
            date = datetime.now()
            datestring = date.strftime('%y.%m.%d_%H.%M')
            filename = 'sudoku_'+datestring+'.ps' #default name
        cnv = turtle.getscreen().getcanvas().postscript(file=filename)

        return filename





if __name__ == '__main__':
   
    lis =   [[0,1,4,0,0,5,0,0,7],
             [0,3,0,0,2,0,8,0,0],
             [0,0,2,1,0,3,0,0,0],
             [0,0,0,0,4,0,0,1,0],
             [0,1,4,0,0,5,0,0,7],
             [0,3,0,0,2,0,8,0,0],
             [0,0,2,1,0,3,0,0,0],
             [0,0,0,0,4,0,0,1,0],
             [0,0,0,0,4,0,0,1,0]]

    lis2 =  [[0,1,4,0,0,5,0,0],
             [0,3,0,0,2,0,8,0],
             [0,0,2,1,0,3,0,0],
             [0,0,0,0,4,0,0,1],
             [0,1,4,0,0,5,0,0],
             [0,3,0,0,2,0,8,0],
             [0,0,2,1,0,3,0,0],
             [0,0,0,0,4,0,0,1]]

    #testing correct display with different grid sizes
    size = 18
    ones = list(np.ones([size, size], dtype = int))

    drawing = Drawing(ones)

    print(drawing.values)

    
    filename = drawing.draw_sudoku('')

    print(filename)






    
