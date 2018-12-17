import numpy as np
import pandas as pd
import json

import os
import uuid
from pygal import *

bar_chart = Bar()
bar_chart.title = "Top 10 : Rating count"


data_file = pd.read_csv('AppleStore.csv')
data_file = data_file.sort_values(by=["rating_count_tot"])

list1 = data_file["rating_count_tot"].tolist()
list2 = data_file["track_name"].tolist()
list1.reverse()
list2.reverse()

for i in range(1,11):
    print(list2[i], ":", list1[i])
    bar_chart.add(list2[i],list1[i])

bar_chart.render_to_file('top10rc.svg')
