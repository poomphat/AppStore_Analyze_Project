import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 1.5"

bar_chart.add("Games",34)
bar_chart.add("Entertainment",2)
bar_chart.add("Education",4)
bar_chart.add("Photo & Video",3)
bar_chart.add("Utilities",1)
bar_chart.add("Health & Fitness",0)
bar_chart.add("Productivity",0)
bar_chart.add("Social Networking",0)
bar_chart.add("Lifestyle",0)
bar_chart.add("Music",2)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",2)
bar_chart.add("Book",1)
bar_chart.add("Finance",1)
bar_chart.add("Travel",0)
bar_chart.add("News",1)
bar_chart.add("Weather",0)
bar_chart.add("Reference",4)
bar_chart.add("Food & Drink",0)
bar_chart.add("Business",1)
bar_chart.add("Navigation",0)
bar_chart.add("Medical",0)
bar_chart.add("Catalogs",0)

bar_chart.render_to_file('15.svg')
