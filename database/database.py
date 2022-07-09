import shelve

database = shelve.open("database/mydatabase") 



for k , v in database.items():
    print(k , v)




















