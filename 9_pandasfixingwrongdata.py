#wrong data:odd data in dataset.
# here we will set coulmn that havingthe uncommon value manually.
import pandas as pd
cell=pd.read_csv('day.csv')
cell.loc[4,"Numeric"]=8
print(cell.to_string())

# for larger dataset:Now, here we will loop through all the values in "Numeric" column, if the values is higher than 8 than set it 
# to 8
import pandas as pd
cell=pd.read_csv('day.csv')
for i in cell.index:
    if  cell.loc[i,"Numeric"]>8:
        cell.loc[i,"Numeric"]=8
print(cell.to_string())


#you can also remove the data from looping
import pandas as pd
cell=pd.read_csv('day.csv')
for i in cell.index:
    if  cell.loc[i,"Numeric"]>8:
        cell.dropna(i,inplace=True)
print(cell.to_string())
