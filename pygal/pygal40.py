import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 4.0"

bar_chart.add("Games",480)
bar_chart.add("Entertainment",145)
bar_chart.add("Education",94)
bar_chart.add("Photo & Video",72)
bar_chart.add("Utilities",600)
bar_chart.add("Health & Fitness",26)
bar_chart.add("Productivity",46)
bar_chart.add("Social Networking",35)
bar_chart.add("Lifestyle",33)
bar_chart.add("Music",41)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",23)
bar_chart.add("Book",24)
bar_chart.add("Finance",21)
bar_chart.add("Travel",21)
bar_chart.add("News",21)
bar_chart.add("Weather",20)
bar_chart.add("Reference",15)
bar_chart.add("Food & Drink",15)
bar_chart.add("Business",18)
bar_chart.add("Navigation",9)
bar_chart.add("Medical",5)
bar_chart.add("Catalogs",1)

bar_chart.render_to_file('40.svg')
