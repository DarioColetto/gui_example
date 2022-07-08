from tkinter import Menu
from components.pages import *

class MenuBar(Menu):
    def __init__(self, parent):
        super().__init__(parent)

        menu_file = Menu(self, tearoff=0)
        self.add_cascade(label="Menu1", menu= menu_file)
        menu_file.add_command(label="All Widgets", )# command=lambda: parent.show_frame(Some_Widgets)
        menu_file.add_separator()
        menu_file.add_command(label="Exit Application",)  #command=lambda: parent.destroy()

        menu_orders = Menu(self, tearoff=0)
        self.add_cascade(label="Menu2", menu=menu_orders)

        menu_pricing = Menu(self, tearoff=0)
        self.add_cascade(label="Menu3", menu=menu_pricing)
        menu_pricing.add_command(label="Page One", ) #command=lambda: parent.show_frame(PageOne)

        menu_operations = Menu(self, tearoff=0)
        self.add_cascade(label="Menu4", menu=menu_operations)
        menu_operations.add_command(label="Page Two", ) #command=lambda: parent.show_frame(PageTwo)
        menu_positions = Menu(menu_operations, tearoff=0)
        menu_operations.add_cascade(label="Menu5", menu=menu_positions)
        menu_positions.add_command(label="Page Three", ) #command=lambda: parent.show_frame(PageThree)
        menu_positions.add_command(label="Page Four", ) #command=lambda: parent.show_frame(PageFour)

        menu_help = Menu(self, tearoff=0)
        self.add_cascade(label="Menu6", menu=menu_help)
        menu_help.add_command(label="Open New Window", ) #command=lambda: parent.OpenNewWindow()



    #     self.frames = {}
    #     pages = (Some_Widgets, PageOne, PageTwo, PageThree, PageFour) # Impor pages..
    #     for F in pages:
    #         frame = F(main_frame, self)
    #         self.frames[F] = frame
    #         frame.grid(row=0, column=0, sticky="nsew")
    #     self.show_frame(Some_Widgets)
        
    #     menubar = MenuBar(self)
    #     self.config(self, menu=menubar)

    # def show_frame(self, name):
    #     frame = self.frames[name]
    #     frame.tkraise()

    # def OpenNewWindow(self):
    #     OpenNewWindow()
