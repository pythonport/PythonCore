#import result
import entry
import os

# MAIN FUNCTION TO ENTER INSIDE APPLICATION
def mainfunc() :
    print()
    print()
    print()
    print()
    print("\t\t"+"*"*30)
    print("\t\t\t MAIN MENU")
    print("\t\t"+"*"*30)
    print()
    print("\t\t\t <1> RESULT MENU")
    print()
    print("\t\t\t <2> ENTRY/EDIT MENU")
    print()
    print("\t\t\t <3> EXIT")
    print("\t\t"+"*"*30)
    print()
    ch = input(" Please select your option(1-3) : ")
    if ch =="1" :
        os.system('cls')
        result.result_main()
    elif ch =="2" :
        os.system('cls')
        entry.entry_main()
    else :
        exit()
