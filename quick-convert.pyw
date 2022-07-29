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
        command = makeTemp, bg = "white", activebackground = "#BFBFBF"
    )
    dist = tk.Button(
        win, image = dist_icon, text = 'DISTANCE',
        compound = tk.LEFT, font = ("Verdana", 14),
        command = makeDist, bg = "white", activebackground = "#BFBFBF"
    )
    mass = tk.Button(
        win, image = mass_icon, text = 'MASS',
        compound = tk.LEFT, font = ("Verdana", 14),
        command = makeMass, bg = "white", activebackground = "#BFBFBF"
    )
    time = tk.Button(
        win, image = time_icon, text = 'TIME',
        compound = tk.LEFT, font = ("Verdana", 14),
        command = makeTime, bg = "white", activebackground = "#BFBFBF"
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
    back = tk.Button(
        win, text = 'Back', command = makeLanding,
        font = ("Verdana", 14), bg = "#A3C2C2"
    )
    title = tk.Label(
        win, text = 'Choose conversion units: ',
        font = ("Verdana", 14), bg = "#99CEFF"
    )
    leave = tk.Button(
        win, text = 'Quit',command=win.destroy,
        font = ("Verdana", 14), bg = "#FF9999"
    )
    back.place(height = 40, width = 100, x = 0, y = 0)
    title.place(height = 40, width = 400, x = 100, y = 0)
    leave.place(height = 40, width = 100, x = 500, y = 0)

# Conversion utilities
units1 = StringVar()
units2 = StringVar()
tempUnits = ["Fahrenheit", "Celsius", "Kelvin"]
distUnits = ["Inches", "Feet", "Yards", "Miles", "Millimeters", "Centimeters", "Meters", "Kilometers"]
massUnits = ["Ounces", "Pounds", "Tons", "Grams", "Kilograms"]
timeUnits = ["Seconds", "Minutes", "Hours", "Days"]

def getUnits():
    if (units1.get() == units2.get()):
        print("Invalid Units!")
    else:
        print("Input:" + units1.get())
        print("Output:" + units2.get())
def placeWidgets(widget1, widget2, widget3):    
    widget1.place(height = 40, width = 100, x = 40, y = 80)
    widget2.place(height = 40, width = 100, x = 150, y = 80)
    widget3.place(height = 40, width = 100, x = 260, y = 80)
    

# Create temperature conversion page
def makeTemp():

    # Render conversion page
    makeConvert()
  
    # Set default units to show
    units1.set("Fahrenheit")
    units2.set("Celsius")
      
    # Dropdown Menus
    dropdown1 = tk.OptionMenu(
        win, units1, *tempUnits
    )
    dropdown2 = tk.OptionMenu(
        win, units2, *tempUnits
    )
    button = tk.Button(
        win, text = "Check Units", command = getUnits
    )
    placeWidgets(dropdown1, dropdown2, button)

    ###

    frm_entry = tk.Frame(win)
    ent_temperature = tk.Entry(win)
    btn_convert = tk.Button(
        win, text="\N{RIGHTWARDS BLACK ARROW}",
        command=fahrenheit_to_celsius
    )
    lbl_temp = tk.Label(
        win, text="\N{DEGREE FAHRENHEIT}"
    )
    lbl_result = tk.Label(
        win, text="\N{DEGREE CELSIUS}"
    )

    # Place elements in app using .place
    frm_entry.place(height = 20, width = 100, x = 100, y = 100)
    ent_temperature.place(height = 20, width = 20, x = 0, y = 40)
    lbl_temp.place(height = 20, width = 20, x = 20, y = 40)
    btn_convert.place(height = 40, width = 50, x = 200, y = 80)
    lbl_result.place(height = 20, width = 100, x = 250, y = 100)

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    
    ###

def makeDist():

    # Render conversion page
    makeConvert()

    # Set default units to show
    units1.set("Yards")
    units2.set("Meters")
      
    # Dropdown Menus
    dropdown1 = tk.OptionMenu(
        win, units1, *distUnits
    )
    dropdown2 = tk.OptionMenu(
        win, units2, *distUnits
    )
    button = tk.Button(
        win, text = "Check Units", command = getUnits
    )
    placeWidgets(dropdown1, dropdown2, button)

def makeMass():

    # Render conversion page
    makeConvert()

    # Set default units to show
    units1.set("Pounds")
    units2.set("Kilograms")
      
    # Dropdown Menus
    dropdown1 = tk.OptionMenu(
        win, units1, *massUnits
    )
    dropdown2 = tk.OptionMenu(
        win, units2, *massUnits
    )
    button = tk.Button(
        win, text = "Check Units", command = getUnits
    )
    placeWidgets(dropdown1, dropdown2, button)

def makeTime():

    # Render conversion page
    makeConvert()

    # Set default units to show
    units1.set("Hours")
    units2.set("Minutes")
      
    # Dropdown Menus
    dropdown1 = tk.OptionMenu(
        win, units1, *timeUnits
    )
    dropdown2 = tk.OptionMenu(
        win, units2, *timeUnits
    )
    button = tk.Button(
        win, text = "Check Units", command = getUnits
    )
    placeWidgets(dropdown1, dropdown2, button) 

makeLanding()
win.mainloop()

