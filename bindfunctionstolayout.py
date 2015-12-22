'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

from tkinter import *

root = Tk()
####
def printname(event):
    print('name ko is nel!')
    label1=Label(root, text='itot?')
    label1.grid(row=5, column=5)

button1=Button(root, text='print name') #, command=printname
button1.bind('<Button-1>', printname)
button1.pack()


####
root.mainloop()
