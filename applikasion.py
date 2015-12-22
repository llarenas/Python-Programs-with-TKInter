'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

from tkinter import *

root = Tk()
root.title("First GUI!")
root.geometry("300x200")



class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.widgets()

def widgets(self):
    Label(self, text="Enter the text below...").grid(row=0,column=0,sticky=W)
    self.textBox = Entry(self)
    self.textBox.grid(row=1,column=0,sticky=W)
    Button(self, text="Output!", command=self.runText).grid(row=2,column=0,sticky=W)


def runText(self):
    print(self.textBox.get())


#app = Application(root)
root.mainloop()
