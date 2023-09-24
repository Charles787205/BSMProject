import curses
from project_functions import *
from math import *
from prettytable import PrettyTable

class Romberg():
    
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
        self.title = 'Romberg'
        self.pi_chr = u'\u03C0'
        self.integ_chr = u'\u222b'
     
    def solve_romberg_from_trapezoidal(self,a:str,b:str,user_function:str, trapezoidal_table): #continuing trapezoidal method, from trapezoidal to romberg
        self.a = a
        self.b = b
        self.user_function = user_function
        self.function = self.user_function.replace('^', '**')
        self.trapezoidal_table = trapezoidal_table
        table = self.solve_romberg()
        self.display_romberg(table)

    def solve_romberg_from_romberg(self):  #solve  romberg from romberg
        self.get_required_values()
        self.trapezoidal_table = solve_trapezoidal(self.a, self.b, self.function)
        table = self.solve_romberg()
        
    def display_romberg(self,table):
        self.window.clear()
        self.title_length = display_title(self.window, self.title, color=self.pink)
        display_string_center_screen(self.window, self.title_length + 6, str(table).splitlines())
        self.table_length = len(str(table).splitlines())
        display_answer(self.window, self.a, self.b, self.user_function, self.title_length, color=self.cyan)
        self.window.getch()
    
    def solve_romberg(self) -> PrettyTable:
        table_values = []
        romberg_formula = "((4**{n}) * ({ma} - {la}))/ ((4**{n}) - 1) " #ma = more accurate la=less acurate
        integral_index = 1 #index sa integrals sa table, for faster undestanding less magic numbers
        for i in range(4):
            
            table_values.append([self.trapezoidal_table[i][0],'%.5f' %self.trapezoidal_table[i][1],'','','']) #initialize the table with the value of trapezoidal table (the strips and integral :*), and blank in n=1, n=2
        for row in range(len(table_values)):
            for col in range(2,5):
                if col < row + 2:
                    ma = table_values[row][integral_index]
                    la = table_values[row-1][integral_index]
                    column_value = '%.5f' % eval(romberg_formula.format(n=row, ma=ma,la=la))
                    table_values[row][col] = column_value
                
        
        column_headers = ['Strips', 'Integrals', 'n=1', 'n=2', 'n=3']
        table = PrettyTable(column_headers)
        table.add_rows(table_values)
        return table
                

            

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
    

