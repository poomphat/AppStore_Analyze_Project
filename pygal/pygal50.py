import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 5.0"

bar_chart.add("Games",283)
bar_chart.add("Entertainment",27)
bar_chart.add("Education",29)
bar_chart.add("Photo & Video",15)
bar_chart.add("Utilities",18)
bar_chart.add("Health & Fitness",19)
bar_chart.add("Productivity",10)
bar_chart.add("Social Networking",13)
bar_chart.add("Lifestyle",9)
bar_chart.add("Music",10)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",1)
bar_chart.add("Book",6)
bar_chart.add("Finance",10)
bar_chart.add("Travel",5)
bar_chart.add("News",2)
bar_chart.add("Weather",5)
bar_chart.add("Reference",5)
bar_chart.add("Food & Drink",2)
bar_chart.add("Business",9)
bar_chart.add("Navigation",5)
bar_chart.add("Medical",2)
bar_chart.add("Catalogs",1)

bar_chart.render_to_file('50.svg')
