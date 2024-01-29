import os
import stuentry
import stutmain
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
    print("\t\t\t <4> MODIFY STUDENT RECORD")
    print()
    print("\t\t\t <5> DELETE STUDENT RECORD")
    print()
    print("\t\t\t <6> BACK TO MAIN MENU")
    print("\t\t"+"*"*30)
    print()
    ch =input(" Please select your option(1-6) : ")
    if ch=="1" :
        os.system('cls')
        stuentry.create()
    elif ch=="2" :
        os.system('cls')
        stuentry.display()
    elif ch=="3" :
        os.system('cls')
        stuentry.search()
    elif ch=="4" :
        os.system('cls')
        #stuentry.modify()
    elif ch=="5" :
        os.system('cls')
        #stuentry.delete()
    if ch =="6" :
        os.system('cls')
        stumain.mainfunc()
