'''
Created on Feb 24, 2022
https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
Creating a Series by passing a list of values, 
letting pandas create a default integer index:
@author: admin
'''
import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)