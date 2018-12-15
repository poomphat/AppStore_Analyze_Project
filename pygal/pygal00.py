import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 0"

bar_chart.add("Games",463)
bar_chart.add("Entertainment",64)
bar_chart.add("Education",66)
bar_chart.add("Photo & Video",24)
bar_chart.add("Utilities",29)
bar_chart.add("Health & Fitness",21)
bar_chart.add("Productivity",6)
bar_chart.add("Social Networking",33)
bar_chart.add("Lifestyle",31)
bar_chart.add("Music",4)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",13)
bar_chart.add("Book",47)
bar_chart.add("Finance",33)
bar_chart.add("Travel",10)
bar_chart.add("News",15)
bar_chart.add("Weather",6)
bar_chart.add("Reference",11)
bar_chart.add("Food & Drink",11)
bar_chart.add("Business",4)
bar_chart.add("Navigation",15)
bar_chart.add("Medical",3)
bar_chart.add("Catalogs",5)

bar_chart.render_to_file('00.svg')
