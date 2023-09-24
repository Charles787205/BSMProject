import curses
import pyfiglet
from typing import List
matrix = []
title = ''
from math import *


"""This is the functions that is shared among the projects"""

   
def display_title(window, title,font='big',color=None) : #display the title in the center using curses
    """display the title and returns the y length"""
    title = pyfiglet.figlet_format(title, font=font)
    centery, centerx = get_the_center_screen(window)
    title_array = title.splitlines()
    title_x_length = len(title_array[0])
    title_height = len(title_array)
    title_start_x = centerx - int(title_x_length/2)
    
    if color is not None:
        display_string(window,0, title_start_x,title_array, color=color)
    else:
        display_string(window,0, title_start_x,title_array)
    
    
    return (len(title.splitlines())) #height sa title

    

def get_the_center_screen(window) :
    """Returns the center y and x"""
    y,x = window.getmaxyx()
    center_screen_y = int(y/2)
    center_screen_x = int(x/2)
    return center_screen_y, center_screen_x


def display_string(window,y,x, string_arr, color=None, colored_row=[], colored_row_color=None):
    for index, line in enumerate(string_arr):
       
        if index in colored_row:
            window.addstr(y+index, x, line, colored_row_color)
        else:
            if color is not None:
                window.addstr(y+index, x, line, color)
            else:
                window.addstr(y+index, x, line )
        



def get_string_from_user(window, cursor_start_x:int, cursor_start_y:int,title, color=None,title_color=None) -> str:
    """Get the string from user input"""
    cursor_x = cursor_start_x
    cursor_y = cursor_start_y
    window.move(cursor_y, cursor_x)
    user_input = ''
    is_entered = False
    center_y, center_x = get_the_center_screen(window)
    maxy,maxx = window.getmaxyx()
    while(not is_entered):
        if title_color is not None:
            display_title(window, title, color=title_color)
        else: 
            display_title(window,title)
        if color != None:
            display_string(window, cursor_y, cursor_x, user_input.splitlines(),color=color)
        else:
            display_string(window, cursor_y, cursor_x, user_input.splitlines())
        
        key = window.getch()
        window.move(cursor_y, cursor_x+1)

        if key == 10: #ascii sa enter
            is_entered = True
        elif key == 8:
            user_input = user_input[:-1]
            filler = ''
            for i in range(0, maxx-1):
                filler += ' '
            window.addstr(cursor_y, 0, filler)
        else:
            user_input += chr(key)

        cursor_x = center_x - int(len(user_input)/2)
        
        
    window.clear()
    return user_input

def display_string_center_screen(window, y, string_arr, color=None, colored_row=[], colored_row_color=None):
    length = 0
    for i in string_arr:
        if len(i) > length:
            length = len(i)

    center_y, centerx = get_the_center_screen(window)
    string_x = centerx - int(length /2)
    display_string(window, y, string_x, string_arr, color=color,colored_row=colored_row, colored_row_color=colored_row_color)

def solve_trapezoidal( a:str, b:str, function:str) -> list:
    """Note a is the lower limit and b is the upper limit"""
    """This function will be different than the rest
    as this will be used also in romberg integration"""
    integrals = []
    panels = []
    table = []
    n = 1
    formula = '((({b})-({a}))/(2*{n})) * ({f_xsuba} + {middle_function} + {f_xsubb})' 

    isdone = False

    while not isdone:
        panels.append(n)
        middle_function = '0'
        f_xsubb = get_function_value(function, b)
        f_xsuba = get_function_value(function, a)
        for i in range(1,n):
            multiply_sa_b =  i/n #nahutdan nakug ingalan
            middle_value = get_function_value(function, f'{b} * {multiply_sa_b}')
            middle_function += f"+ 2*({middle_value})"
        all_function = formula.format(b=b, a=a,n=n, f_xsuba=f_xsuba, middle_function=middle_function, f_xsubb=f_xsubb)
        integral = eval(all_function)
        integrals.append(integral)
        n*=2
        if n > 2048:
            isdone = True
    
    for i in range(len(panels)):
        table.append([panels[i], integrals[i]])
   
    return table

    

def get_function_value(function:str, x):
    
    new_function = function.replace('x', str(x))
    function_value = eval(new_function) 

    return function_value

    
def display_answer(window, a,b , function, title_length, color):
        """For romberg and trapezoidal method 2 lines under the title"""
        center_y, center_x = get_the_center_screen(window)
        prompt_answer = ["function   :","upper limit: ", "lower limit: "]
        prompt_answer_length = 0
        integ_chr = u'\u222b'

        for i in prompt_answer:
            if len(i) > prompt_answer_length:
                prompt_answer_length = len(i)


        display_string(window, title_length + 2, center_x - prompt_answer_length, prompt_answer)
        display_string(window, title_length + 2, center_x, [f'{integ_chr}[{b},{a}] f(x) = {function}',b,a], color=color)
