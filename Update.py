import numpy as np
import pandas as pd
import json
no_update = 0
bad = 0
good = 0
no_rating =0


data_file = pd.read_csv('AppleStore.csv')
lis1 = data_file["user_rating"].tolist()
lis2 = data_file["user_rating_ver"].tolist()

for i in range(len(data_file["user_rating"])):
    if lis1[i] == lis2[i] :
        no_update += 1
    elif lis1[i] > lis2[i]:
        bad += 1
    elif  lis1[i] < lis2[i]:
        good += 1

print("no_update:", no_update)
print("bad      :", bad)
print("good     :", good)
