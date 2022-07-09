from pathlib import Path
import shelve 

path = Path(__file__).parent
print("database works") 


def data_base():
    database = shelve.open("database/mydatabase")  
    return database



        
if __name__ == "__main__":
    
    with shelve.open("database/credentials") as credentials:
        credentials['username'] = 'pepe'
        credentials['password'] = 'pepe1234'

        print(credentials['username'] ,credentials['password'])

    
    # with shelve.open("database/mydatabase") as database:
    #     for k , v in database.items():
    #         print(k , v)

   














