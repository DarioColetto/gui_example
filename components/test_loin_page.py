if __name__ == "__main__":

    try:
        from login_page import *
    
    except ModuleNotFoundError:
        
        import sys
        import os
        

        sys.path.append(os.getcwd())

        from login_page import *

    login_page_test = LoginPage()
    login_page_test.mainloop()

    print(sys.path)

