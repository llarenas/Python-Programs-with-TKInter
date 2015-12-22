'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

from tkinter import *

root = Tk() #create blank window
################################

topframe= Frame(root) #create root
topframe.pack() #display
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

button1 = Button(topframe, text="click me!", fg="red")
button2 = Button(topframe, text="click boy!", fg="green")
button3 = Button(topframe, text="click bebe!", fg="pink") ###
button4 = Button(bottomframe, text="click me!", fg="maroon")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)



################################
root.mainloop() #display tuloy2
