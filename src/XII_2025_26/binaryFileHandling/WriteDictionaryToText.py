'''
Created on Aug 7, 2025

@author: admin
'''
fh = open('emp.txt','w')
e1 = {'ecode':452,'ename':'ramesh','salary':784512,'dept':'sales'}
e2 = {'ecode':745,'ename':'kamlesh','salary':764502,'dept':'service'}
e3 = {'ecode':124,'ename':'vimlesh','salary':774502,'dept':'backend'}
e4 = {'ecode':999,'ename':'kamla','salary':894592,'dept':'web developer'}

fh.write(str(e1))
fh.write(str(e2))
fh.write(str(e3))
fh.write(str(e4))
fh.close()
print('done')