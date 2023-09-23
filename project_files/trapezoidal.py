import curses
from math import *
from project_functions import *
from prettytable import PrettyTable


class Trapezoidal():

    def __init__(self, window):
        self.window = window
        self.window.clear()
        self.green = curses.color_pair(1)
        self.red = curses.color_pair(2)
        self.cyan = curses.color_pair(3)
        self.yellow = curses.color_pair(4)
        self.header_color = curses.color_pair(5)
        self.title = 'Trapezoidal Method'
        self.pi_chr = u'\u03C0'
        self.integ_chr = u'\u222b'
        self.solve_trapezoidal()


    def solve_trapezoidal(self):
        self.window.clear()
        self.get_required_values()
        table_values = solve_trapezoidal(self.a, self.b, self.function)
        table =  PrettyTable(['Panels', 'Area'])
        table.add_rows(table_values)
        self.clear_display_title()
        display_string_center_screen(self.window, self.title_length + 4, str(table).splitlines(), colored_row=[0,1,2], colored_row_color=self.header_color)
        self.window.getch()

    def get_required_values(self):
        self.window.clear()
        self.title_length = display_title(self.window, self.title)
        centery,centerx = get_the_center_screen(self.window)

        prompt = """Enter the function below
        use 'x' as the variable"""
        display_string_center_screen(self.window, self.title_length+4, prompt.splitlines(), color=self.yellow)
        self.function = get_string_from_user(self.window,centerx,centery,self.title, color=self.green)

        
        self.clear_display_title()
        prompt = 'Enter the upper limit (the b variable)'
        display_string_center_screen(self.window, self.title_length+4, prompt.splitlines(), color=self.yellow)
        self.b = get_string_from_user(self.window,centerx,centery,self.title, color=self.yellow)

        self.clear_display_title()
        prompt = 'Enter the lower limit (the a variable)'
        display_string_center_screen(self.window, self.title_length+4, prompt.splitlines(), color=self.yellow)
        self.a = get_string_from_user(self.window,centerx,centery,self.title, color=self.yellow)

        
    def clear_display_title(self):
        self.window.clear()
        display_title(self.window, self.title, color=self.yellow)







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

    
    
     