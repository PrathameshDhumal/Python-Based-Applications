##############################################################
#
#Author:Prathamesh Dhumal
#Date:2/8/21
#About:Creating a digital computer clock
#
##############################################################
# Importing Modules
from tkinter import *
from time import strftime

root = Tk()  
root.title("Digital Computer Clock by Prathamesh Dhumal")  

# Function used to display time on the label
def time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text = string)
    lbl.after(1000, time)

# Styling the label widget which displays the clock
lbl = Label(root, font = ("arial", 160, "bold"),bg="black",fg="cyan")

# Pack method in tkinter packs widgets into rows or columns. Positions label
lbl.pack(anchor = "center",fill = "both",expand=1)

time()  # Time function is called

mainloop()   # Runs the application program