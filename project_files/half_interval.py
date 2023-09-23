import curses
from project_functions import *
from math import *
from prettytable import PrettyTable
class HalfInterval():
    
    def __init__(self, window):
        self.window = window
        self.window.clear()
        self.green = curses.color_pair(1)
        self.red = curses.color_pair(2)
        self.cyan = curses.color_pair(3)
        self.yellow = curses.color_pair(4)
        self.header_color = curses.color_pair(5)
        self.title = 'Half-Interval'
        self.solve_half_interval()

    def get_required_values(self):
        self.title_length = display_title(self.window, self.title, color=self.cyan)
        prompt = """Enter the value of f(x) below,
    Notes:
        Use 'x' as the variable
        Example:
            4x^3 + 12x^2 + 16x would be written as
            4 * x^3 + 12 * x ^ 2 + 16 * x
        """
        display_string_center_screen(self.window, self.title_length+4, prompt.splitlines())
        centery, centerx =get_the_center_screen(self.window)
        equation = get_string_from_user(self.window, centerx, centery,self.title, color=self.yellow)
        self.equation = equation.replace("^", "**")
        
        prompt = """Enter the value of x+ such that the value of f(x+) > 0"""
        display_string_center_screen(self.window, self.title_length+4, prompt.splitlines())
        self.x_pos = float(get_string_from_user(self.window, centerx, centery, self.title, color=self.yellow))

        prompt = """Enter the value of x -such that the value of f(x-) < 0"""
        display_string_center_screen(self.window, self.title_length+4, prompt.splitlines())
        self.x_neg = float(get_string_from_user(self.window, centerx, centery, self.title, color=self.yellow))

        prompt_equation = equation.strip()
        prompt_equation = prompt_equation.replace("**", '^')
        prompt_equation = prompt_equation.replace('*', "")
        self.prompt_equation = prompt_equation.replace(" ", '')
        display_string_center_screen(self.window, self.title_length+4, prompt_equation.splitlines())
    
    def solve_half_interval(self):
        self.get_required_values()
        self.window.clear()
        x_kplus1 = (self.x_pos + self.x_neg) / 2
        print(self.equation)
        fx_kplus1 = eval(self.equation.replace('x', str(x_kplus1)))
        #table_values is a list of dictionaries init first row
        k = 0
        table_values = []
        #table_values = [{'k': k , 'xk+': self.x_pos, 'xk-': self.x_neg, 'x(k+1)':x_kplus1, 'f[x(k+1)]':fx_kplus1}]
        while abs(fx_kplus1) > .01:
            if fx_kplus1 > 0:
                self.x_pos = x_kplus1
            else:
                self.x_neg = x_kplus1
            k+=1
            x_kplus1 = (self.x_pos + self.x_neg) / 2
            fx_kplus1 = eval(self.equation.replace('x', str(x_kplus1)))
            table_values.append({'k': k , 'xk+': self.x_pos, 'xk-': self.x_neg, 'x(k+1)':x_kplus1, 'f[x(k+1)]':fx_kplus1})
        
        headers = list(table_values[0].keys())
        str_table_values = self.make_table_values(table_values)

        table = PrettyTable(headers)
        table.add_rows(str_table_values)
        self.window.clear()
        table_str_arr = str(table).splitlines()
        print(table_str_arr)
        display_title(self.window, self.title, color=self.yellow)
        display_string_center_screen(self.window, self.title_length, table_str_arr, colored_row=[0,1,2], colored_row_color=self.header_color)
        final_answer = f"One root of the equation {self.prompt_equation} is {x_kplus1}"
        centery,centerx = get_the_center_screen(self.window)
        final_answer_x = centerx - int(len(final_answer)/2)
        final_answer_y = self.title_length + len(table_str_arr) + 2

        equation_x = final_answer_x + final_answer.find(f'{self.prompt_equation}')
        x_kplus1_x = final_answer_x + final_answer.find(f'{x_kplus1}')
        display_string(self.window,final_answer_y, final_answer_x, [final_answer])
        display_string(self.window, final_answer_y, equation_x, [f'{self.prompt_equation}'], self.yellow)
        display_string(self.window, final_answer_y, x_kplus1_x, [f'{x_kplus1}'], self.cyan)
        self.window.getch()

    def make_table_values(self,table_values):
        headers = list(table_values[0].keys())
        table = []
        for dict in table_values:
            table_row = []
            for col in headers:
                if col != 'k':
                    table_row.append(str('%.4f' % dict[col]).rstrip('0').rstrip('.'))
                else:
                    table_row.append(dict[col])
            table.append(table_row)
        print(table)
        return table