import curses
from math import *
from project_functions import *
from prettytable import PrettyTable
from romberg import Romberg


class Trapezoidal():

    def __init__(self, window):
        self.window = window
        self.window.clear()
        self.green = curses.color_pair(1)
        self.red = curses.color_pair(2)
        self.cyan = curses.color_pair(3)
        self.yellow = curses.color_pair(4)
        self.header_color = curses.color_pair(5)
        curses.init_pair(6, 206, curses.COLOR_BLACK)
        self.pink = curses.color_pair(6)
        self.title = 'Trapezoidal'
        self.pi_chr = u'\u03C0'
        self.integ_chr = u'\u222b'
        self.solve_trapezoidal()


    def solve_trapezoidal(self):
        self.window.clear()
        self.get_required_values()
        self.table_values = solve_trapezoidal(self.a, self.b, self.function)
        table =  PrettyTable(['Panels', 'Area'])
        table.add_rows(self.table_values)
        
        self.clear_display_title()
        a = self.a.replace("pi", self.pi_chr)
        b = self.b.replace("pi", self.pi_chr)
        table_y = self.title_length + 6
        display_string_center_screen(self.window, table_y, str(table).splitlines(), colored_row=[0,1,2], colored_row_color=self.header_color)
        display_answer(self.window, a,b, self.user_function,self.title_length, self.pink)

        table_length = len(str(table).splitlines())
        self.prompt_to_romberg(table_y, table_length)

        
    def prompt_to_romberg(self,y,y_length):
        continue_prompt = "Continue to romberg? press C"
        continue_prompt_length = len(continue_prompt)
        blanks =''
        centery, centerx = get_the_center_screen(self.window)
        for i in range(len(continue_prompt)):
            blanks += " "


        self.window.addstr(y + y_length + 2, centerx - len(continue_prompt), continue_prompt)
        
        key = chr(self.window.getch())
        if key == 'c' or key == 'C':
            romberg = Romberg(self.window)
            romberg.solve_romberg_from_trapezoidal(self.a, self.b, self.user_function, self.table_values)


    def display_answer(self, a,b , function):
        center_y, center_x = get_the_center_screen(self.window)
        prompt_answer = ["function   :","upper limit: ", "lower limit: "]
        prompt_answer_length = 0

        for i in prompt_answer:
            if len(i) > prompt_answer_length:
                prompt_answer_length = len(i)


        display_string(self.window, self.title_length + 2, center_x - prompt_answer_length, prompt_answer)
        display_string(self.window, self.title_length + 2, center_x, [f'{self.integ_chr}[{b},{a}] f(x) = {function}',b,a], color=self.pink)





    def get_required_values(self):
        self.window.clear()
        self.title_length = display_title(self.window, self.title)
        centery,centerx = get_the_center_screen(self.window)

        prompt = """Enter the function below
        use 'x' as the variable"""
        display_string_center_screen(self.window, self.title_length+4, prompt.splitlines(), color=self.yellow)
        self.user_function = get_string_from_user(self.window,centerx,centery,self.title, color=self.pink)
        self.function = self.user_function.replace("^", "**")
        
        self.clear_display_title()
        prompt = 'Enter the upper limit (the b variable)'
        display_string_center_screen(self.window, self.title_length+4, prompt.splitlines(), color=self.yellow)
        self.b = get_string_from_user(self.window,centerx,centery,self.title, color=self.pink)

        self.clear_display_title()
        prompt = 'Enter the lower limit (the a variable)'
        display_string_center_screen(self.window, self.title_length+4, prompt.splitlines(), color=self.yellow)
        self.a = get_string_from_user(self.window,centerx,centery,self.title, color=self.pink)

        
    def clear_display_title(self):
        self.window.clear()
        display_title(self.window, self.title, color=self.yellow)








     