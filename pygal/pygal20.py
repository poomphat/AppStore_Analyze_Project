import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 2"

bar_chart.add("Games",577)
bar_chart.add("Entertainment",120)
bar_chart.add("Education",114)
bar_chart.add("Photo & Video",91)
bar_chart.add("Utilities",72)
bar_chart.add("Health & Fitness",43)
bar_chart.add("Productivity",48)
bar_chart.add("Social Networking",30)
bar_chart.add("Lifestyle",36)
bar_chart.add("Music",31)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",33)
bar_chart.add("Book",14)
bar_chart.add("Finance",21)
bar_chart.add("Travel",25)
bar_chart.add("News",19)
bar_chart.add("Weather",14)
bar_chart.add("Reference",8)
bar_chart.add("Food & Drink",19)
bar_chart.add("Business",15)
bar_chart.add("Navigation",7)
bar_chart.add("Medical",2)
bar_chart.add("Catalogs",2)

bar_chart.render_to_file('20.svg')
