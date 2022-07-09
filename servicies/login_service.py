import shelve
import sys
import os


sys.path.append(os.getcwd())

from database.database import path


print("login_service working")

def validation(username, password):
    
    try:
        with shelve.open(f'{path}/credentials', 'r' )  as credentials:
                if credentials['username'] == username and credentials['password'] == password:
                    
                    return True
  

    except KeyError:
        print ("User and Password shoul be created")