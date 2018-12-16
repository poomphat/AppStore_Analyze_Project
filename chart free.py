import numpy as np
import pandas as pd
import json

data_file = pd.read_csv('AppleStore.csv')

free = 0
notfree = 0

price = data_file["price"]
for i in price:
    if i == 0:
        free += 1
    elif i > 0:
        notfree += 1
print("Free :", free)
print("Not free :", notfree)
            

    







    
