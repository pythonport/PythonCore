'''
Created on Feb 24, 2022
https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
@author: admin
'''
import numpy as np
import pandas as pd
dates = pd.date_range("20210101", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)