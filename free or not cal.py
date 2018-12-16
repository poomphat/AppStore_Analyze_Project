import numpy as np
import pandas as pd
import json

data_file = pd.read_csv('AppleStore.csv')

free50 = 0
free45 = 0
free40 = 0
free35 = 0
free30 = 0
free25 = 0
free20 = 0
free15 = 0
free10 = 0
free05 = 0
free00 = 0

notfree50 = 0
notfree45 = 0
notfree40 = 0
notfree35 = 0
notfree30 = 0
notfree25 = 0
notfree20 = 0
notfree15 = 0
notfree10 = 0
notfree05 = 0
notfree00 = 0

c = 1
box3 = []

box1 = data_file["price"].tolist()
box1 = [str(i-1) for i in box1]
box2 = data_file["user_rating"].tolist()
box2 = [str(i) for i in box2]
for x in box1:
    for y in box2[c::]:
        c += 1
        box3.append(x+" "+y)
        break

for y in box3:
    if "-1" in y:
        if " 5.0" in y:
            free50 += 1
        elif " 4.5" in y:
            free45 += 1
        elif " 4.0" in y:
            free40 += 1
        elif " 3.5" in y:
            free35 += 1
        elif " 3.0" in y:
            free30 += 1
        elif " 2.5" in y:
            free25 += 1
        elif " 2.0" in y:
            free20 += 1
        elif " 1.5" in y:
            free15 += 1
        elif " 1.0" in y:
            free10 += 1
        elif " 0.5" in y:
            free05 += 1
        elif " 0.0" in y:
            free00 += 1
    elif "-1" not in y:
        if " 5.0" in y:
            notfree50 += 1
        elif " 4.5" in y:
            notfree45 += 1
        elif " 4.0" in y:
            notfree40 += 1
        elif " 3.5" in y:
            notfree35 += 1
        elif " 3.0" in y:
            notfree30 += 1
        elif " 2.5" in y:
            notfree25 += 1
        elif " 2.0" in y:
            notfree20 += 1
        elif " 1.5" in y:
            notfree15 += 1
        elif " 1.0" in y:
            notfree10 += 1
        elif " 0.5" in y:
            notfree05 += 1
        elif " 0.0" in y:
            notfree00 += 1

print("FreeRate 5.0 :",free50)
print("FreeRate 4.5 :",free45)
print("FreeRate 4.0 :",free40)
print("FreeRate 3.5 :",free35)
print("FreeRate 3.0 :",free30)
print("FreeRate 2.5 :",free25)
print("FreeRate 2.0 :",free20)
print("FreeRate 1.5 :",free15)
print("FreeRate 1.0 :",free10)
print("FreeRate 0.5 :",free05)
print("FreeRate 0.0 :",free00)
print()
print("Not free Rate 5.0 :",notfree50)
print("Not free Rate 4.5 :",notfree45)
print("Not free Rate 4.0 :",notfree40)
print("Not free Rate 3.5 :",notfree35)
print("Not free Rate 3.0 :",notfree30)
print("Not free Rate 2.5 :",notfree25)
print("Not free Rate 2.0 :",notfree20)
print("Not free Rate 1.5 :",notfree15)
print("Not free Rate 1.0 :",notfree10)
print("Not free Rate 0.5 :",notfree05)
print("Not free Rate 0.0 :",notfree00)


    







    
