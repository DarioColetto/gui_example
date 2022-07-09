import shelve

print("database works") 


def data_base():
    database = shelve.open("database/mydatabase")  
    return database


        
if __name__ == "__main__":
    

    
    with shelve.open("database/mydatabase") as database:
        for k , v in database.items():
            print(k , v)




















