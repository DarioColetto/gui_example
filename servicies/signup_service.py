import shelve
import sys
import os

sys.path.append(os.getcwd())

from database.database import path



def validation(username, password):

    """Checks username/password combination"""

    try:
        with shelve.open(f'{path}/credentials' )  as credentials:
                if credentials['username'] == username:
                    
                    return "User already exist"

                elif len(credentials['password']) >= 4:

                    return "Your passwor should be at least 4 charactes"

                else:
                    credentials['username'] = username
                    credentials['password'] = password    

    except KeyError:
        print ("User and Password shoul be created")




if __name__ == "__main__":
    pass
    