from tkinter import *
from maze import start, finish

# Has to happen before anything else
root = Tk()
root.title("TBD")
#root.geometry("400x400")


# Display maze
def enter():
    for label in root.grid_slaves():
        if int(label.grid_info()["row"]) > 3:
            label.grid_forget()

    rows = int(num_of_rows.get())
    cols = int(num_of_cols.get())
    wall = float(wall_prob.get())
    r = 5

    # Display initial maze
    testing = Label()
    begin = start(rows, cols, wall)
    initial = Label(root, text="Initial Maze:").grid(pady=2, column=0)#columnspan=2)
    for row in begin:
        Label(text=" ".join(map(str,row)), borderwidth=1).grid(pady=2, column=0)#columnspan=2)

    # Display A* maze
    final = finish(rows, cols, begin)
    if final == "None":
        short_path = Label(root, text="No valid path found.").grid(row=4, column=1)#columnspan=2)
    else:
        short_path = Label(root, text="Shortest Path:").grid(pady=2, row=4, column=1)#columnspan=2)
        for row in final:
            Label(text=" ".join(map(str,row)), borderwidth=1).grid(pady=2, row=r, column=1)#columnspan=2)
            r += 1
    # for label in root.grid_slaves():
    #     Label(text="" + str(label.grid_info()), borderwidth=1).grid(columnspan=2)

# Delete maze variables and the maze
def clear():
    num_of_rows.delete(0, END)
    num_of_cols.delete(0, END)
    wall_prob.delete(0, END)
    for label in root.grid_slaves():
        if int(label.grid_info()["row"]) > 3:
            label.grid_forget()

# Create text boxes
num_of_rows = Entry(root, width=20)
num_of_rows.grid(row=0, column=1, padx=20)
num_of_cols = Entry(root, width=20)
num_of_cols.grid(row=1, column=1, padx=20)
wall_prob = Entry(root, width=20)
wall_prob.grid(row=2, column=1, padx=20)

# Create text box labels
rows_label = Label(root, text="Number of Rows:")
rows_label.grid(row=0, column=0, padx=20, pady=5)
cols_label = Label(root, text="Number of Columns:")
cols_label.grid(row=1, column=0, padx=20)
wall_label = Label(root, text="Wall probability (Range: 0-1):")
wall_label.grid(row=2, column=0, padx=20, pady=5)

# Create buttons for creating the maze and clearing everything
pass_arguments = Button(root, text="Enter", command=enter, width=10, padx=5, pady=1)
pass_arguments.grid(row=3, column=0, pady=10)

clear_arguments = Button(root, text="Clear", command=clear, width=10, padx=5, pady=1)
clear_arguments.grid(row=3, column=1)

# Allow keyboard enter key to create maze
root.bind('<Return>',lambda event:enter())

# Center the application window
root.eval('tk::PlaceWindow . center')

root.mainloop()