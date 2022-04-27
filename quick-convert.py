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
    makeHeader(win)

# Create frame header
def makeHeader(win):    
    title = tk.Label(win, text = 'Select a measurement converter: ')
    title.place(height = 30, x = 0, y = 0)
    leave = tk.Button(win, text = 'Quit', command=win.destroy)
    leave.place(height = 40, width = 100, x = 500, y = 0)

# Test method for clicking
def clicked():
    showinfo(title = 'Alert!', message = 'Button Clicked!')

# Create landing page
def makeLanding(win): 
    temp = tk.Button(
        win, image = temp_icon, text = 'TEMPERATURE',
        compound = tk.LEFT, command = clicked
    )
    dist = tk.Button(
        win, image = dist_icon, text = 'DISTANCE',
        compound = tk.LEFT, command = clicked
    )
    mass = tk.Button(
        win, image = mass_icon, text = 'MASS',
        compound = tk.LEFT, command = clicked
    )
    time = tk.Button(
        win, image = time_icon, text = 'TIME',
        compound = tk.LEFT, command = clicked
    )
    temp.place(height = 180, width = 300, x = 0, y = 40)
    dist.place(height = 180, width = 300, x = 300, y = 40)
    mass.place(height = 180, width = 300, x = 0, y = 220)
    time.place(height = 180, width = 300, x = 300, y = 220)

makeHeader(win)
makeLanding(win)
win.mainloop()
