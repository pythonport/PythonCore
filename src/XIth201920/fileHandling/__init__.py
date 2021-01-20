'''
File handling in python
'''

fout = open("jnvbokro.txt",'w')
admno = input("Enter admno - ")
name = input("Enter name - ")
marks = input("Enter marks - ")

stustr = admno+","+name+","+marks
fout.write(stustr)
fout.close()