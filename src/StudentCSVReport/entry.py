import os
import stuentry
import stumain
#STUDENT ENTRY MAN FUNCTION

def entry_main() :
    print()
    print()
    print()
    print()
    print("\t\t"+"*"*30)
    print("\t\t\t ENTRY MENU")
    print("\t\t"+"*"*30)
    print()
    print("\t\t\t <1> CREATE STUDENT RECORD")
    print()
    print("\t\t\t <2> DISPLAY ALL STUDENTS RECORD")
    print()
    print("\t\t\t <3> SEARCH STUDENT RECORD")
    print()
    print("\t\t\t <4> BACK TO MAIN MENU")
    print("\t\t"+"*"*30)
    print()
    ch =input(" Please select your option(1-6) : ")
    if ch=="1" :
        os.system('cls')
        stuentry.create()
    elif ch=="2" :
        os.system('cls')
        stuentry.showData()
    elif ch=="3" :
        os.system('cls')
        stuentry.search()
    elif ch=="4" :
        os.system('cls')
        stumain.mainfunc()
    else :
        os.system('cls')
        print("Invalid input")
