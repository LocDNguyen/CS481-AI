from tkinter import *
from maze import start, finish
from scroll import *



root.title("A* Maze Runner")


def enter():
    for label in fTable.grid_slaves():
        if int(label.grid_info()["row"]) > 3:
            label.grid_forget()

    rows = int(num_of_rows.get())
    cols = int(num_of_cols.get())
    wall = float(wall_prob.get())
    r = 5

    # Display initial maze
    begin = start(rows, cols, wall)
    Label(fTable, text="Initial Maze:").grid(pady=2, column=0)
    for row in begin:
        Label(fTable, text=" ".join(map(str,row)), borderwidth=1).grid(pady=2, column=0)
        updateScrollRegion()

    # Display A* maze
    final = finish(rows, cols, begin)
    if final == "None":
        Label(fTable, text="No valid path found.").grid(row=4, column=1)
    else:
        Label(fTable, text="Shortest Path:").grid(pady=2, row=4, column=1)
        for row in final:
            Label(fTable, text=" ".join(map(str,row)), borderwidth=1).grid(pady=2, row=r, column=1)
            r += 1
            updateScrollRegion()

def clear():
    num_of_rows.delete(0, END)
    num_of_cols.delete(0, END)
    wall_prob.delete(0, END)
    for label in fTable.grid_slaves():
        if int(label.grid_info()["row"]) > 3:
            label.grid_forget()


# Create text boxes
num_of_rows = Entry(fTable, width=20)
num_of_rows.grid(row=0, column=1, padx=20)
num_of_cols = Entry(fTable, width=20)
num_of_cols.grid(row=1, column=1, padx=20)
wall_prob = Entry(fTable, width=20)
wall_prob.grid(row=2, column=1, padx=20)

# Create text box labels
rows_label = Label(fTable, text="Number of Rows:").grid(row=0, column=0, padx=20, pady=5)
cols_label = Label(fTable, text="Number of Columns:").grid(row=1, column=0, padx=20)
wall_label = Label(fTable, text="Wall probability (Range: 0-1):").grid(row=2, column=0, padx=20, pady=5)

# Create buttons for creating the maze and clearing everything
pass_arguments = Button(fTable, text="Enter", command=enter, width=10, padx=5, pady=1).grid(row=3, column=0, pady=10)

clear_arguments = Button(fTable, text="Clear", command=clear, width=10, padx=5, pady=1).grid(row=3, column=1)

# Allow keyboard enter key to create maze
root.bind('<Return>',lambda event:enter())


root.mainloop()