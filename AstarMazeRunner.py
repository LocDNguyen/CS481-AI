# USES Astar_gen FILE #
# USES Astar_gen FILE #
# USES Astar_gen FILE #

import ast
from tkinter import *
from tkinter import messagebox
from scroll import *
from Astar_gen import *

saved_path_generator = None
first_run = True
astar_path = None
astar_travelled_path = None
global maze
global rows
global cols
global wall
global start_x
global start_y
global end_x
global end_y

root.title("A* Maze Runner")
# Image from https://wildfiremotionpictures.com/2014/10/08/film-review-the-maze-runner-2014/
image = PhotoImage(file='maze.png')
root.iconphoto(False, image)
root.geometry("550x500+200+100")

def enter():
    global rows
    global cols
    global wall
    global start_x
    global start_y
    global end_x
    global end_y
    global first_run
    global maze
    for label in fTable.grid_slaves():
        if int(label.grid_info()["row"]) > 7:
            label.grid_forget()

    back_button.config(state=DISABLED)
    generate_steps.config(state=DISABLED)
    show_complete_maze.config(state=DISABLED)
    first_run = True

    rows = int(num_of_rows.get())
    cols = int(num_of_cols.get())
    wall = float(wall_prob.get())
    start_x = int(start_coord.get())
    start_y = int(start_coord_two.get())
    end_x = int(end_coord.get())
    end_y = int(end_coord_two.get())
    if start_x < 1 or start_x > rows-2 or start_y < 1 or start_y > cols-2:
        messagebox.showerror('???', 'Error: Invalid Start Coordinate!')
        start_coord.delete(0, END)
        start_coord_two.delete(0, END)
        start_coord.insert(0, "Ex: 1")
        start_coord_two.insert(0, "Ex: 1")
        return
    if end_x < 1 or end_x > rows-2 or end_y < 1 or end_y > cols-2:
        messagebox.showerror('???', 'Error: Invalid End Coordinate!')
        end_coord.delete(0, END)
        end_coord_two.delete(0, END)
        end_coord.insert(0, "Ex: 8")
        end_coord_two.insert(0, "Ex: 8")
        return

    # code similar to begin()
    maze = generate_maze(rows, cols, wall, start_x, start_y, end_x, end_y)
    temp = maze
    Label(fTable, text="Initial Maze:").grid(pady=2, column=0, row=8)
    for row in maze:
        Label(fTable, text=" ".join(map(str,row)), borderwidth=1, font=("Liberation Mono", "10")).grid(pady=2, column=0)
        updateScrollRegion()
    final = finish(temp, start_x, start_y, end_x, end_y)
    if final == None:
        Label(fTable, text="No valid path found.").grid(row=8, column=1)
    else:
        Label(fTable, text="Shortest Path:").grid(pady=2, row=8, column=1)
        show_complete_maze.config(state=NORMAL)
        generate_steps.config(state=NORMAL)
        

            

def instant():
    # Display A* maze
    for label in fTable.grid_slaves():
        if int(label.grid_info()["row"]) > 8 and int(label.grid_info()["column"]) > 0:
            label.grid_forget()

    final = finish(maze, start_x, start_y, end_x, end_y)
    r = 9
    for row in final:
        Label(fTable, text=" ".join(map(str,row)), borderwidth=1, font=("Liberation Mono", "10")).grid(pady=2, row=r, column=1)
        r += 1
        updateScrollRegion()
    


def clear():
    num_of_rows.delete(0, END)
    num_of_cols.delete(0, END)
    wall_prob.delete(0, END)
    start_coord.delete(0, END)
    start_coord_two.delete(0, END)
    end_coord.delete(0, END)
    end_coord_two.delete(0, END)

    for label in fTable.grid_slaves():
        if int(label.grid_info()["row"]) > 7:
            label.grid_forget()

    back_button.config(state=DISABLED)
    generate_steps.config(state=DISABLED)
    show_complete_maze.config(state=DISABLED)
    
    # reset the step variables
    global saved_path_generator 
    saved_path_generator= None
    global astar_path
    astar_path = None
    global first_run
    first_run = True
    global astar_travelled_path
    astar_travelled_path = None

    num_of_rows.insert(0, "Ex: 5, 10, 20")
    num_of_cols.insert(0, "Ex: 5, 10, 20")
    wall_prob.insert(0, "Ex: .1, .2, .3")
    start_coord.insert(0, "Ex: 1")
    start_coord_two.insert(0, "Ex: 1")
    end_coord.insert(0, "Ex: 8")
    end_coord_two.insert(0, "Ex: 8")


