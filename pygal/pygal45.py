import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 4.5"

bar_chart.add("Games",1664)
bar_chart.add("Entertainment",118)
bar_chart.add("Education",134)
bar_chart.add("Photo & Video",154)
bar_chart.add("Utilities",62)
bar_chart.add("Health & Fitness",81)
bar_chart.add("Productivity",78)
bar_chart.add("Social Networking",36)
bar_chart.add("Lifestyle",29)
bar_chart.add("Music",58)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",15)
bar_chart.add("Book",30)
bar_chart.add("Finance",20)
bar_chart.add("Travel",24)
bar_chart.add("News",12)
bar_chart.add("Weather",24)
bar_chart.add("Reference",21)
bar_chart.add("Food & Drink",15)
bar_chart.add("Business",22)
bar_chart.add("Navigation",13)
bar_chart.add("Medical",11)
bar_chart.add("Catalogs",1)

bar_chart.render_to_file('45.svg')
