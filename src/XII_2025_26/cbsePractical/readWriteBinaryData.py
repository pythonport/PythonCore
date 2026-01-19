'''
Created on Jan 19, 2026
Write two functions to writeEmp() ane readEmp() function to write and
read employee data where employee having structure like below
{'ecode':452,'ename':'ramesh','salary':784512,'dept':'sales'}
@author: admin
'''
import pickle
def writeEmp() :
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

def readEmp():
    fh = open('emp.dat','rb')
    try :
        while True :
            nemp = pickle.load(fh)
            print(nemp)
    except EOFError :
        print('file ended now ')
        fh.close()
writeEmp()
readEmp()