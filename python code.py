import numpy as np
import pandas as pd
import json
data_file = pd.read_csv('AppleStore.csv')
data_file.sort_values(by=['price'])
print(data_file.sort_values(by=['price']))