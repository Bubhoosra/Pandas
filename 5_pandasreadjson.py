#json: Big data sets are normally stored and extract as json
# json is a plain text, format same an object.
import pandas as pd
dev=pd.read_json('sample1.json')
print(dev.to_string())

# disctionary as json
