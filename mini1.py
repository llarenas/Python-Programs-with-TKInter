'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

# this file extension and needed for minisystemko.py


from tkinter import *
import tkinter.messagebox
import random
import urllib.request

class Ronel:

    def __init__(self, master):
     
        
        #******* Main Menu*******#
        menu = Menu(master)
        master.config(menu=menu)

        submenu = Menu(menu)
        menu.add_cascade(label='File', menu=submenu)
        submenu.add_command(label="mouse", command=self.mouse)
        submenu.add_separator()
        submenu.add_command(label='exit', command=master.quit)

        editmenu = Menu(menu)
        menu.add_cascade(label='edit', menu=editmenu)
        editmenu.add_command(label="download photo.", command=self.dl)
        editmenu.add_command(label="comment.", command=self.donot)

        #******* Toolbar*******#
        toolbar = Frame(master, bg='blue')
        insertbutt = Button(toolbar, text='insert pic', command=self.donot)
        insertbutt.pack(side=LEFT, padx=2, pady=2)
        printbutt = Button(toolbar, text='print', command=self.donot)
        printbutt.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)



        #******* Status Bar*******#
        status = Label(master, text="preparing....", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

    def donot(self):
        print('ok ah!!!!!!!!!!!!')


    def mouse(self):

        root= Tk()
        #####

        def leftClick(event):
            tkinter.messagebox.showinfo('Left Click!!!', 'you left clicked it!')
            
            

        def midClick(event):
            status = Label(root, text="middle click!", bd=1, relief=SUNKEN, anchor=W)
            status.pack(side=BOTTOM, fill=X)

        def rightClick(event):
             tkinter.messagebox.showinfo('Right Click!!!', 'you right clicked it!')

            #may frame ang window. sa frame i test kung an ang gn click sa ilaga.
        frame = Frame(root, width=300, height='250')
        frame.bind("<Button-1>", leftClick)
        frame.bind("<Button-2>", midClick)
        frame.bind("<Button-3>", rightClick)
        frame.pack()

        #####
        root.mainloop()

    
    def dl(self):

        answer=tkinter.messagebox.askquestion('want to proceed?', 'do you want to download picture?')

        if answer == 'yes':
            root= Tk()
        #####

            def xxx(self):   
                def download_web_image(url):
                    print(" Downloading ")
                    name = random.randrange(1, 1000)
                    full_name = str(name) + ".jpg"
                    urllib.request.urlretrieve(url, full_name)


                download_web_image(entryname.get())

                

            label = Label(root, text='enter the url')
            entryname = Entry(root)
            button = Button(root, text='Download')
            button.bind("<Button-1>", xxx)
            label.pack()
            entryname.pack()
            button.pack()
            
        #####
            root.mainloop()

        else:
            print(" Download Canceled ")

        



