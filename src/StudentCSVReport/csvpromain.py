import os
import stumain
# MAIN FUNCTION TO ENTER INSIDE APPLICATION
def mfunc() :
    print()
    print()
    print()
    print()
    print("\t\t"+"*"*50)
    print("\t\t PROJECT")
    print("\t\t ON")
    print("\t\t STUDENT REPORT CARD")
    print("\t\t JAWAHAR NAVODAYA VIDYALAYA, DHANBAD")
    print("\t\t"+"*"*50)
    print()
    print("\t\t REPORT SUBMITTED BY :")
    print("\t\t\t\t\t BINAY KUMAR")
    print("\t\t\t\t\t HARSH KUMAR BARNWAL")
    print("\t\t\t\t\t KUMKUM KUMARI")
    print("\t\t\t\t\t NIHARIKA SINHA")
    print("\t\t\t\t\t PREM KUMAR MAHATO")
    print("\t\t\t\t\t PRINCE KUMAR")
    print("\t\t\t\t\t PUNAM KUMARI")
    print("\t\t\t\t\t VISHAL KUMAR")
    print()    
    print("\t\t GUIDED BY : Mr. RAJESH KUMAR JHA, PGT(CS)")
    print()
    print("\t\t"+"*"*50)
    chr = input("PRESS 'G' TO CONTINUE : ")
    if chr =="g" or chr =="G" :
        os.system('cls')
        stumain.mainfunc()
    
#Calling main function
if __name__=='__main__':
    mfunc()
