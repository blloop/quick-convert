import tkinter as tk
from tkinter.messagebox import showinfo

# Import images
temp_icon = tk.PhotoImage(file = './img/temperature.png')
dist_icon = tk.PhotoImage(file = './img/distance.png')
mass_icon = tk.PhotoImage(file = './img/mass.png')
time_icon = tk.PhotoImage(file = './img/time.png')

# Create root window
win = tk.Tk()
win.resizable(False, False)
win.geometry('600x400+200+100')
win.title('Image Button Demo')

# Clear widgets from window
def reset(win):
    for widget in win.winfo_children():
        widget.destroy()
    makeHeader(win)

# Create frame header
def makeHeader(win):    
    title = tk.Label(win, text = 'Select a measurement converter: ')
    title.place(x = 0, y = 0)
    leave = tk.Button(win, text = 'Quit', command=win.destroy)
    leave.place(x = 550, y = 0)

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
    temp.pack(ipadx=50,ipady=5,expand=True)
    dist.pack(ipadx=50,ipady=5,expand=True)
    mass.pack(ipadx=50,ipady=5,expand=True)
    time.pack(ipadx=50,ipady=5,expand=True)

makeHeader(win)
makeLanding(win)
win.mainloop()
