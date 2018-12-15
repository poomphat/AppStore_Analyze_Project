import os
import uuid
from pygal import *
bar_chart = HorizontalBar()
bar_chart.title = "Rate 0.5"

bar_chart.add("Games",0)
bar_chart.add("Entertainment",0)
bar_chart.add("Education",0)
bar_chart.add("Photo & Video",0)
bar_chart.add("Utilities",0)
bar_chart.add("Health & Fitness",0)
bar_chart.add("Productivity",0)
bar_chart.add("Social Networking",0)
bar_chart.add("Lifestyle",0)
bar_chart.add("Music",0)
bar_chart.add("Shoping",0)
bar_chart.add("Sports",0)
bar_chart.add("Book",0)
bar_chart.add("Finance",0)
bar_chart.add("Travel",0)
bar_chart.add("News",0)
bar_chart.add("Weather",0)
bar_chart.add("Reference",0)
bar_chart.add("Food & Drink",0)
bar_chart.add("Business",0)
bar_chart.add("Navigation",0)
bar_chart.add("Medical",0)
bar_chart.add("Catalogs",0)

bar_chart.render_to_file('05.svg')
