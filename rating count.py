import numpy as np
import pandas as pd
import json


datafile_rating_count5 = 0
datafile_rating_count45 = 0
datafile_rating_count4 = 0
datafile_rating_count35 = 0
datafile_rating_count3 = 0
datafile_rating_count25 = 0
datafile_rating_count2 = 0
datafile_rating_count15 = 0
datafile_rating_count1 = 0
datafile_rating_count05 = 0
datafile_rating_count0 = 0


data_file = pd.read_csv('AppleStore.csv')
for i in data_file["user_rating"]:
    if i == 5:
        datafile_rating_count5 += 1
    if i == 4.5:
        datafile_rating_count45 += 1
    if i == 4:
        datafile_rating_count4 += 1
    if i == 3.5:
        datafile_rating_count35 += 1
    if i == 3:
        datafile_rating_count3 += 1
    if i == 2.5:
        datafile_rating_count25 += 1
    if i == 2:
        datafile_rating_count2 += 1
    if i == 1.5:
        datafile_rating_count15 += 1
    if i == 1:
        datafile_rating_count1 += 1
    if i == 0.5:
        datafile_rating_count05 += 1
    if i == 0:
        datafile_rating_count0 += 1


print("rating 5   : ", datafile_rating_count5)
print("rating 4.5 : ", datafile_rating_count45)
print("rating 4   : ", datafile_rating_count4)
print("rating 3.5 : ", datafile_rating_count35)
print("rating 3   : ", datafile_rating_count3)
print("rating 2.5 : ", datafile_rating_count25)
print("rating 2   : ", datafile_rating_count2)
print("rating 1.5 : ", datafile_rating_count15)
print("rating 1   : ", datafile_rating_count1)
print("rating 0.5 : ", datafile_rating_count05)
print("rating 0   : ", datafile_rating_count0)
