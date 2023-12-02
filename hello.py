# USES maze FILE #
# USES maze FILE #
# USES maze FILE #

from tkinter import *
from tkinter import messagebox
from maze import start, finish
from scroll import *


root.title("A* Maze Runner")
# Image from https://wildfiremotionpictures.com/2014/10/08/film-review-the-maze-runner-2014/
image = PhotoImage(file='maze.png')
root.iconphoto(False, image)
root.geometry("400x500+200+100")

def enter():
    for label in fTable.grid_slaves():
        if int(label.grid_info()["row"]) > 7:
            label.grid_forget()

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

    # Display initial maze
    begin = start(rows, cols, wall, start_x, start_y, end_x, end_y)
    Label(fTable, text="Initial Maze:").grid(pady=2, column=0, row=8)
    for row in begin:
        Label(fTable, text=" ".join(map(str,row)), borderwidth=1).grid(pady=2, column=0)
        updateScrollRegion()

    # Display A* maze
    final = finish(begin, start_x, start_y, end_x, end_y)
    r = 9
    if final == "None":
        Label(fTable, text="No valid path found.").grid(row=8, column=1)
    else:
        Label(fTable, text="Shortest Path:").grid(pady=2, row=8, column=1)
        for row in final:
            for i in row:
                Label(fTable, text=" ".join(map(str,i)), borderwidth=1).grid(pady=2, row=r, column=1)
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
    
    num_of_rows.insert(0, "Ex: 5, 10, 20")
    num_of_cols.insert(0, "Ex: 5, 10, 20")
    wall_prob.insert(0, "Ex: .1, .2, .3")
    start_coord.insert(0, "Ex: 1")
    start_coord_two.insert(0, "Ex: 1")
    end_coord.insert(0, "Ex: 8")
    end_coord_two.insert(0, "Ex: 8")

    root.bind("<1>", lambda event: event.widget.focus_set())

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
pass_arguments = Button(fTable, text="Enter", command=enter, width=10, padx=5, pady=1).grid(row=6, column=0, pady=10)

clear_arguments = Button(fTable, text="Clear", command=clear, width=10, padx=5, pady=1).grid(row=6, column=1)

test_button_right = Button(fTable, text=">", width=5, padx=5, pady=1).grid(row=7, column=1)
test_button_left = Button(fTable, text="<", width=5, padx=5, pady=1).grid(row=7, column=0)

# Allow keyboard enter key to create maze
root.bind('<Return>', lambda event:enter())

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