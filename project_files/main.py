import curses
import os
import pyautogui
import project
import curses
import project_functions
from gauss_jordan import GaussJordan
from gaussian import Gaussian
from moss import Moss
import gaussian_functions
from gemps import Gemps
title = "Darius' Project"

def main():
    
    os.system('cls')
    pyautogui.press('F11')
    try:
        curses.wrapper(start_curses)
        pyautogui.press('F11')
    except ZeroDivisionError:
        print("No solution in the given linear equation")
    


def start_curses(window):
    curses.initscr()
    curses.init_pair(1, curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    project_functions.display_title(window, title)
    user_input = eval(project_functions.get_problem_type(window))
    if user_input < 3:
        matrix = gaussian_functions.get_matrix_from_user(window, title)
        for row_ind, row in enumerate(matrix):
            for col_ind, col in enumerate(matrix[row_ind]):
                matrix[row_ind][col_ind] = eval(col)
        if user_input == 1:
            Gemps(matrix, window)
        elif user_input == 2:
            GaussJordan(matrix, window)
    elif user_input == 3:
        Moss(window)


    
main()