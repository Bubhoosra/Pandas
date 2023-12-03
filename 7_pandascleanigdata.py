#cleaning data:it means fixing the bad data in your dataset(set of data).
# bad data could be empty cell,data in a wrong format, duplicate data and wrong data.
#empty cell:it will give u wrong results,we will have to remove the rows always that contain the bad data.
# loading and reading the original file
# import pandas as pd
# cell=pd.read_excel('dirtydata.xlsx')
# print(cell.to_string())
# here we will return a new data frame with no empty cell by using dropna().
import pandas as pd
cell=pd.read_csv('day.csv')
cellnew=cell.dropna()
print(cellnew)


# this is not working in excel sheet?
# import pandas as pd
# cell=pd.read_excel('dirtydata.xlsx')
# cellnew=cell.dropna()
# print(cellnew)

# if at any case you want to change the original dataframe, then use the inplace=True argumant.it will
# remove the rows containg the null(NaN) values.
import pandas as pd
cell=pd.read_csv('day.csv')
cell.dropna(inplace=True)
print(cell.to_string())

# replacing the null values with a values by fillna()
import pandas as pd
cell=pd.read_csv('day.csv')
cell.fillna(120,inplace=True)
print(cell.to_string())


# here we can use also replace the empty cell using
# mean(), median(),mode()
# CLACULATE THE mean and replace the empty values.
import pandas as pd
cell=pd.read_csv(('day.csv'))
x=cell["Numeric"].mean()
cell["Numeric"].fillna(x,inplace=True)
print(cell.to_string())

# Calculate the median and replace any empty values from it.
import pandas as pd
cell=pd.read_csv(('day.csv'))
x=cell["Numeric"].median()
cell["Numeric"].fillna(x,inplace=True)
print(cell.to_string())

# Calculate the mode and replace any empty values from it.
import pandas as pd
cell=pd.read_csv(('day.csv'))
x=cell["Numeric"].mode()[0]
cell["Numeric"].fillna(x,inplace=True)
print(cell.to_string())



