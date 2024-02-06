import os
#import stuentry
import studentmain

def result_main() :
    print("\t\t"+"*"*30)
    print("\t\t\t RESULT MENU")
    print("\t\t"+"*"*30)
    print()
    print("\t\t\t <1> Class Result")
    print()
    print("\t\t\t <2> Student Report Card")
    print()
    print("\t\t\t <3> Back to Main Menu")
    print("\t\t"+"*"*30)
    print()
    ch = input(" Please select your option(1-3) : ")
    if ch=="1" :
        os.system('cls')
        stuentry.display()
    elif ch=="2" :
        os.system('cls')
        stuentry.search()
    if ch =="3" :
        os.system('cls')
        studentmain.mainfunc()
