import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo

# Create root window
win = tk.Tk()
win.resizable(False, False)
win.geometry('600x400+200+100')
win.title('Quick Convert')

# Import images
temp_icon = tk.PhotoImage(file = './img/temperature.png')
dist_icon = tk.PhotoImage(file = './img/distance.png')
mass_icon = tk.PhotoImage(file = './img/mass.png')
time_icon = tk.PhotoImage(file = './img/time.png')

# Clear widgets from window
def reset(win):
    for widget in win.winfo_children():
        widget.destroy()

# Test method for clicking
def clicked():
    showinfo(title = 'Alert!', message = 'Button Clicked!')

# Create landing page
def makeLanding(win):
    
    # Create header
    title = tk.Label(
        win, text = 'Select a measurement converter: ',
        font = ("Verdana", 14), bg = "#99CEFF"
    )
    leave = tk.Button(
        win, text = 'Quit',command=win.destroy,
        font = ("Verdana", 14), bg = "#FF9999"
    )
    title.place(height = 40, width = 500, x = 0, y = 0)
    leave.place(height = 40, width = 100, x = 500, y = 0)

    # Create image buttons
    temp = tk.Button(
        win, image = temp_icon, text = 'TEMPERATURE',
        compound = tk.LEFT, font = ("Verdana", 14),
        command = clicked, bg = "white", activebackground = "black"
    )
    dist = tk.Button(
        win, image = dist_icon, text = 'DISTANCE',
        compound = tk.LEFT, font = ("Verdana", 14),
        command = clicked
    )
    mass = tk.Button(
        win, image = mass_icon, text = 'MASS',
        compound = tk.LEFT, font = ("Verdana", 14),
        command = clicked, bg = "white"
    )
    time = tk.Button(
        win, image = time_icon, text = 'TIME',
        compound = tk.LEFT, font = ("Verdana", 14),
        command = clicked, bg = "white"
    )
    temp.place(height = 180, width = 300, x = 0, y = 40)
    dist.place(height = 180, width = 300, x = 300, y = 40)
    mass.place(height = 180, width = 300, x = 0, y = 220)
    time.place(height = 180, width = 300, x = 300, y = 220)

makeLanding(win)
win.mainloop()
