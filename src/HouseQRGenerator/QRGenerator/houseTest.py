'''
Created on Mar 5, 2022
Generate QR Code house wise
@author: admin
'''

import qrcode
import csv


def getFilePath(houseName):
    filePath = ''
    if (houseName == 'arawali-b') :
        filePath = r'C:\Users\admin\Documents\PyDevPrograms\PythonQRHouseWise\src\house\boy\arawal\arawal.csv'
    elif (houseName == 'nilgiri-b') :
        filePath = r'C:\Users\admin\Documents\PyDevPrograms\PythonQRHouseWise\src\house\boy\nilgiri\nilgiri.csv'
    elif (houseName == 'shivalik-b') :
        filePath = r'C:\Users\admin\Documents\PyDevPrograms\PythonQRHouseWise\src\house\boy\shivalik\shivalik.csv'
    elif (houseName == 'udaygiri-b') :
        filePath = r'C:\Users\admin\Documents\PyDevPrograms\PythonQRHouseWise\src\house\boy\udaygiri\udaygiri.csv'
    elif (houseName == 'arawali-g') :
        filePath = r'C:\Users\admin\Documents\PyDevPrograms\PythonQRHouseWise\src\house\girl\arawali\arawali.csv'
    elif (houseName == 'nilgiri-g') :
        filePath = r'D:\Python-Softwares-2023\PythonCode\PythonCore\src\HouseQRGenerator\house\girl\nilgiri\nilgiri.csv'
    elif (houseName == 'shivalik-g') :    
        filePath = r'C:\Users\admin\Documents\PyDevPrograms\PythonQRHouseWise\src\house\girl\shivalik\shivalik.csv'
    elif (houseName == 'udaygiri-g') :
        filePath = r'C:\Users\admin\Documents\PyDevPrograms\PythonQRHouseWise\src\house\girl\udaygiri\udaygiri.csv'
    return filePath


def getStudentList(filePath):
    lstStudent = []    
    with open(filePath, 'r') as csvfile:
    # creating a csv reader object
        csvreader = csv.DictReader(csvfile)
        # extracting each data row one by one
        for row in csvreader:
            stuDetails = {}
            for r in row :
                # print(r,' => ',row[r])
                stuDetails[r] = row[r]
            lstStudent.append(stuDetails)
    # print(lstStudent)
    return lstStudent


def generateHouseQR(stulist, boyGirl):
    for student in stulist :
        print(student)
        generateQR(student, boyGirl)
    

def generateQR(student, boyGirl): 
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=2,
    )
    House = student['House']
    Name = student['Name']
    
    qr.add_data(student)
    qr.make(fit=True)    
    img = qr.make_image(fill_color="black", back_color="white")
    # img.show()
    abpath = r'D:\Python-Softwares-2023\PythonCode\PythonCore\src\HouseQRGenerator\house'
    img.save(abpath + '\\' + boyGirl + '\\' + House + '\\' + House[0] + '-' + Name + ".png")


#main program starts here
houseList = ['arawali-b', 'arawali-g', 'nilgiri-b', 'nilgiri-g', 'shivalik-b', 'shivalik-g', 'udaygiri-b', 'udaygiri-g']    
filePath = getFilePath(houseList[3])
stulist = getStudentList(filePath)
if(len(stulist) != 0) :
    boyGirl = 'girl'  # girl  Change to boy/girl based on house data
    generateHouseQR(stulist, boyGirl)
    print('QR Generated ! Thumps up !')
else :
    print('No data found please check again.')
