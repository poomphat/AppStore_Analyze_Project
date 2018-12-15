import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 1"

bar_chart.add("Games",458)
bar_chart.add("Entertainment",93)
bar_chart.add("Education",102)
bar_chart.add("Photo & Video",80)
bar_chart.add("Utilities",48)
bar_chart.add("Health & Fitness",50)
bar_chart.add("Productivity",46)
bar_chart.add("Social Networking",31)
bar_chart.add("Lifestyle",30)
bar_chart.add("Music",28)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",40)
bar_chart.add("Book",12)
bar_chart.add("Finance",30)
bar_chart.add("Travel",24)
bar_chart.add("News",16)
bar_chart.add("Weather",24)
bar_chart.add("Reference",13)
bar_chart.add("Food & Drink",15)
bar_chart.add("Business",10)
bar_chart.add("Navigation",12)
bar_chart.add("Medical",10)
bar_chart.add("Catalogs",2)

bar_chart.render_to_file('10.svg')
