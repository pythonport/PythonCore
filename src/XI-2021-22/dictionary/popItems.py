'''
Created on Mar 14, 2022

@author: admin
'''
d = {1:33, 2:44, 5:44, 6:76, 2:32}
keynum = 6
#pval = d.pop(keynum, "Key {0} not found".format(keynum))

pval = d.pop(keynum, None)
if(pval!=None) :
    print("returned value is  -", pval)
print("Done")