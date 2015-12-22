'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

from tkinter import *
import tkinter.messagebox

root =Tk()
#####

#messagebox nga para sa may choices.
answer=tkinter.messagebox.askquestion('q 1', 'do yu want to download it anyway?')

if answer == 'yes':
    #print(" 8==D~ ")
    l=Label(root, text="8==D~ ")
    l.pack()
    #para sa messagebox nga for notification lang.
    ans=tkinter.messagebox.showinfo('messagebx title!!!', 'Download Complete')
else:
    #print(" Download Canceled ")
    m=Label(root, text="Download Canceled  ")
    m.pack()
     

    



#####
root.mainloop()
