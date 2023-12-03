#removing the duplicate values by duplicate methods.
import pandas as pd
cell=pd.read_csv('day.csv')
# return true for duplicate value and false for else case.
print(cell.duplicated())

# removing  duplicates
import pandas as pd
cell=pd.read_csv('day.csv')
cell.drop_duplicates(inplace=True)
print(cell.to_string())
