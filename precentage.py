import numpy as np
import pandas as pd
import json
free = 0
notfree = 0


data_file = pd.read_csv('AppleStore.csv')

for i in data_file["price"]:
    if i == 0:
        free += 1
    else:
        notfree += 1
print(free)
print(notfree)