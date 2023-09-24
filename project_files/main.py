import curses
import os
import pyautogui
import curses
from project_functions import *
from gauss_jordan import GaussJordan
from gaussian import Gaussian
from moss import Moss
import gaussian_functions
from gemps import Gemps
from half_interval import HalfInterval
from trapezoidal import Trapezoidal
from romberg import Romberg
title = "BSM Project"

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
    curses.init_pair(4, 227, curses.COLOR_BLACK)
    curses.init_pair(5, 91, 220) #https://stackoverflow.com/questions/18551558/how-to-use-terminal-color-palette-with-curses the numbers are colors
    curses.init_pair(6, 206, curses.COLOR_BLACK)
    print(display_title(window, title,font='big'))
    user_input = eval(get_problem_type(window))
    if user_input < 4: #all gauss methods need matrix
        matrix = gaussian_functions.get_matrix_from_user(window, title)
        for row_ind, row in enumerate(matrix):
            for col_ind, col in enumerate(matrix[row_ind]):
                matrix[row_ind][col_ind] = eval(col)
        if user_input == 1:
            Gaussian(matrix, window)
        elif user_input == 2:
            GaussJordan(matrix, window)
        elif user_input == 3:
            Gemps(matrix, window)
    elif user_input == 4:
        Moss(window)
    elif user_input == 5:
        HalfInterval(window)
    elif user_input == 6:
        Trapezoidal(window)
    elif user_input == 7:
        romberg = Romberg(window)
        romberg.solve_romberg_from_romberg()

def get_problem_type(window): #gauss ba gauss jordan etc
    """Returns the chr value of the user input"""
    prompt = """Enter the number of the problem
    [1]. Gaussian
    [2]. Gauss-Jordan
    [3]. GEMPS
    [4]. Moss
    [5]. Half-Interval Method
    [6]. Trapezoidal
    [7]. Romberg
    """
    center_screen_y, center_screen_x = get_the_center_screen(window)
    prompt_array = prompt.splitlines()
    prompt_x_length = len(prompt_array[0])
    prompt_y_length = len(prompt_array)

    prompt_x = center_screen_x - int(prompt_x_length/2)
    prompt_y = center_screen_y - int(prompt_y_length/2)
    

   
    display_string(window, prompt_y, prompt_x, prompt_array)
    window.move(prompt_y+ prompt_y_length, prompt_x  )
    user_input = window.getch()
    
    return chr(user_input)

main()