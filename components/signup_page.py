from tkinter import Frame, Label, Tk, messagebox, ttk
import sys
import os
        

sys.path.append(os.getcwd())
from components.styles import text_styles
from servicies.signup_service import validation 

class SignupPage(Tk):

    def __init__(self):

        super().__init__()

        self.geometry("600x600")
        self.resizable(0, 0)
        self.title("Registration")
        

        main_frame =Frame(self, bg="#3F6BAA", height=150, width=250)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")


        label_user =Label(main_frame, text_styles, text="New Username:")
        label_user.grid(row=1, column=0)
        

        label_pw =Label(main_frame, text_styles, text="New Password:")
        label_pw.grid(row=2, column=0)

        entry_user = ttk.Entry(main_frame, width=20, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(main_frame, width=20, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        button = ttk.Button(main_frame, text="Create Account", command=lambda: signup())
        button.grid(row=4, column=1)

        def signup():
           
            user = entry_user.get()
            password  = entry_pw.validate()
            
            resp = validation(user, password)
            messagebox.showerror("Information", "That Username already exists")
           
            # if  not validation(user):
                
            # else:
            #     if len(password) > 3:
            #         credentials = open("credentials.txt", "a")
            #         credentials.write(f"Username,{user},Password,{password},\n")
            #         credentials.close()
            #         messagebox.showinfo("Information", "Your account details have been stored.")
            #         SignupPage.destroy(self)

            #     else:
            #         messagebox.showerror("Information", "Your password needs to be longer than 3 values.")




if __name__ == '__main__':
    test = SignupPage()
    test.mainloop()
