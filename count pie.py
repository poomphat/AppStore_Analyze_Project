import os
import uuid
from pygal import *
pie_chart = Pie()
pie_chart.title = "Rating count (in %)"


pie_chart.add("Rate 5",492/7197*100)
pie_chart.add("Rate 4.5",2663/7197*100)
pie_chart.add("Rate 4",1626/7197*100)
pie_chart.add("Rate 3.5",702/7197*100)
pie_chart.add("Rate 3",383/7197*100)
pie_chart.add("Rate 2.5",196/7197*100)
pie_chart.add("Rate 2",106/7197/100)
pie_chart.add("Rate 1.5",56/7197/100)
pie_chart.add("Rate 1",44/7197*100)
pie_chart.add("Rate 0.5",0)
pie_chart.add("Rate 0",929/7197/100)

pie_chart.render_to_file('count pie.svg')
