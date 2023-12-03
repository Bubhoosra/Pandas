# data in a wrong fromat:to fix this problem 
# 1. to remove that row
#2. convert all the cells in same format.
# now lets try to convert all the cells in the same format
import pandas as pd
cell=pd.read_csv('dirtydata.csv')
cell["date"]=pd.to_datetime(cell["date"])
print(cell.to_string())