def step_display():
    #only run this code on the first run: it creates the maze, error checks, and saves information to global variables 
    global first_run
    for label in fTable.grid_slaves():
        if int(label.grid_info()["row"]) > 8 and int(label.grid_info()["column"]) > 0:
            label.grid_forget()
    if first_run:
        # for label in fTable.grid_slaves():
        #     if int(label.grid_info()["row"]) > 8 and int(label.grid_info()["column"]) > 0:
        #         label.grid_forget()
        start = (start_x, start_y)
        goal = (end_x, end_y)
        global saved_path_generator
        saved_path_generator = astar_pathfind_gen(maze, start, goal)
        global astar_path
        astar_path = []
        
        first_run = False
        global astar_travelled_path
        astar_travelled_path = []

        for node in saved_path_generator:
            #print(node, end=", ")
            astar_path.append(node)

        #Label(fTable, text="Shortest Path:").grid(pady=2, row=8, column=1)
        # r = 9
        # for row in maze:
        #     Label(fTable, text=" ".join(map(str,row)), borderwidth=1, font=("Liberation Mono", "10")).grid(pady=2, row=r, column=1)
        #     r += 1
        #     updateScrollRegion()

    r=9 # need to redeclare since r is created in the firstrun section
    # for label in fTable.grid_slaves():
    #     if int(label.grid_info()["row"]) > 8 and int(label.grid_info()["column"]) > 0:
    #         label.grid_forget()
            

    # build path
    # if len(astar_path) == 0:
    #     print('ere')
    #     astar_path = astar_travelled_path
    #     astar_travelled_path = []
    #     for i in range(len(astar_travelled_path)):
    #         step_maze[astar_travelled_path[i][0]][astar_travelled_path[i][1]] = " "
    #     # debug
    #     print_maze(maze)

    step_maze = maze[:]    # PROBLEM: Maze is getting updated with * characters, is not getting reset
    for i in range(len(astar_travelled_path)):
        step_maze[astar_travelled_path[i][0]][astar_travelled_path[i][1]] = '★'
    step_maze[astar_path[0][0]][astar_path[0][1]] = '★'

    astar_travelled_path.append(astar_path.pop(0))


    for row in maze:
        Label(fTable, text=" ".join(map(str,row)), borderwidth=1, font=("Liberation Mono", "10")).grid(pady=2, row=r, column=1)
        r += 1
        updateScrollRegion()

    # debug
    print("Viewed from N:")
    print(astar_travelled_path)
    print("To be viewed N:")
    print(astar_path)


    if not astar_path:
        generate_steps.config(state=DISABLED)
    else:
        back_button.config(state=NORMAL)

def back():
    r = 9
    step_maze = maze[:]
    for i in range(len(astar_path)):
        step_maze[astar_path[i][0]][astar_path[i][1]] = " "

    astar_path.insert(0, astar_travelled_path.pop(-1))

    for row in step_maze:
        Label(fTable, text=" ".join(map(str,row)), borderwidth=1, font=("Liberation Mono", "10")).grid(pady=2, row=r, column=1)
        r += 1
        updateScrollRegion()

    # debug
    print("Viewed from P:")
    print(astar_travelled_path)
    print("To be viewed P:")
    print(astar_path)

    if not astar_travelled_path:
        back_button.config(state=DISABLED)
    else:
        generate_steps.config(state=NORMAL)
    

# Adding/Removing example text in entry boxes
def remove_row_text():
    if num_of_rows.get() != "":
        num_of_rows.delete(0, END)
def remove_col_text():
    if num_of_cols.get() != "":
        num_of_cols.delete(0, END)
def remove_wall_text():
    if wall_prob.get() != "":
        wall_prob.delete(0, END)
def remove_start_text():
    if start_coord.get() != "":
        start_coord.delete(0, END)
def remove_start_two_text():
    if start_coord_two.get() != "":
        start_coord_two.delete(0, END)
def remove_end_text():
    if end_coord.get() != "":
        end_coord.delete(0, END)
def remove_end_two_text():
    if end_coord_two.get() != "":
        end_coord_two.delete(0, END)
def add_row_text():
    if num_of_rows.get() == "":
        num_of_rows.insert(0, "Ex: 5, 10, 20")
def add_col_text():
    if num_of_cols.get() == "":
        num_of_cols.insert(0, "Ex: 5, 10, 20")
def add_wall_text():
    if wall_prob.get() == "":
        wall_prob.insert(0, "Ex: .1, .2, .3")
def add_start_text():
    if start_coord.get() == "":
        start_coord.insert(0, "Ex: 1")
def add_start_two_text():
    if start_coord_two.get() == "":
        start_coord_two.insert(0, "Ex: 1")
def add_end_text():
    if end_coord.get() == "":
        end_coord.insert(0, "Ex: 8")
def add_end_two_text():
    if end_coord_two.get() == "":
        end_coord_two.insert(0, "Ex: 8")


