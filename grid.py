'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

from tkinter import *

root = Tk()
####

labelname = Label(root, text='name')
labelpass = Label(root, text='password')
entryname = Entry(root)
entrypass = Entry(root)
####
labelname.grid(row=0)
labelpass.grid(row=1)

entryname.grid(row=0, column=1)
entrypass.grid(row=1, column=1)

####
root.mainloop()
