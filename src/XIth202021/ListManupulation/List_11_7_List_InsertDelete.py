'''
Created on Feb 23, 2021

@author: admin
'''

lst = [1, 2, 3, 4, 5]
print("Existing list it  - ", lst)

while True : 
    print("Main Menu")
    print("1. Insert")
    print("2. Delete")
    print("3. Exit")
    ch = int(input("Enter your choice 1/2/3 - "))
    
    if ch == 1 :
        val = int(input("Enter value to be entered - "))
        pos = int(input("Enter position - "))
        index = pos - 1
        lst.insert(index, val)
        print("{} is inserted at position {} and at index {}".
              format(val, pos, index))
        print("New list is {}".format(lst))
        print("-"*20)
        
    elif ch == 2:
        print("=========")
        print("Delete Menu")
        print("1. Delete using Value")
        print("2. Delete using index")
        print("3. Delete a sublist")
        dch = int(input("Enter your choice 1/2/3 - "))
        if dch == 1:
            dval = int(input("Enter value to be deleted - "))
            lst.remove(dval)
            print("New list is {}".format(lst))
            print("-"*20)    
            
            
    elif ch == 3 :
        print("Choice 3")
        break
    else :
        print("Invalid choice")
    