# Create text boxes
num_of_rows = Entry(fTable, width=12)
num_of_rows.grid(row=0, column=1, padx=20)
num_of_rows.insert(0, "Ex: 5, 10, 20")
num_of_cols = Entry(fTable, width=12)
num_of_cols.grid(row=1, column=1, padx=20)
num_of_cols.insert(0, "Ex: 5, 10, 20")
wall_prob = Entry(fTable, width=12)
wall_prob.grid(row=2, column=1, padx=20)
wall_prob.insert(0, "Ex: .1, .2, .3")

start_coord = Entry(fTable, width=5)
start_coord.grid(row=3, column=1, padx=20, sticky=W)
start_coord.insert(0, "Ex: 1")
start_coord_two = Entry(fTable, width=5)
start_coord_two.grid(row=3, column=1, padx=20, sticky=E)
start_coord_two.insert(0, "Ex: 1")

end_coord = Entry(fTable, width=5)
end_coord.grid(row=4, column=1, padx=20, sticky=W)
end_coord.insert(0, "Ex: 8")
end_coord_two = Entry(fTable, width=5)
end_coord_two.grid(row=4, column=1, padx=20, sticky=E)
end_coord_two.insert(0, "Ex: 8")

# Create text box labels
rows_label = Label(fTable, text="Number of Rows:").grid(row=0, column=0, padx=20, pady=5)
cols_label = Label(fTable, text="Number of Columns:").grid(row=1, column=0, padx=20)
wall_label = Label(fTable, text="Wall probability (Range: 0-1):").grid(row=2, column=0, padx=20, pady=5)

start_label = Label(fTable, text="Start Coordinate:").grid(row=3, column=0, padx=20)
open_parenth_label = Label(fTable, text="(").grid(row=3, column=0, sticky=E)
comma_label = Label(fTable, text=",").grid(row=3, column=1, padx=20, sticky=S)
close_parenth_label = Label(fTable, text=")").grid(row=3, column=2, sticky=W)

end_label = Label(fTable, text="End Coordinate:").grid(row=4, column=0, padx=20, pady=5)
open_parenth_label = Label(fTable, text="(").grid(row=4, column=0, sticky=E)
comma_label = Label(fTable, text=",").grid(row=4, column=1, padx=20, sticky=S)
close_parenth_label = Label(fTable, text=")").grid(row=4, column=2, sticky=W)

# Create buttons for creating the maze and clearing everything
pass_arguments = Button(fTable, text="Enter", command=enter, width=10, padx=10, pady=1).grid(row=4, column=3, padx=20, pady=10)

back_button = Button(fTable, text="Generate Previous Step", command=back, width=18, padx=5, pady=1, state=DISABLED)
back_button.grid(row=6, column=0, pady=10)

generate_steps = Button(fTable, text="Generate Next Step", command=step_display, width=18, padx=5, pady=1, state=DISABLED)
generate_steps.grid(row=6, column=1, pady=10)

show_complete_maze = Button(fTable, text="Instant", command=instant, width=10, padx=5, pady=1, state=DISABLED)
show_complete_maze.grid(row=7, column=0, pady=10)

clear_arguments = Button(fTable, text="Clear", command=clear, width=10, padx=5, pady=1).grid(row=7, column=1)

# Allow keyboard keys to activate buttons
root.bind('<Return>', lambda event:enter())
# root.bind('<Left>', lambda event:back())
# root.bind('<Right>', lambda event:step_display())

# Entry box descriptions
num_of_rows.bind("<FocusIn>", lambda event:remove_row_text())
num_of_rows.bind("<FocusOut>", lambda event:add_row_text())
num_of_cols.bind("<FocusIn>", lambda event:remove_col_text())
num_of_cols.bind("<FocusOut>", lambda event:add_col_text())
wall_prob.bind("<FocusIn>", lambda event:remove_wall_text())
wall_prob.bind("<FocusOut>", lambda event:add_wall_text())
start_coord.bind("<FocusIn>", lambda event:remove_start_text())
start_coord.bind("<FocusOut>", lambda event:add_start_text())
start_coord_two.bind("<FocusIn>", lambda event:remove_start_two_text())
start_coord_two.bind("<FocusOut>", lambda event:add_start_two_text())
end_coord.bind("<FocusIn>", lambda event:remove_end_text())
end_coord.bind("<FocusOut>", lambda event:add_end_text())
end_coord_two.bind("<FocusIn>", lambda event:remove_end_two_text())
end_coord_two.bind("<FocusOut>", lambda event:add_end_two_text())

# If user clicks on an empty space, the insert cursor will disappear from the entry box
root.bind("<1>", lambda event: event.widget.focus_set())

root.mainloop()
