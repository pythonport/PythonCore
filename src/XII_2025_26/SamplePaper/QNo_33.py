'''
Created on Mar 19, 2026

@author: admin
'''
import csv

def Accept() :
    fout = open('Sales.csv','w', newline='')
    witerObject = csv.writer(fout)
    
    Product_ID = input('Product_ID - ')
    Product_Name = input('Product_Name - ')
    Quantity_Sold = input('Quantity_Sold - ')
    Price_Per_Unit = input('Price_Per_Unit - ')
    product = [Product_ID, Product_Name, Quantity_Sold, Price_Per_Unit]
    
    witerObject.writerow(product)
    

def CalculateTotalSales() :
    fout = open('Sales.csv','r')
    reader = csv.reader(fout)
    totalsales = 0
    for row in reader :
        sales = int(row[2])*int(row[3])
        totalsales+=sales
    return totalsales

Accept()
print(CalculateTotalSales())