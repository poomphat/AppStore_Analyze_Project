import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 4"

bar_chart.add("Games",2832)
bar_chart.add("Entertainment",281)
bar_chart.add("Education",277)
bar_chart.add("Photo & Video",241)
bar_chart.add("Utilities",131)
bar_chart.add("Health & Fitness",118)
bar_chart.add("Productivity",136)
bar_chart.add("Social Networking",80)
bar_chart.add("Lifestyle",75)
bar_chart.add("Music",109)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",45)
bar_chart.add("Book",56)
bar_chart.add("Finance",38)
bar_chart.add("Travel",47)
bar_chart.add("News",34)
bar_chart.add("Weather",47)
bar_chart.add("Reference",37)
bar_chart.add("Food & Drink",29)
bar_chart.add("Business",40)
bar_chart.add("Navigation",25)
bar_chart.add("Medical",14)
bar_chart.add("Catalogs",4)

bar_chart.render_to_file('40.svg')
