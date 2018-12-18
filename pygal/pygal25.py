import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 2.5"

bar_chart.add("Games",101)
bar_chart.add("Entertainment",85)
bar_chart.add("Education",16)
bar_chart.add("Photo & Video",7)
bar_chart.add("Utilities",3)
bar_chart.add("Health & Fitness",7)
bar_chart.add("Productivity",4)
bar_chart.add("Social Networking",7)
bar_chart.add("Lifestyle",3)
bar_chart.add("Music",6)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",3)
bar_chart.add("Book",3)
bar_chart.add("Finance",4)
bar_chart.add("Travel",1)
bar_chart.add("News",5)
bar_chart.add("Weather",3)
bar_chart.add("Reference",2)
bar_chart.add("Food & Drink",3)
bar_chart.add("Business",1)
bar_chart.add("Navigation",0)
bar_chart.add("Medical",0)
bar_chart.add("Catalogs",0)

bar_chart.render_to_file('25.svg')
