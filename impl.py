from draw import *
from sudoku import *
import numpy as np
import subprocess, os


if __name__ == '__main__':
    sudoku = Sudoku(None)
    sudoku.build_random_game(9)
    #print(list(sudoku.board))
    drawing = Drawing(sudoku.board.tolist())
    filename = drawing.draw_sudoku('')


    
    pdf_name = filename[:-2]+'pdf'


    PS2_PATH = 'C:\\Program Files\\gs\\gs9.52\\lib'
    os.environ["PATH"] += os.pathsep + PS2_PATH
    instruction = 'ps2pdf "'+os.getcwd()+'\\"'+filename+' "'+os.getcwd()+'\\'+pdf_name+'"'
    res = subprocess.Popen(instruction, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # Wait for the process end and print error in case of failure 
    if res.wait() != 0:
        output, error = res.communicate()
        print(error)

    

    
