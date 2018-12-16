import os
import uuid
from pygal import *
bar_chart = Bar()
bar_chart.title = "Free & Not free"
dis = ["0.0", "0.5", "1.0", "1.5", "2.0", "2.5", "3.0", "3.5", "4.0", "4.5", "5.0"]
bar_chart.x_labels = map(str, dis)

bar_chart.add("Free",[591,0,22,31,52,112,215,390,918,1436,288])
bar_chart.add("Not free",[338,0,22,25,54,84,168,312,707,1227,204])


bar_chart.render_to_file('free.svg')
