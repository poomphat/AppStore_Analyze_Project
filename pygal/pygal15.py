import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 1.5"

bar_chart.add("Games",10)
bar_chart.add("Entertainment",6)
bar_chart.add("Education",3)
bar_chart.add("Photo & Video",4)
bar_chart.add("Utilities",6)
bar_chart.add("Health & Fitness",3)
bar_chart.add("Productivity",2)
bar_chart.add("Social Networking",3)
bar_chart.add("Lifestyle",7)
bar_chart.add("Music",0)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",1)
bar_chart.add("Book",0)
bar_chart.add("Finance",6)
bar_chart.add("Travel",1)
bar_chart.add("News",1)
bar_chart.add("Weather",1)
bar_chart.add("Reference",1)
bar_chart.add("Food & Drink",0)
bar_chart.add("Business",0)
bar_chart.add("Navigation",0)
bar_chart.add("Medical",1)
bar_chart.add("Catalogs",0)

bar_chart.render_to_file('15.svg')
