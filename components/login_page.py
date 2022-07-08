from tkinter import Frame, Label, Tk, messagebox, ttk
from servicies.routing_service import Routing
from servicies.login_service import validate

class LoginPage(Tk):

    def __init__(self, *args, **kwargs):

        super().__init__(self, *args, **kwargs)


        self.geometry("626x431")  
        self.resizable(0, 0)  
        
        main_frame = Frame(self, bg="#708090", height=431, width=626)
        main_frame.pack(fill="both", expand="true")
        
        
        #syles aparte
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "blue"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "blue",
                       "foreground": "#E1FFFF"}

        frame_login = Frame(main_frame, bg="blue", relief="groove", bd=2)
        frame_login.place(rely=0.30, relx=0.17, height=130, width=400)

        label_title = Label(frame_login, title_styles, text="Login Page")
        label_title.grid(row=0, column=1, columnspan=1)

        label_user = Label(frame_login, text_styles, text="Username:")
        label_user.grid(row=1, column=0)

        label_pw = Label(frame_login, text_styles, text="Password:")
        label_pw.grid(row=2, column=0)

        entry_user = ttk.Entry(frame_login, width=45, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(frame_login, width=45, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        button = ttk.Button(frame_login, text="Login", command=lambda: getlogin())
        button.place(rely=0.70, relx=0.50)

        signup_btn = ttk.Button(frame_login, text="Register", command=lambda: Routing.to_signup_page(...))
        signup_btn.place(rely=0.70, relx=0.75)


        
        def getlogin():
            username = entry_user.get()
            password = entry_pw.get()
            
            validation = validate(username, password)
            
            if validation:
                messagebox.showinfo("Login Successful",
                                       "Welcome {}".format(username))
                root.deiconify()
                top.destroy()
            else:
                messagebox.showerror("Information", "The Username or Password you have entered are incorrect ")

