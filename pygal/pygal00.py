import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 0.0"

bar_chart.add("Games",562)
bar_chart.add("Entertainment",64)
bar_chart.add("Education",43)
bar_chart.add("Photo & Video",40)
bar_chart.add("Utilities",29)
bar_chart.add("Health & Fitness",18)
bar_chart.add("Productivity",18)
bar_chart.add("Social Networking",27)
bar_chart.add("Lifestyle",21)
bar_chart.add("Music",9)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",16)
bar_chart.add("Book",22)
bar_chart.add("Finance",12)
bar_chart.add("Travel",6)
bar_chart.add("News",6)
bar_chart.add("Weather",3)
bar_chart.add("Reference",8)
bar_chart.add("Food & Drink",4)
bar_chart.add("Business",6)
bar_chart.add("Navigation",3)
bar_chart.add("Medical",2)
bar_chart.add("Catalogs",1)

bar_chart.render_to_file('00.svg')
