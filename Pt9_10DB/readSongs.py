from connect import * # import the connect.py module 



#subroutine/function

def read():
    dbCursor.execute("SELECT * FROM songs")# select all records from songs table
    records = dbCursor.fetchall()# fetches all records selected from the songs table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)
if __name__=="__main__":
    read()


