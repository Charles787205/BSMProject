import curses
from sympy import *
from project_functions import *
from prettytable import PrettyTable
from math import *

class Newton():

    def __init__(self, window):
        self.window = window
        self.window.clear()
        self.green = curses.color_pair(1)
        self.red = curses.color_pair(2)
        self.cyan = curses.color_pair(3)
        self.title = 'Newton'
        self.num_of_iterations = 6
        self.solve_newton()
    
    def solve_newton(self):
        self.title_length = self.clear_display_title()
        x = symbols('x')
        prompt = 'Enter function: (use "x" as the variable)'
        display_string_center_screen(self.window,self.title_length +4,[prompt] ,color=self.green)
        centery, centerx = get_the_center_screen(self.window)
        self.user_function = get_string_from_user(self.window, centerx, self.title_length + 7,self.title, color=self.red)
        self.user_function = self.user_function.replace('^', '**')
        

        self.clear_display_title()
        prompt = 'Enter the initial value of x (x0):'
        display_string_center_screen(self.window,self.title_length +4,[prompt] ,color=self.green)
        self.x_value = get_string_from_user(self.window, centerx, self.title_length + 7,self.title, color=self.red)

        if 'e' in self.user_function:
            self.user_function = self.user_function.replace('e', 'E')

        self.function = sympify(self.user_function)
        self.function_prime = diff(self.function)

        table = PrettyTable(['k', 'x_k','f(x_k)', "f'(x_k)", 'x_(k+1)', 'e_r'])
        x_k = eval(self.x_value)
        for k in range(self.num_of_iterations):
            f_xk = self.function.subs(x, x_k)
            fprime_xk = self.function_prime.subs(x, x_k)
            x_k1 = (x_k - (f_xk/fprime_xk))
            e_r = abs(x_k1 - x_k)
            row_val = [k, x_k, f_xk, fprime_xk, x_k1, e_r]
            table.add_row(row_val, divider=True)
            x_k = eval(str(x_k1))
        self.user_function = pretty(self.function)
        self.function_prime = pretty(self.function_prime)
        
        display_title(self.window, self.title, color=self.red)
        answer_length = self.display_answer()
        display_string_center_screen(self.window, self.title_length + answer_length + 4, str(table).splitlines(), color=self.red)

        self.window.getch()

    
    def display_answer(self):
        func_arr = self.user_function.splitlines()
        func_prime_arr = self.function_prime.splitlines()

        func_arr_xlength = 0
        func_prime_arr_xlength = 0
        centery, centerx = get_the_center_screen(self.window)
        for i in func_arr:
            if func_arr_xlength < len(i):
                func_arr_xlength = len(i)
        for i in func_prime_arr:
            if func_prime_arr_xlength < len(i):
                func_prime_arr_xlength = len(i)
        func_arr_xlength += 1 #Para sa space
        func_prime_arr_xlength += 1
        f_str = "f(x)= "
        fp_str = "f'(x)= "
        xsubk0_str = "x(k0) = "
        #compute the width of the string
        answer_width = len(f_str) + func_arr_xlength + len(fp_str) + func_prime_arr_xlength + len(xsubk0_str) + len(self.x_value)
        str_start_y = self.title_length + 2 #starting position of the string
        str_start_x = centerx - int(answer_width/2)
        
        display_string(self.window, str_start_y, str_start_x,[f_str], color=self.cyan)
        display_string(self.window,str_start_y-(len(func_arr)-1), str_start_x + len(f_str), func_arr, color=self.green)
        display_string(self.window, str_start_y, str_start_x+len(f_str) +func_arr_xlength, [fp_str], color=self.cyan)
        display_string(self.window, str_start_y-(len(func_prime_arr)-1),str_start_x+ len(f_str) + func_arr_xlength + len(fp_str), func_prime_arr, color=self.green)
        display_string(self.window, str_start_y, str_start_x+len(f_str) + func_arr_xlength + len(fp_str) + func_prime_arr_xlength, [xsubk0_str], color=self.cyan)
        display_string(self.window, str_start_y, str_start_x+len(f_str) + func_arr_xlength + len(fp_str) + func_prime_arr_xlength + len(xsubk0_str), [self.x_value], color=self.green)
        
        y1 = len(func_arr)
        y2 = len(func_prime_arr)
        
        return y1 if y1 > y2 else y2

    def clear_display_title(self):
        self.window.clear()
        return(display_title(self.window, self.title, color=self.red))