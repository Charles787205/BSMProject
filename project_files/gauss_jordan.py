
import curses

from project_functions import *
from gaussian_functions import *
class GaussJordan():
    
    def __init__(self,matrix,window):
        self.matrix = matrix
        self.window = window
        self.window.clear()
        self.green = curses.color_pair(1)
        self.red = curses.color_pair(2)
        self.cyan = curses.color_pair(3)
        self.blue = curses.color_pair(7)
        
        self.title = "Gauss Jordan"
        window.clear()
        self.title_height = display_title(self.window, self.title)
        self.starty = self.title_height + 4
        self.solve_gauss_jordan()
        
        
    
    def interchange(self, col_num):
        
        max_value = abs(self.matrix[col_num][col_num])#assign sa pina ka una sa
        row_with_max_value = col_num
        if self.matrix[col_num][col_num] != 1:
            for index in range(col_num, len(self.matrix)):
                value = abs(self.matrix[index][col_num])
                if value > max_value:   
                    max_value = value
                    row_with_max_value = index
            arr1 = self.matrix[col_num] #col_num naa diri kay same ra dapat sa row_num
            arr2 = self.matrix[row_with_max_value]

            self.matrix[col_num] = arr2
            self.matrix[row_with_max_value] = arr1 #diri na na change
        
        return [col_num,row_with_max_value] if col_num != row_with_max_value else [col_num,-1]
        
    def normalize(self, col): #since same ra ang col ug row nga i normalize
        val = self.matrix[col][col]
        new_row = []
        for row_val in self.matrix[col]:
            new_val = float(row_val)/float(val)
            new_row.append(new_val)
        self.matrix[col] = new_row

        process = f"R{col+1} = R{col+1} / {val}"
        return col, process

    def eliminate(self, col, row):
        value_to_eliminate = self.matrix[row][col]
        new_row_arr = []
        for index, val in enumerate(self.matrix[row]):
            prev_row_val = self.matrix[col][index]
            new_val = val - (value_to_eliminate*prev_row_val)
            new_row_arr.append(new_val)
        self.matrix[row] = new_row_arr
        return f"R{row+1} - (%.2gR{col+1})" % value_to_eliminate

    def solve_gauss_jordan(self):
        centery, centerx = get_the_center_screen(self.window)
        self.matrix_width = self.draw_matrix(centerx, process=["Matrix"])
        first_matrix_startx = centerx - (self.matrix_width + 2)
        second_matrix_startx = first_matrix_startx + (self.matrix_width+2) + 2 # dili + 4 para mas dali masabtan ang logic
        

        self.title_height = display_title(self.window, self.title)
        self.starty = self.title_height + 4

        #Ipakita sa ang starting matrix
        
        #self.window.addstr(starty, second_matrix_startx -2, '>>')
        
        for row_ind, row in enumerate(self.matrix):
            
            #First Phase interchange sa PIVOT
            self.window.clear() 
            display_title(self.window, self.title,color=self.green)
            self.matrix_width = self.draw_matrix(first_matrix_startx, process=["Matrix"])
            row_with_max, row_changed = self.interchange(row_ind )
            interchange_process = ["Interchange"]
            if row_changed == -1:
                interchange_process.append('Not necessary')
            else:
                interchange_process.append(f'R{row_changed+1} -> R{row_with_max+1}')
            self.matrix_width =self.draw_matrix(second_matrix_startx, process=interchange_process, colored_row={row_with_max:self.green, row_changed:self.red})
            self.window.getch()

            #Normalization
            self.window.clear()
            display_title(self.window, self.title,color=self.green)
            self.matrix_width = self.draw_matrix(first_matrix_startx, process=["Interchanged Matrix"])
            col, process = self.normalize(row_ind)
            self.matrix_width = self.draw_matrix(second_matrix_startx,
                            process=["Normalize", f"{process}"],
                            colored_row={row_ind:self.green})
            self.window.refresh()
            self.window.getch()

            #Elimination najud
            '''First for loop elimination pababa sa 1

                Second for loop elimination sa taas maong naay if
            
            '''
            for col_ind in range(row_ind+1, len(self.matrix)):
                first_matrix_startx = centerx - (self.matrix_width + 2) - 5
                second_matrix_startx = first_matrix_startx + (self.matrix_width+2) + 2
                self.window.clear()
                display_title(self.window, self.title,color=self.green)
                self.matrix_width = self.draw_matrix(first_matrix_startx, process=["Past Matrix"]) #Display and daan na matrix
                process = self.eliminate(row_ind, col_ind)                                         #I eliminate
                self.matrix_width = self.draw_matrix(second_matrix_startx,                         #Display ang bag.o side by side
                                process=["Eliminate", process],
                                colored_row={col_ind: self.green})
                self.window.getch()
            if(row_ind > 0):
                for col_ind in range(row_ind-1, -1,-1):
                    first_matrix_startx = centerx - (self.matrix_width + 2) - 5
                    second_matrix_startx = first_matrix_startx + (self.matrix_width+2) + 2
                    self.window.clear()
                    display_title(self.window, self.title,color=self.green)                                
                    self.matrix_width = self.draw_matrix(first_matrix_startx, process=["Past Matrix"]) #Same ra sa taas
                    process = self.eliminate(row_ind, col_ind)
                    self.matrix_width = self.draw_matrix(colored_row={col_ind: self.green},
                                    process = ["Eliminate", process],
                                    startx=second_matrix_startx)
                    self.window.getch()
        final_answer =''
        for index, row in enumerate(self.matrix):
            final_answer += f"xsub{index+1} = {str('%.4f' % row[len(row)-1]).rstrip('0').rstrip('.')}\n"
        y,x = get_the_center_screen(self.window)
        display_string(self.window,y ,x-7 , final_answer.splitlines(), color=self.cyan)
        self.window.getch()


    def draw_matrix(self, startx, process=[], colored_row={}):
        return draw_matrix(self.window, self.matrix, startx=startx, starty=self.starty, colored_row=colored_row, process=process)

 
    
