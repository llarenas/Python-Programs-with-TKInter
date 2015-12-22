'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

from tkinter import *

root = Tk() #create blank window ... tk() class sa tkinter
################################

photo = PhotoImage(file="174.jpg")

label = Label(root, image=photo)

label.pack()



################################
root.mainloop() #display tuloy2
