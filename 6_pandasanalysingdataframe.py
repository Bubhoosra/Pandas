# quick view of analysing dataframe:one of the most used methods for a quick overview of the dataframe is th 
#head method: this methods retuns the header or specified rows.
# here we will print first 10 rows in th dataframe.
import pandas as pd
cell=pd.read_csv('day.csv')
print(cell.head(10))

# here we will print last 10 rows
import pandas as pd
cell=pd.read_csv('day.csv')
print(cell.tail(10))

#what idf u want the information in the dataframe.via info
import pandas as pd
cell=pd.read_csv('day.csv')
print(cell.info())




