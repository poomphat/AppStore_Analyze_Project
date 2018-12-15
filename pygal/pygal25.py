import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 2.5"

bar_chart.add("Games",44)
bar_chart.add("Entertainment",40)
bar_chart.add("Education",16)
bar_chart.add("Photo & Video",16)
bar_chart.add("Utilities",13)
bar_chart.add("Health & Fitness",2)
bar_chart.add("Productivity",2)
bar_chart.add("Social Networking",6)
bar_chart.add("Lifestyle",12)
bar_chart.add("Music",3)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",12)
bar_chart.add("Book",3)
bar_chart.add("Finance",6)
bar_chart.add("Travel",3)
bar_chart.add("News",2)
bar_chart.add("Weather",2)
bar_chart.add("Reference",1)
bar_chart.add("Food & Drink",3)
bar_chart.add("Business",5)
bar_chart.add("Navigation",0)
bar_chart.add("Medical",0)
bar_chart.add("Catalogs",0)

bar_chart.render_to_file('25.svg')
