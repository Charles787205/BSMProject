import curses
from math import *
from project_functions import *
from prettytable import PrettyTable

class Moss():
    def __init__(self, window) -> None:
        self.window = window
        self.green = curses.color_pair(1)
        self.red = curses.color_pair(2)
        self.cyan = curses.color_pair(3)
        self.title = 'Moss'
        self.window.clear()
        self.solve_moss()
        

    def solve_moss(self):
        self.title_length = display_title(self.window, self.title)
        prompt ="""
Please enter the equation
Operations:
    + is addition
    - is subtraction
    * is multiplication
    / is division
    ** exponentiation
    sqrt() for squareroot
Use 'x' as the variable
"""     
        self.display_prompt(prompt)
        y,x = get_the_center_screen(self.window)
        
        user_input_equation = get_string_from_user(self.window, x, y+3, self.title)
        
        
        prompt = "Enter the initial value of x"
        self.window.clear()
        display_title(self.window, self.title)
        self.display_prompt(prompt)
        x_value = float(get_string_from_user(self.window, x, y+3, self.title))

        prompt = "Enter the number of iteration (k)"
        self.window.clear()
        display_title(self.window, self.title)
        self.display_prompt(prompt)
        iterations = int(get_string_from_user(self.window, x, y+3, self.title))


        
        x_values = []
        for i in range(iterations+1):
            print(x_value)
            x_values.append(x_value)
            equation = user_input_equation.replace('x', f'{x_value}')
            x_value = eval(equation)
        table = []
        relative_errors = []
        for k in range(len(x_values)-1):
            str_form = '{val:.4f}'
            relative_error = (x_values[k+1] - x_values[k]) / x_values[k+1]
            relative_errors.append(relative_error)
            table.append([
                k,
                str_form.format(val=x_values[k]), 
                str_form.format(val=x_values[k+1]), 
                str_form.format(val=relative_error),
            ])
            
        
        """Tan.awon kung converging ba o diverging"""
        isSmaller = True
        for i in range(len(relative_errors)-1):
            if(relative_errors[i] <= relative_errors[i+1]):
                isSmaller = False
            print(isSmaller)

        self.draw_moss_table(table, 'Converging' if isSmaller else 'Diverging')


    def draw_moss_table(self,table_values:list, final_answer:str):
        
        
        headers = ['k', "x", 'xsub1', 'd'] 
        max_y, max_x = self.window.getmaxyx()
        center_y,center_x = get_the_center_screen(self.window)

        self.window.clear()
        display_title(self.window, self.title)


        table_y = self.title_length + 4 #4 rows gikan sa title
        table_x = center_x  

        final_answer_y = self.title_length + 2
        final_answer_x = center_x - 5 #length sa converging ug diverging divided by 2 (magic)

        table = PrettyTable(headers)
        table.add_rows(table_values)

        table_str_array =  str(table).splitlines()
        table_length = len(table_str_array[0])
        table_x = center_x - int(table_length/2)
        display_string(self.window, table_y, table_x, table_str_array, self.green)
        display_string(self.window, final_answer_y, final_answer_x, [final_answer], self.cyan)
        curses.curs_set(0)
        self.window.getch()

    
    def display_prompt(self, prompt):
        
        
        prompt_array = prompt.splitlines()

        longest_string = 0
        for string in prompt_array:
            if len(string) > longest_string:
                longest_string = len(string)
        y,x = get_the_center_screen(self.window)
        string_x = x - int(longest_string/2)
        string_y = self.title_length + 4
        display_string(self.window,string_y, string_x, prompt_array, color=self.cyan)
        

