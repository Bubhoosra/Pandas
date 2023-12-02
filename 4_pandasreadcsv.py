# csv: comma separated file,it is a simple way to store the
# big and biggest data sets.csv files contains plain text.
# loading the csv into a dataframe.
# read_csv file to to_string(for loading th full data in vscode).
import pandas as pd
df=pd.read_csv('day.csv')
print(df.to_string())


# max_rows: you can check the your system maximum width.
import pandas as pd
print(pd.options.display.max_rows)
# yes, we can use the maximum no. of rows in our system.
