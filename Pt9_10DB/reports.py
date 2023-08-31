from connect import *


def artist():  # option 1
    artistField = input("Enter the name of the Artist to search for:  ")
    dbCursor.execute(f"SELECT * FROM songs WHERE Artist = '{artistField}' ")# select all records from songs table
    records = dbCursor.fetchall()# fetches all records selected from the songs table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)


def title(): # option 2
    titleField = input("Enter the name of the song Title to search for:  ")
    dbCursor.execute(f"SELECT * FROM songs WHERE Title = '{titleField}' ")# select all records from songs table
    records = dbCursor.fetchall()# fetches all records selected from the songs table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)



def genre(): # option 3
    genreField = input("Enter the name of the song Genre to search for:  ")
    dbCursor.execute(f"SELECT * FROM songs WHERE Genre = '{genreField}' ")# select all records from songs table
    records = dbCursor.fetchall()# fetches all records selected from the songs table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)


def songID(): # option 4
    idField = input("Enter the SongID of the record to search forbe deleted: ")
    dbCursor.execute(f"SELECT * FROM songs WHERE SongID = {idField} ")# select all records from songs table
    records = dbCursor.fetchall()# fetches all records selected from the songs table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)



# fieldName = input("Enter Field Name: ")

def readOrder(): # option 5
    # dbCursor.execute(f"SELECT * FROM songs ORDER BY {fieldName} DESC")
    # dbCursor.execute(f"SELECT * FROM songs ORDER BY SongID DESC")
    # dbCursor.execute(f"SELECT Artist, Genre FROM songs ORDER BY SongID DESC")
    # dbCursor.execute(f"SELECT Artist, Genre FROM songs ORDER BY Artist ASC")
    dbCursor.execute(f"SELECT * FROM songs WHERE Genre = 'Soul' or Genre = 'Rap' ")
    # dbCursor.execute(f"SELECT * FROM songs WHERE Title Like 't%' ")
    # dbCursor.execute(f"SELECT * FROM songs WHERE Title Like '%t%' ")
    # dbCursor.execute(f"SELECT * FROM songs WHERE Title NOT Like 't%' ")
       
    #  https://www.w3schools.com/mysql/mysql_like.asp

    records = dbCursor.fetchall()# fetches all records selected from the songs table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)


# option 6 = Exit
if __name__=="__main__":
    # artist()
    # title()
    # genre()
    # songID()
    readOrder()
  