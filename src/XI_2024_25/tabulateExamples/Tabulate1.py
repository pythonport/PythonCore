'''
Created on Jan 23, 2025

@author: admin
'''
from tabulate import tabulate
table = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]

tbl = tabulate(table)
print(tbl)
print('--------')
print(tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"]))


table = [["spam",42],["eggs",451],["bacon",0]]
headers = ["item", "qty"]
print(tabulate(table, headers, tablefmt="grid"))