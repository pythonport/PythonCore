'''
Created on Apr 24, 2019

@author: admin
'''
fin  = open("result.txt",'w')
strresult1 = "CS - 67, Che - 68, Phy - 90, Maths - 98, Eng -100\n"
strresult2 = "CS - 77, Che - 65, Phy - 20, Maths - 78, Eng -70\n"
strresult3 = "CS - 98, Che - 68, Phy - 95, Maths - 98, Eng -90\n"
strresult4 = "CS - 63, Che - 68, Phy - 80, Maths - 98, Eng -80\n"
strresult5 = "CS - 78, Che - 68, Phy - 50, Maths - 98, Eng -70"
fin.write(strresult1)
fin.write(strresult2)
fin.flush()
fin.write(strresult3)
fin.write(strresult4)
fin.write(strresult5)
flag = input("do you want to close")
if flag :
    fin.close()
print("Writting is done")
fout = open("result.txt",'r')
print(fout.read())
fout.close()