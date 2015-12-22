'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''
#this file is for the usingklasses.py


from tkinter import *
class ronelbuttons:

    def __init__(self, master):
        frame= Frame(master) #root is now master
        frame.pack()

        self.printbutton =Button(frame, text='print message', command=self.printMessage)
        self.printbutton.pack(side=LEFT)

        self.quitButton=Button(frame, text='quit', command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print('wow its work!')
