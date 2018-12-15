import numpy as np
import pandas as pd
import json

data_file = pd.read_csv('AppleStore.csv')
num = len(data_file["id"])
print(num)
for i in range(num):
     num = data_file[i-1:i]
     print(num["user_rating"])