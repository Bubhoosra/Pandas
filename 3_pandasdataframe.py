# dataframe is a 2d data-structure with table including(rows, col)

import pandas as pd
cel={"name":["raj","ranu","tanu"],"age":[23,34,12]}
new=pd.DataFrame(cel)
print(new)

# locate new:pandas use the loc to return one or more row.
import pandas as pd
cel={"name":["raj","ranu","tanu"],"age":[23,34,12]}
new=pd.DataFrame(cel)
print(new.loc[0])

# example of returning row 0 and 1
import pandas as pd
cel={"name":["raj","ranu","tanu"],"age":[23,34,12]}
new=pd.DataFrame(cel)
print(new.loc[[0,1]])

# named-indexed: with th indexargument you can name on your own index.
import pandas as pd
cel={"name":["raj","ranu","tanu"],"age":[23,34,12]}
new=pd.DataFrame(cel,index=["roll1","roll2","roll3"])
print(new)

# loacte named index
import pandas as pd
cel={"name":["raj","ranu","tanu"],"age":[23,34,12]}
new=pd.DataFrame(cel,index=["roll1","roll2","roll3"])
print(new.loc["roll2"])

# load the data from th csv file into dataframe
import pandas as pd
fileload=pd.read_csv()

