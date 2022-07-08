from tkinter import Frame, Tk
from components.menu_bar import MenuBar

class MyApp(Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Mi aplicacion")
        self.geometry('600x600')
        
        menu = MenuBar(self)
        self['menu'] = menu
        
        main_frame = Frame(self, bg="#84CEEB", height=600, width=1024)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        
        
       


