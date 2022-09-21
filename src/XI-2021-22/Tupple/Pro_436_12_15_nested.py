stu = (11,'Riya',(90,98,94,95,91))
total = 500
print('Minimum marks scored by -',stu[1],' is - ',min(stu[2]))
print('Maximum marks scored by -',stu[1],' is - ',max(stu[2]))
print('Total marks scored by -',stu[1],' is - ',sum(stu[2]))
percentMarks = (sum(stu[2])/total)*100
print('Percent marks scored by -',stu[1],' is - ',percentMarks)