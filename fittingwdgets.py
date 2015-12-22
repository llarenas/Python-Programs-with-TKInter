'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

from tkinter import *

root = Tk()
###########

one = Label(root, text='one', bg='red', fg='green')
one.pack()

two = Label(root, text='duwa', bg='black', fg='white')
two.pack(fill=X)

three = Label(root, text='three', bg='blue', fg='gold')
three.pack(side=LEFT, fill=Y)

four = Label(root, text='4', bg='yellow', fg='purple')
four.pack(side=RIGHT, fill=Y)

##########
root.mainloop()
