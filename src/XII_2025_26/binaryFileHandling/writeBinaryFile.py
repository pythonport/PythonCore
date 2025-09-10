'''
Created on Aug 7, 2025
Code to demnonstrate the use of pickle module to write dictionary into file.
@author: admin
'''
import pickle
fh = open('emp.dat','wb')
e1 = {'ecode':452,'ename':'ramesh','salary':784512,'dept':'sales'}
e2 = {'ecode':745,'ename':'kamlesh','salary':764502,'dept':'service'}
e3 = {'ecode':124,'ename':'vimlesh','salary':774502,'dept':'backend'}
e4 = {'ecode':999,'ename':'kamla','salary':894592,'dept':'web developer'}

pickle.dump(e1, fh)
pickle.dump(e2, fh)
pickle.dump(e3, fh)
pickle.dump(e4, fh)
fh.close()
print('done')