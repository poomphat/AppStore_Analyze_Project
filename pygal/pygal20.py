import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 2.0"

bar_chart.add("Games",60)
bar_chart.add("Entertainment",8)
bar_chart.add("Education",5)
bar_chart.add("Photo & Video",6)
bar_chart.add("Utilities",4)
bar_chart.add("Health & Fitness",2)
bar_chart.add("Productivity",2)
bar_chart.add("Social Networking",2)
bar_chart.add("Lifestyle",0)
bar_chart.add("Music",1)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",3)
bar_chart.add("Book",1)
bar_chart.add("Finance",3)
bar_chart.add("Travel",0)
bar_chart.add("News",1)
bar_chart.add("Weather",1)
bar_chart.add("Reference",2)
bar_chart.add("Food & Drink",1)
bar_chart.add("Business",1)
bar_chart.add("Navigation",0)
bar_chart.add("Medical",1)
bar_chart.add("Catalogs",0)

bar_chart.render_to_file('20.svg')
