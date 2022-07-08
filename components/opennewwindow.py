from tkinter import Frame, Label, Tk, ttk

class OpenNewWindow(Tk):

    def __init__(self, *args, **kwargs):

        super().__init__(self, *args, **kwargs)

        main_frame = Frame(self)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.title("Here is the Title of the Window")
        self.geometry("500x500")
        self.resizable(0, 0)

        frame1 = ttk.LabelFrame(main_frame, text="This is a ttk LabelFrame")
        frame1.pack(expand=True, fill="both")

        label1 = Label(frame1, font=("Verdana", 20), text="OpenNewWindow Page")
        label1.pack(side="top")