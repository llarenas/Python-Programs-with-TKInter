'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

from tkinter import *

root= Tk()
#####

def leftClick(event):
    print('left!!!')

def midClick(event):
    print('middle fingah!!!')

def rightClick(event):
    print('Right!!!')


frame = Frame(root, width=300, height='250')
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", midClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

#####
root.mainloop()
