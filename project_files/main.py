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
from newton import Newton


def main():
    
    os.system('cls')
    pyautogui.press('F11')
    try:
        curses.wrapper(start_curses)
        pyautogui.press('F11')
    except ZeroDivisionError:
        print("No solution in the given linear equation")
    


def start_curses(window):
    title = "BSM Project"
    curses.initscr()
    curses.init_pair(1, 47,curses.COLOR_BLACK) #green
    curses.init_pair(2, 197, curses.COLOR_BLACK) #red
    curses.init_pair(3, 123, curses.COLOR_BLACK) #cyan
    curses.init_pair(4, 227, curses.COLOR_BLACK) #yellow
    curses.init_pair(5, 18, 208) #blue , orange #https://stackoverflow.com/questions/18551558/how-to-use-terminal-color-palette-with-curses the numbers are colors
    curses.init_pair(6, 206, curses.COLOR_BLACK) #pink
    curses.init_pair(7,182,curses.COLOR_BLACK) #blue
#print()
    userContinue = True
    
    while userContinue:
        window.clear()
        display_title(window, title,font='big',color=curses.color_pair(2))
        user_input = get_problem_type(window)
        try:
            user_input = eval(user_input)
        except:
            pass
        
        if user_input < 4: #all gauss methods need matrix
            title_input = "Gaussian"
            if user_input == 2:
                title_input = 'GaussJordan'
            elif user_input == 3:
                title = 'GEMPS'
            
            matrix = gaussian_functions.get_matrix_from_user(window, title,color=curses.color_pair(2))
            for row_ind, row in enumerate(matrix): #convert to numbers
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
        elif user_input == 8:
            Newton(window)
        elif user_input == 9:
            break
        

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
    [8]. Newton               
    [Q]. Quit                 
    """
    center_screen_y, center_screen_x = get_the_center_screen(window)
    prompt_array = prompt.splitlines()
    prompt_x_length = len(prompt_array[0])
    prompt_y_length = len(prompt_array)

    prompt_x = center_screen_x - int(prompt_x_length/2)
    prompt_y = center_screen_y - int(prompt_y_length/2)
    
    user_selected = False
    selected_row = 1 # 3rd row of the string
    curses.curs_set(0)
    while not user_selected:
        color = curses.color_pair(5)
        display_string_center_screen(window, prompt_y, prompt_array,colored_row=[selected_row],color=curses.color_pair(3), colored_row_color=curses.color_pair(5))
        user_input = window.getch()
        if user_input == curses.KEY_UP:
            selected_row -= 1
        elif user_input == curses.KEY_DOWN:
            selected_row += 1
        elif user_input == ord('\n'):
            user_selected = True
        
        if selected_row < 1:
            selected_row = 9
        elif selected_row > 9:
            selected_row = 1
        
    return selected_row 

main()