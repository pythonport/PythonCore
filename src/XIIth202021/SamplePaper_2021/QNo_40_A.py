'''
Created on Jan 6, 2021
A binary file Book.dat has structure [BookNo, Book_Name, Author, Price].
[i] Write a user defined function CreateFile() to input data for a 
record and add to Book.dat .
[ii] Write a function CountRec(Author) in Python which accepts the 
Author name as parameter and count and return number of books by 
the given Author are stored in the binary file Book.dat
@author: admin
'''
import pickle


def CreateFile():
    fout = open('Book.dat', 'ab')
    BookNo = input("Enter book number - ")
    Book_Name = input("Enter Book_Name - ")
    Author = input("Enter book Author - ")
    Price = input("Enter book Price - ")
    bookList = [BookNo, Book_Name, Author, Price]
    pickle.dump(bookList, fout)
    fout.close()
    print("Book stored")

    
def CountRec():
    fout = open('Book.dat', 'rb')
    Author = input("Enter book Author - ")
    countBook = 0
    try :
        while True :
            bookList = pickle.load(fout)
            if Author == bookList[2] :
                countBook += 1
                print(bookList)
    except:
        fout.close()
    print("Total book written by ", Author, ' is - ', countBook)    
    print("Total book written by  %s is %d "%(Author,countBook))    


def GetAllBook():
    fout = open('Book.dat', 'rb')
    try :
        while True :
            bookList = pickle.load(fout)
            print(bookList)
    except:
        fout.close()


#CreateFile()
CountRec()
#GetAllBook()
