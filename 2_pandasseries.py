# A  pandas series is like a column in a table. It is 1d array which holds data of any type.

import pandas as pd
l=[1,2,3]
r=pd.Series(l)
print(r)

# labeling- label can be use to access a specified value.
import pandas as pd
sharad=[1,2,3]
sharadnew=pd.Series(sharad,index=["x","y","z"])
print(sharadnew)
# we can use a key-value objects like a dictionary, when creating a series.
#here we will create a simple pandas library series from a dictionary.
import pandas as pd
cal={"day1":345,"day2":456,"day3":908}
sharadnew=pd.Series(cal)
print(sharadnew)