import sys
import os
        

sys.path.append(os.getcwd())
from tkinter import Frame, Label, Tk, messagebox, ttk
from servicies.routing_service import Routing

from servicies.login_service import validation
from components.styles import title_styles, text_styles



class LoginPage(Tk):

    def __init__(self):

        super().__init__()

        self.geometry("626x431")  
        self.resizable(0, 0) 
        self.title("Login") 
        
        main_frame = Frame(self, bg="#708090", height=431, width=626)
        main_frame.pack(fill="both", expand="true")
        
        frame_login = Frame(main_frame, bg="blue", relief="groove", bd=2)
        frame_login.place(rely=0.30, relx=0.17, height=130, width=400)

        label_title = Label(frame_login, title_styles, text="Login Page")
        label_title.grid(row=0, column=1, columnspan=1)

        label_user = Label(frame_login, text_styles, text="Username:")
        label_user.grid(row=1, column=0)

        label_pw = Label(frame_login, text_styles, text="Password:")
        label_pw.grid(row=2, column=0)

        self.entry_user = ttk.Entry(frame_login, width=45, cursor="xterm")
        self.entry_user.grid(row=1, column=1)

        self.entry_pw = ttk.Entry(frame_login, width=45, cursor="xterm", show="*")
        self.entry_pw.grid(row=2, column=1)

        self.button = ttk.Button(frame_login, text="Login", command= self.getlogin)
        self.button.place(rely=0.70, relx=0.50)

        signup_btn = ttk.Button(frame_login, text="Register", command=lambda: Routing.to_signup_page(...))
        signup_btn.place(rely=0.70, relx=0.75)


        
    def getlogin(self):
            
        username = self.entry_user.get()
        password = self.entry_pw.get()
            
            
        if validation(username, password):
            messagebox.showinfo('Login Successful',  f'Welcome {username}')
                
            self.destroy()
        else:
            messagebox.showerror("Information", "The Username or Password you have entered are incorrect ")



if __name__ == '__main__':
    test = LoginPage()
    test.mainloop() 