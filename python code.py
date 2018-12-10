import numpy as np
import pandas as pd
import json
#open file AppleSotore.CSV 
data_file = pd.read_csv('AppleStore.csv')
#Sort price
data_file.sort_values(by=['price'])
#output datafile
print(data_file.sort_values(by=['price']))