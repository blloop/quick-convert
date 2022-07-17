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
def reset():
    for widget in win.winfo_children():
        widget.destroy()

# Test method for clicking
def clicked():
    showinfo(title = 'Alert!', message = 'Button Clicked!')

# Create landing page
def makeLanding():

    # Clear window
    reset()
    
    # Create landing page header
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
        command = makeTemp, bg = "white", activebackground = "gray"
    )
    dist = tk.Button(
        win, image = dist_icon, text = 'DISTANCE',
        compound = tk.LEFT, font = ("Verdana", 14),
        command = makeDist, bg = "white", activebackground = "gray"
    )
    mass = tk.Button(
        win, image = mass_icon, text = 'MASS',
        compound = tk.LEFT, font = ("Verdana", 14),
        command = makeMass, bg = "white", activebackground = "gray"
    )
    time = tk.Button(
        win, image = time_icon, text = 'TIME',
        compound = tk.LEFT, font = ("Verdana", 14),
        command = makeTime, bg = "white", activebackground = "gray"
    )
    temp.place(height = 180, width = 300, x = 0, y = 40)
    dist.place(height = 180, width = 300, x = 300, y = 40)
    mass.place(height = 180, width = 300, x = 0, y = 220)
    time.place(height = 180, width = 300, x = 300, y = 220)
    
# Create conversion page
def makeConvert():

    # Clear window
    reset()
    
    # Create conversion page header
    title = tk.Label(
        win, text = 'Choose conversion units: ',
        font = ("Verdana", 14), bg = "#99CEFF"
    )
    leave = tk.Button(
        win, text = 'Return to menu',command=makeLanding,
        font = ("Verdana", 14), bg = "#FF9999"
    )
    title.place(height = 40, width = 400, x = 0, y = 0)
    leave.place(height = 40, width = 200, x = 400, y = 0)

def makeTemp():

    # Render convertion page
    makeConvert()

    # Add temperature conversion elements
    temp = tk.Button(
        win, text = 'TEMPERATURE',
        compound = tk.LEFT, font = ("Verdana", 14),
        command = clicked, bg = "white", activebackground = "gray"
    )
    temp.place(height = 180, width = 300, x = 0, y = 40)

def makeDist():

    # Render convertion page
    makeConvert()

    # Add temperature conversion elements
    dist = tk.Button(
        win, image = dist_icon, text = 'DISTANCE',
        compound = tk.LEFT, font = ("Verdana", 14),
        command = clicked, bg = "white", activebackground = "gray"
    )
    dist.place(height = 180, width = 300, x = 0, y = 40)

def makeMass():

    # Render convertion page
    makeConvert()

    # Add temperature conversion elements
    mass = tk.Button(
        win, image = mass_icon, text = 'MASS',
        compound = tk.LEFT, font = ("Verdana", 14),
        command = clicked, bg = "white", activebackground = "gray"
    )
    mass.place(height = 180, width = 300, x = 0, y = 40)

def makeTime():

    # Render convertion page
    makeConvert()

    # Add temperature conversion elements
    time = tk.Button(
        win, image = time_icon, text = 'TIME',
        compound = tk.LEFT, font = ("Verdana", 14),
        command = clicked, bg = "white", activebackground = "gray"
    )
    time.place(height = 180, width = 300, x = 0, y = 40)   

makeLanding()
win.mainloop()
