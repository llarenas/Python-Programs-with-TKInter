'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

from tkinter import *

def donot():
    print('ok ah!!!!!!!!!!!!')

root =Tk()

#******* Main Menu*******#
menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label='file', menu=submenu)
submenu.add_command(label="new proj.", command=donot)
submenu.add_command(label="neeew!.", command=donot)
submenu.add_separator()
submenu.add_command(label='exit', command=donot)

editmenu = Menu(menu)
menu.add_cascade(label='edit', menu=editmenu)
editmenu.add_command(label="redo.", command=donot)
editmenu.add_command(label="comment.", command=donot)

#******* Toolbar*******#
toolbar = Frame(root, bg='blue')
insertbutt = Button(toolbar, text='insert pic', command=donot)
insertbutt.pack(side=LEFT, padx=2, pady=2)
printbutt = Button(toolbar, text='print', command=donot)
printbutt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)



#******* Status Bar*******#
status = Label(root, text="preparing....", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)



#####
root.mainloop()



