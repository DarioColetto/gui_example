import imp
import shelve
import sys
import os

sys.path.append(os.getcwd())

from database.database import data_base
     

class Respository:
    
    
    def __init__(self):
        pass
 
    def get_all(self):
        
        with data_base() as db:
            rows = {k: v for (k,v) in db.items()}
            return rows

    def get_by_name(self, name):
        
        with data_base() as db:
            return db[name]


    def add_element(self, name, type, BaseState):

        with data_base() as db:
            db[name] = {'type' : type, 'BaseState' : BaseState }
            print( name , " fue agreggado")
    
    def delete_by_name(self, name):

        with data_base() as db:
            db.pop(name)
            print( name , " fue eliminado")


if __name__ == "__main__":
    
    import time
    
    print(Respository().get_by_name('Mewtwo'))
    time.sleep(2)
    
    Respository().delete_by_name('Mewtwo')
    time.sleep(2)
    
    Respository().add_element('Mewtwo','Psychic', '680' )
    time.sleep(2)
    
    print(Respository().get_by_name('Mewtwo'))
    time.sleep(2)
    
    print(Respository().get_all())
    

