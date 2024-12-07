'''
Created on Oct 12, 2024

@author: admin
'''
def push_book(BooksStack, new_book):
    BooksStack.append(new_book)

def pop_book(BooksStack) :
    if (BooksStack ==[] ) :
        return "Underflow"
    else :
        item = BooksStack.pop()
        return item

def peep(BooksStack):
    if (BooksStack ==[] ) :
        return "None"
    else :
        top = len(BooksStack)-1
        item = BooksStack[top]
        return item