import curses
from project_functions import *




"""This is the functions that is shared among the gaussian methods"""

def get_matrix_from_user(window,title, color=None):
    
    display_title(window, title=title,color=color)
    prompt = """Enter the matrix below, note that the number of columns in 
    the first row will determine the number of rows. 
    Press spacebar for new column and enter for next row"""
    prompt_array = prompt.splitlines()
    prompt_x_length = len(prompt_array[0])
    prompt_y_length = len(prompt_array)
    center_screen_y, center_screen_x = get_the_center_screen(window)
    prompt_x = center_screen_x - int(prompt_x_length/2)
    prompt_y = center_screen_y - int(prompt_y_length/2)

    #display_string(window, prompt_y, prompt_x, prompt_array)
    #window.getch()
    is_next_row = False
    user_input = ''
    input_y = prompt_y+prompt_y_length+2 #input x ug y  kung asa mugawas ang input sa user para makita niya
    input_x = 0 
    input_start_x = center_screen_x
    line_number = 0 #kung asa na line nag input si user
    string_matrix = ""
    matrix_made = False
    row_to_add, col_to_add = 1,0 #init 
    matrix = []
    gap = 0
    while(not is_next_row):
        window.clear()
        input_arr = user_input.splitlines()
        display_title(window, title=title)
        display_string(window, prompt_y, prompt_x, prompt_array)
        if matrix_made:
            string_matrix_arr = string_matrix.splitlines()
            
            matrixx = center_screen_x - int(len(string_matrix_arr[0])/2)
            matrixy = prompt_y+prompt_y_length+2
            display_string(window, matrixy, matrixx, string_matrix_arr)
            
            window.move(matrixy+(row_to_add), matrixx+(gap + col_to_add * len(matrix[0]))+2)
            key = window.getch()
            curses.curs_set(0)
            if key == 32 or key==10: #ascii sa spacebar
                
                user_input = ""
                col_to_add += 1
                if col_to_add >= len(matrix[0]):
                    col_to_add =0
                    row_to_add +=1
                    if row_to_add >= len(matrix):
                        break
            elif key == 8: #backspace
                user_input = user_input[:-1]

            else:
                user_input += chr(key)
                
            string_matrix,matrix,gap = make_string_matrix_from_user_input(window, user_input, matrix,row_to_add,col_to_add )
            
        else:
            if len(input_arr) == 0:
                input_x = input_start_x
            else:
                input_x =  input_start_x if len(input_arr[-1]) == 0 else center_screen_x - int(len(input_arr[-1])/2)
            display_string(window, prompt_y+prompt_y_length+2,input_x, input_arr) #display the user_input
            
            
            window.move(prompt_y+prompt_y_length+1 + len(input_arr), center_screen_x+int(len(user_input)/2)+1) #move cursor
            key = window.getch()
            if key == 10: #Ascii sa enter
                
                line_number += 1
                string_matrix, matrix = make_matrix_from_first_row(window, user_input)
                matrix_made = True
                user_input = ""
                
            elif key == 8: #Ascii sa backspace
                user_input = user_input[:-1]
            elif key == ord('e'): #exit
                is_next_row = True
            else:
                user_input += chr(key)
                window.addch(prompt_y+prompt_y_length+2, center_screen_x-1, chr(key))
    return matrix
    
def make_string_matrix_from_user_input(window, user_input, matrix, row_to_add, col_to_add):
    
    gap = 0
    string_matrix = ''
    matrix[row_to_add][col_to_add] = user_input
    for row_ind, row in enumerate(matrix):
        for ind, col in enumerate(matrix[row_ind]):
            if len(str(col)) > gap:
                gap = len(str(col))
    
    for row_ind, row in enumerate(matrix): 
        string_matrix += "|"
        for col_ind, col in enumerate(matrix[row_ind]):
            if row_ind == row_to_add:
                if col_ind > col_to_add:
                    if(col_ind == len(row)-1):
                        string_matrix += " :{:<{width}} ".format("_", width=gap+2)
                    else:
                        string_matrix += " {:<{width}} ".format("_", width=gap+2)
                else:
                    if(col_ind == len(row)-1):
                        string_matrix += " :{:<{width}} ".format(col, width=gap+2)
                    else:
                        string_matrix += " {:<{width}} ".format(col, width=gap+2)
                        
            elif row_ind > row_to_add:
                if col_ind > col_to_add:
                    if(col_ind == len(row)-1):
                        string_matrix += " :{:<{width}} ".format("_", width=gap+2)
                    else:
                        string_matrix += " {:<{width}} ".format("_", width=gap+2)
                else:
                    if(col_ind == len(row)-1):
                        string_matrix += " :{:<{width}} ".format("_", width=gap+2)
                    else:
                        string_matrix += " {:<{width}} ".format("_", width=gap+2)
            else:
                if(col_ind == len(row)-1):
                    string_matrix += " :{:<{width}} ".format(col, width=gap+2)
                else:
                    string_matrix += " {:<{width}} ".format(col, width=gap+2)
            
        string_matrix += "|\n"
    return string_matrix, matrix, gap
        

    

def make_matrix_from_first_row(window, user_input):
    columns = user_input.split()
    gap = 0
    string_matrix = ""
    matrix =[]
    matrix += [columns]
    for col in columns:
        if len(col) > gap:
            gap = len(col)
    string_matrix += '|'
    for index,col in enumerate(columns):
        
        if(index == len(columns)-1):
            string_matrix += " :{:<{width}} ".format(col, width=gap+2)
        else:
            string_matrix += " {:<{width}} ".format(col, width=gap+2)
    string_matrix += '|'
    for col in range(0, len(columns)-2): #ADD THE NONE EXISTING MATRIX
        string_matrix += "\n"
        string_matrix += '|'
        row = []
        for index,col in enumerate(columns):
            row.append(0)
            if(index == len(columns)-1):
                string_matrix += " :{:<{width}} ".format("_", width=gap+2)
            else:
                string_matrix += " {:<{width}} ".format("_", width=gap+2)
        string_matrix += '|'
        matrix += [row]
        
    
    return string_matrix, matrix

def draw_matrix(window, matrix, startx, starty, colored_row = {}, process=[]):
    gap = 0
    string_matrix_length = 0
    stringy = starty
    starty += 4 #ang two kay gap gikan sa process title to matrix
    for row_ind, row in enumerate(matrix):
        for ind, col in enumerate(matrix[row_ind]):
            length = len('{:.4g}'.format(col).rstrip('0').rstrip('.'))
            if length > gap:
                gap = length
    for row_ind, row in enumerate(matrix):
        string_matrix = '|'
        for col_ind, col in enumerate(row):
            formatted_col = '{:.4g}'.format(col)
            if formatted_col == '-0':
                formatted_col = '0'
            if(col_ind == len(row)-1):
                string_matrix += " :{:<{width}} ".format(formatted_col, width=gap)
            else:
                string_matrix += " {:<{width}} ".format(formatted_col, width=gap)
        string_matrix += '|'
        if(string_matrix_length == 0):
            string_matrix_length = len(string_matrix)
        if row_ind in colored_row:
            window.addstr(starty, startx, string_matrix, colored_row.get(row_ind))
        else:
            window.addstr(starty, startx, string_matrix)
        starty += 1
    
    for ind, string in enumerate(process):
        centerx = int(string_matrix_length/2) + startx
        stringx = centerx - int(len(string)/2)
        stringy += 1
        window.addstr(stringy, stringx, string, curses.color_pair(3-ind))

    return string_matrix_length